from flask import Flask, render_template



app = Flask(__name__)

# app.register_blueprint(tasks_blueprint)

@app.route('/')
def home():
    return "hello pet lovers"

if __name__ == '__main__':
    app.run(debug=True)
