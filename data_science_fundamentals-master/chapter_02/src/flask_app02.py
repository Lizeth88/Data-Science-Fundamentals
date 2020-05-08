from flask import Flask
from flask import jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world_json_list():
	tim=datetime.now()
	data =["Year: ",tim.year,"Month: ",tim.month, "Day: ",tim.day,"Hour: ",tim.hour,"Minutes: ",tim.minute,"Seconds: ",tim.second,]
	
	return jsonify(data)

if __name__ == '__main__':
    app.run()