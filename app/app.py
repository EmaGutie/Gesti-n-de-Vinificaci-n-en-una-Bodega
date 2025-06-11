from flask import Flask
from config.data import DATA_BASE_URL
app=Flask(__name__)
app.config["DATA_BASE_URL"]=DATA_BASE_URL
app.config["DATA_TRACK_MODIFICATION"]=False
if __name__=="mail":
    app.run(debug=True)