from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Team MRFG'
    return 'I will kill you'

print('your app is starting')


if __name__ == "__main__":
    app.run()
