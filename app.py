from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Mr. Stark welcomes you by Snyder........'
    

print('your app is starting')


if __name__ == "__main__":
    app.run()
