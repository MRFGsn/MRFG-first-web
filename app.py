from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'

print('This is My first web site')


if __name__ == "__main__":
    app.run()
