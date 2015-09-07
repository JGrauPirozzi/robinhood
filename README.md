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

    pip install robinhood

Instructions for use:
---------------------

Place market order for 3 shares of RJET at best market price:

```python
>>> r = Robinhood(username, password)
>>> r.place_buy_order("RJET", 3, "market")
u'98a90ba4-fddf-440b-8156-5c4a59fe1931'
```

Instructions for use:

1.  Update auth.txt with your Robinhood username and password.
2.  Uncomment any commands in example.py that you want to run.
3.  Run: python example.py

If it doesn't work, open a GitHub issue.