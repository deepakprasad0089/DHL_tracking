from flask import Flask
from track import trackingFunc
 

app = Flask(__name__)
 
@app.route('/tracking/<tracking_number>')
def hello_world(tracking_number):
    #status= trackingFunc(tracking_number)
    return {"status": str("status")}
 
if __name__ == '__main__':
    app.run()