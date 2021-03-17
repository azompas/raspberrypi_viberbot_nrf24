from flask import Flask, render_template, redirect, url_for
from random import randint
from communication import Communication
from threading import Thread

app=Flask(__name__)
com = Communication()
@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route("/runTask", methods=['POST'])
def long_task():
	n=randint(0,100)
	com.set_message(n)
	return redirect(url_for('index'))

if __name__=="__main__":
	t1 = Thread(target = com.run)
	t1.setDaemon(True)
	t1.start()
	#~ app.run(debug=True)  # trexei locally mono se debug mode
	# app.run(host='0.0.0.0', debug=True)  # texei sto dyktio (LAN) se
										   # debug mode me default port 5000
	app.run(host='0.0.0.0', port=8080, debug=True)  # texei sto dyktio (LAN) se
													# debug mode me sygkekrimeno port
