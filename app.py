from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html>
<head><title>Sentiment Analysis</title></head>
<body>
    <h2>Sentiment Analysis</h2>
    <form method="post">
        <textarea name="text"></textarea><br>
        <input type="submit" value="Analyze">
    </form>
    {% if result %}
        <p>Polarity: {{ result.polarity }}</p>
        <p>Subjectivity: {{ result.subjectivity }}</p>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        result = TextBlob(text).sentiment
    return render_template_string(template, result=result)

if __name__ == "__main__":
    app.run(debug=True)
