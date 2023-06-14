import os
from flask import Flask
app = Flask(__name__)

@app.route("/trigger-here")
def triggerFunction():
    os.system("driver_drowsiness.py 1")
    return "Server is UP and is Running Please Refresh again"

if __name__ == '__main__':
    app.run()
