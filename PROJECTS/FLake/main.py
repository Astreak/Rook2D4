from flask import *
import json

app=Flask(__name__)

data=[
	{"id":0,
	"name":["PRAJ","HELLO"],
	"age":[20,19]
	},
	{"id":1,
	"name":["PRJ","lol"],
	"age":[23,1]
	}


]



@app.route("/")
def home():
	return "<h1><center>API PAGE</center></h1>"

@app.route("/api")
def API():
	return jsonify(data)
@app.route("/ok",methods=["GET"])
def ok():
	if 'id' in request.args:
		id=int(request.args["id"])
	else:
		raise("OK No api id found");
	results=[]
	for D in data:
		if D['id']==id:
			results.append(D)

	return jsonify(results)



app.run(port=3000)
