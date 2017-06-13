from flask import Flask, render_template
app = Flask(__name__)

global state
state = 0

@app.route("/")
def index():
    global state
    state = (state + 1) % 9
    return render_template('index_ui.html', the_state=state)

if __name__ == "__main__":
    app.run()
