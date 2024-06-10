'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

from bottle import route, run

@route('/')
def index():
    return "Hello, welcome to my Bottle web app!"

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
