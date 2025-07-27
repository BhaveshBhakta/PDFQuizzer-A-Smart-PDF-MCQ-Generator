import os
from flask import Flask, request, render_template
from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import summarize_text
from utils.mcq_generator import generate_mcqs
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    mcqs_text = None

    if request.method == "POST":
        file = request.files["pdf_file"]
        num_questions = request.form["num_questions"]
        topic = request.form.get("topic", "")

        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            text = extract_text_from_pdf(file_path)
            
            summary = summarize_text(text)
            print("\n🔍 SUMMARY:\n", summary)

            mcqs_output = generate_mcqs(summary, num_questions, topic)
            print("\n🧠 RAW MCQs OUTPUT:\n", mcqs_output)

            if isinstance(mcqs_output, dict):
                mcqs_text = mcqs_output.get("text", str(mcqs_output))
            else:
                mcqs_text = str(mcqs_output)

    return render_template("index.html", mcqs=mcqs_text)

if __name__ == "__main__":
    app.run(debug=True)
