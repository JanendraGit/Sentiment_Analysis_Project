from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = None
    if request.method == 'POST':
        text = request.form.get('text_input')
        # TODO: Pass 'text' to your actual sentiment analysis model here
        if text:
            sentiment = "Positive" # Placeholder result
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)