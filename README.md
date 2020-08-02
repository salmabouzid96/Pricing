# Introduction
This code provides a python API that connects to "Yahoo Finance API Pricing".

# Before running on a terminal 
Make sure that you get your own subscription values : <Your_rapid_API_host> and <Your_rapid_API_Key>.     
- You can get your subscription's values by signing up in the link below :
https://rapidapi.com/apidojo/api/yahoo-finance1/pricing
- Then choose the Basic plan for 500 free API calls.
- Replace the RAPID KEY AND HOST by yours in the API script.

# How to run
1- Clone the project 
2- Create a virtual environment and install the packages needed after its activation
```
$ virtualenv venv
$ venv\Scripts\activate     #For Windows 
$ venv/bin/activate         #For Linux 
$ pip install -r requirements.txt


```
3- Run the script
```
python pricing.py

```
4- Access the API via 127.0.0.1:port/ (by specifing the same port used in the script: 5000 for this case)
 * Another route  127.0.0.1:port/instrument is available to provide you the pricing of a specific instrument that you enter via your cmd.
 
 # Functionalities
 - Connects to "Yahoo Finance API Pricing".
 - 127.0.0.1:port/ provides you with an instrument's pricing specified through the python API (in the params of your request).
 - 127.0.0.1:port/instrument provides you with a specific instrument's prcing that is specified by the user via the terminal through 'Enter the stock symbol'.
 
 # Development environment
* Python = 3.7

