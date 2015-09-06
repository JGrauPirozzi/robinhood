from Robinhood import Robinhood

with open('auth.txt', 'r') as f:
	username = f.readline()
	password = f.readline()
	account = f.readline()

# Create a robinhood object
r = Robinhood(username, password, account)

## Place market order
order_ID = r.place_buy_order("CSCO", 1, "market")
print order_ID

## Place limit order for one share at $39 / share
order_ID = r.place_buy_order("CSCO", 1, "limit", 39)
print order_ID

## Cancel an order
r.cancel_order(order_ID)