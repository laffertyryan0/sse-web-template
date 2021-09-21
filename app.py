#!/usr/bin/python

from flask import Flask, render_template, Response
import time

app = Flask(__name__)


def sendSSE():
    #send data via sse
    IPADDR = "localhost"
    while(True):
        data = '{"time":"'+time.strftime('%H:%M:%S', time.localtime())+'"}'
        yield 'data: '+ data +'\n\n'
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return Response(sendSSE(),mimetype = "text/event-stream")

@app.before_first_request
def start():
    sendSSE()
 
if __name__ == '__main__':
    app.run(debug=False, host = '0.0.0.0')
