<<<<<<< HEAD
from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Starting Ml project"

# Git

@app.route('/hello',methods=['GET'])
def hello():
    return "Starting hello"



if __name__=="__main__":
=======
from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Starting Ml project"

# Git

@app.route('/hello',methods=['GET'])
def hello():
    return "Starting hello"



if __name__=="__main__":
>>>>>>> 5d2c3beeaa4234396adc882a043d255fd2b9066d
    app.run(debug=True,port=5050)