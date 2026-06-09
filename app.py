from flask import Flask
from flask import render_template
from flask import request

from scanner.scanner import scan_file

import os

app = Flask(__name__, static_folder="statics")

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["file"]

        path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(path)

        findings = scan_file(path)

        high = 0
        medium = 0
        low = 0

        for item in findings:

            if item["severity"] == "HIGH":
                high += 1

            elif item["severity"] == "MEDIUM":
                medium += 1

            elif item["severity"] == "LOW":
                low += 1

        score = 100 - (high * 20) - (medium * 10)

        if score < 0:
            score = 0

        if score >= 80:
            risk = "LOW RISK"

        elif score >= 50:
            risk = "MEDIUM RISK"

        else:
            risk = "HIGH RISK"

        return render_template(
            "result.html",
            findings=findings,
            high=high,
            medium=medium,
            low=low,
            score=score,
            risk=risk
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        debug=True,
        use_reloader=False
    )