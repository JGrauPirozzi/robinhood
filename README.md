# robinhood

This library facilitates automated, commission-free stock trading from Python using Robinhood's API.

Current Features:
* Get stock quote
* Place market buy / sell orders
* Place limit buy / sell orders
* Cancel an open order
* View order details or status
* Retrieve a list of historical orders
* View current user information

To install:

    pip install robinhood


Inspired by Rohonpai's Robinhood framework (https://github.com/rohanpai/Robinhood), benkroop/robinhood fixes bugs while adding new features and additional documentation. 

Instructions for use:
---------------------

Place market order for 3 shares of RJET at best market price:

```python
>>> r = Robinhood(username, password)
>>> r.place_buy_order("RJET", 3, "market")
u'98a8caa4-fddf-df0b-8156-5c474dc01931'
```
Get a quote for AAPL
```python
>>> r.quote_price('AAPL')
u'109.2700'
```
Place limit order for 1 share of CSCO at a limit of $28.42 per share
```python
>>> r.place_buy_order("CSCO", 1, "limit", 28.42)
u'52ad96db-4c01-29c8-9951-a31f883853b5'
```
Cancel an order
```python
>>> r.cancel_order("52ad96db-4c01-29c8-9951-a31f883853b5")
<Response [200]>
```
Get order status
```python
>>> r.order_status("52ad96db-4c01-29c8-9951-a31f883853b5")
u'cancelled'
```
Get most recent order
```python
>>> r.list_orders()[0]
u'52ad96db-4c01-29c8-9951-a31f883853b5'
```
Get details of most recent order
```python
>>> order_ID = r.list_orders()[0]
>>> order = r.order_details(order_ID)
{u'cumulative_quantity': u'0.00000', u'last_transaction_at': u'2015-09-07T07:12:03.726590Z', u'account': u'https://api.robinhood.com/accounts/2PY73824/', u'stop_price': None, u'reject_reason': None, u'state': u'cancelled', u'url': u'https://api.robinhood.com/orders/52ad96db-4c01-29c8-9951-a31f883853b5/', u'created_at': u'2015-09-07T07:12:03.726590Z', u'updated_at': u'2015-09-07T07:12:03.743988Z', u'executions': [], u'price': u'3.25000000', u'instrument': u'https://api.robinhood.com/instruments/975cfe9d-8197-44f9-b07a-a18387cfae63/', u'time_in_force': u'gfd', u'trigger': u'immediate', u'fees': u'0.00', u'cancel': None, u'position': u'https://api.robinhood.com/accounts/2PY73824/positions/975cfe9d-8197-44f9-b07a-a183878493ac/', u'quantity': u'3.00000', u'type': u'market', u'average_price': None, u'side': u'buy'}
```
Print selected user info
```python
>>> print "Your address is: " + r.address + ", " + r.city + ", " + r.state_residence + " " + r.zipcode
Your address is: 121 Amherst St., Boston, MA 02111
```
