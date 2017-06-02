from flask import Flask, render_template
app = Flask(__name__)

global state

@app.route("/")
def index():
    global state
    state = (state + 1) % 8
    return render_template('index.html', the_state=state)

@app.route("/static/jquery.js")
def jquery():
    return app.send_static_file('jquery.js')

if __name__ == "__main__":
    state = 0
    app.run()
