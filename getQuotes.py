#Just testing the Working branch.

from ystockquote import *
import datetime

#Open a new file to write to and give it today's date as a filename.
f = open("d:\\scratch\\" + str(datetime.date.today()) + ".txt", 'w')

#Open the files with the list of stocks to fetch quote for and read each line into the stocks variable.
stocklist = open("d:\\git\\ystockquote\\stocklist.txt", "r")
stocks = list(stocklist)

#Loop through the list writing the latest price for each.
for s in stocks:
    s = s[:-1]
    quote = (get_last_trade_price(s))
    string = str(s + ": " + quote + "\n")
    print str(s + ": " + quote + "\n")
    f.write(string)


#Close the file.    
f.close()
stocklist.close()