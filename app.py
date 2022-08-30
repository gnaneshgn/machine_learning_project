from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    return "Starting Ml project"

# Git
#Docker
@app.route('/hello',methods=['GET'])
def hello():
    return "Starting hello"





if __name__=="__main__":
    app.run()