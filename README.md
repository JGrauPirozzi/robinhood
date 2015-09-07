# easyRobinhood

Inspired by Rohonpai's Robinhood framework (https://github.com/rohanpai/Robinhood), benkroop/robinhood fixes bugs while adding new features and additional documentation. 

Current Features:
* Get stock quote
* Place market buy / sell orders
* Place limit buy / sell orders
* Cancel an open order
* View order details or status
* Retrieve a list of historical orders
* View current user information

To install:

    pip install -r requirements.txt

Instructions for use:
---------------------
Initializing

	r = Robinhood(username, password)

Get price quote

	price = r.quote_prices("AAPL")

Place market order for 3 shares of RJET at best market price

	order_ID = r.place_buy_order("RJET", 3, "market")

Instructions for use:

1.  Update auth.txt with your Robinhood username and password.
2.  Uncomment any commands in example.py that you want to run.
3.  Run: python example.py

If it doesn't work, open a GitHub issue.