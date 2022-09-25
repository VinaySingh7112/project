import pywhatkit
import datetime as dt
import random

# whatsup=pywhatkit.sendwhatmsg('+7024094276')

now=dt.datetime.now()
weekday=now.weekday()
if weekday == 1:
    with open("quotes.txt")as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.randint(all_quotes)
    print(quote)
    