"""
File name: pricing.py
Author: Salma Bouzid
	salma.bouzid@usherbrooke.ca
Date created: 02/08/2020
"""

from flask import Flask, request, jsonify, json
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)
RAPIDAPI_KEY    = "acae8306ecmsh3a05fc0e3299063p1b6991jsn8f3b83d177b8" #Your_RAPID_API_KEY
RAPIDAPI_HOST = "apidojo-yahoo-finance-v1.p.rapidapi.com"     #Your_RAPID_API_HOST
class Instrument(Resource):
	def get(self):
		url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"
		querystring = {"frequency":"1m", #The increment step
				"filter":"history",
				"period1":"1546448400", #The start date in epoch timestamp
				"period2":"1562086800", #The end date in epoch timestamp
				"symbol":"AMRN"} #The specified instrument to get the pricing for
		headers = {
			'x-rapidapi-host': RAPIDAPI_HOST,
			'x-rapidapi-key': RAPIDAPI_KEY
			}
		response = requests.request("GET", url, headers=headers, params=querystring)
		data = json.loads(response.text)
		return jsonify(data['prices'])

class Instrument_Pricing(Resource):
	def get(self):
		url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
		symbol_string = input("Enter the stock symbol: ")
		querystring = {"symbol": symbol_string}
		headers = {
			'x-rapidapi-host': RAPIDAPI_HOST,
			'x-rapidapi-key': RAPIDAPI_KEY
		}
		response = requests.request("GET", url, headers=headers, params=querystring)
		data = json.loads(response.text)
		return jsonify(data['price']['regularMarketPrice']) #To get the specific regular Market Price
		#return jsonify(data['price']) #To get all the information of pricing for the instrument


api.add_resource(Instrument, '/') # Route_1
api.add_resource(Instrument_Pricing, '/instrument') # Route_2



if __name__ == '__main__':
	app.run(port=5000)
