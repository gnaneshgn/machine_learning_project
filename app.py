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
    app.run(debug=True,port=5050)