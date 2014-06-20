#Just testing the Working branch.

from ystockquote import *
import datetime

#Open the file with the list of stocks to fetch quote for and read each line into the stocks variable.
stocklist = open("d:\\git\\ystockquote\\stocklist.txt", "r")
indexlist = open("d:\\git\\ystockquote\\indexlist.txt", "r")

tickers = list(stocklist) + list(indexlist)

#Loop through the list appending the date and price for each stock to it's file.
for t in tickers:
    f = open("d:\\scratch\\" + t[:-1] + ".txt", "a")
    t = t[:-1]
    quote = (get_last_trade_price(t))
    string = str(datetime.date.today()) + str(": " + quote + "\n")
    print str(t + ": " + quote + "\n")
    f.write(string)
    f.close()
    
#Close the file.    
stocklist.close()