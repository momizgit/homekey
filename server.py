from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/out', methods = ['GET'])
def ReturnJSON():
	if(request.method == 'GET'):
		data = {
			"Name" : "Light",
			"Status" : "ON",
			"IP" : "1.1.1.1",
		}

		return jsonify(data)

if __name__=='__main__':
	app.run(debug=True)
