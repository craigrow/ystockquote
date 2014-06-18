#Just testing the Working branch.

from ystockquote import *
import datetime

#Open a new file to write to and give it today's date as a filename.
f = open("d:\\git\\ystockquote\\" + str(datetime.date.today()) + ".txt", 'w')

#Create a list of stocks to get quote for.
stocks = 'AIG', 'ALNY', 'AMBA', 'AMT', 'AMZN', 'BIDU', 'BOFI', 'BRK-B', 'CMG', 'DASTY', 'DDD', 'DNOW', 'GS', 'GTLS', 'INVN', 'IPGP', 'ISIS', 'ISRG', 'JNJ', 'JOBS', 'KMI', 'KO', 'LNKD', 'MA', 'MCD', 'MKL', 'NOV', 'OLED', 'P', 'PG', 'PRLB', 'PSMT', 'SSYS', 'TSLA', 'UPL', 'UPS', 'XONE', 'YNDX', 'Z'  

#Loop through the list writing the latest price for each.
for s in stocks:
    print s
    quote = (get_last_trade_price(s))
    print quote
    string = str(s + ": " + quote + "\n")
    print string
    f.write(string)
    
#Close the file.    
f.close()