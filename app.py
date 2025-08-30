import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from utils import allowed_file, read_file_text, score_resume

# --- Flask setup ---
app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    resume_text_final = ""

    resume_file = request.files.get("resume_file")
    if resume_file and resume_file.filename:
        if not allowed_file(resume_file.filename):
            flash("Unsupported resume file type.")
            return redirect(url_for("index"))
        safe = secure_filename(resume_file.filename)
        path = os.path.join(app.config["UPLOAD_FOLDER"], safe)
        resume_file.save(path)
        resume_text_final = read_file_text(path)
        try:
            os.remove(path)
        except:
            pass

    if not resume_text_final:
        resume_text_final = request.form.get("resume_text", "").strip()

    if not resume_text_final:
        flash("Please provide a resume file or paste resume text.")
        return redirect(url_for("index"))

    jd_text = request.form.get("jd_text", "").strip()
    if not jd_text:
        flash("Please provide a job description.")
        return redirect(url_for("index"))

    score = score_resume(resume_text_final, jd_text)
    return render_template(
        "index.html",
        score=score,
        resume_preview=resume_text_final[:300] + "..." if resume_text_final else "N/A",
    )


if __name__ == "__main__":
    app.run(debug=True)
