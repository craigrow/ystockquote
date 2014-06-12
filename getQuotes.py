from ystockquote import *

f = open('d:\\git\\ystockquote\\testfile', 'r')
stock = 'MSFT'
print stock
print(get_last_trade_price(stock))

stocks = 'MSFT', 'AMZN', 'UPL'


for s in stocks:
    print s
    print (get_last_trade_price(s))

"""
f = open('d:\\git\\ystockquote\\testfile', 'r')

for line in f:
    stock = str(line)
    print stock
    print(get_last_trade_price(stock))
    print line
    print price
"""
