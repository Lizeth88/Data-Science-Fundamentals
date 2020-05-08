from flask import Flask
app = Flask(__name__)
from flask import jsonify
from datetime import datetime, date, time, timedelta 

@app.route('/')
def hello_world():
	time= datetime.now()
    data = ["año: ", time.year, "Mes: ", time.month, "Día: ", time.day, "Hora: ", time.hour, "Minutos: ", time.minute, "Segundos: ", time.second ]
	
	return jsonify(data)

if __name__ == '__main__':
    app.run()