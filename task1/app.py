from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, OpenTelemetry!"

@app.route('/slow')
def heavy():
    time.sleep(1)
    return "Slow request finished!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)