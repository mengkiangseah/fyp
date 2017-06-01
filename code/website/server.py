from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def index():
    state = random.randint(1, 8)
    return render_template('index.html', the_state=state)

@app.route("/styles.css")
def css():
    state = 1
    return render_template('styles.css', the_state=state)

if __name__ == "__main__":
    app.run()
