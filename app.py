import sys

from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("we are raising custom excption")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.error(housing.error_message)
    logging.info("We are testing logging module")
    return "Starting Ml project"

# Git
#Docker






if __name__=="__main__":
    app.run(debug=True)