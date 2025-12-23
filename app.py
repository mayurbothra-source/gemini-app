from flask import Flask, request, render_template_string
import google.generativeai as genai

import os
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Gemini Test App</title>
<h2>Gemini App</h2>
<form method="post">
<input name="prompt" style="width:400px" placeholder="Enter your prompt">
<button type="submit">Submit</button>
</form>
<p>{{ response }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        result = model.generate_content(prompt)
        response = result.text
    return render_template_string(HTML, response=response)

if __name__ == "__main__":
    app.run(debug=True)


