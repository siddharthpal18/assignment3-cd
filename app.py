from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "This is Assignment 3 for Deploying Cloud Infrastructure class - Hello from Pal ECS Container."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
