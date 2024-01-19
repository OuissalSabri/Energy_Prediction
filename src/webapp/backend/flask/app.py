from flask import Flask
import pickle

with open('C://Users//HP//Documents//Downloads//Energy-Demand-Forecasting-master//Energy-Demand-Forecasting-master//src//webapp//backend//models//model.pkl', 'rb') as f:
	model = pickle.load(f)
	app = Flask(__name__)
	from routes import *
	if __name__ == '__main__':
		app.run(debug=True)
