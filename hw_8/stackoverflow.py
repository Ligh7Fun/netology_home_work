import datetime
import time

import requests

tags = 'Python'
days = 2
now = datetime.datetime.today()
to_date = int(time.mktime(datetime.date(now.year, now.month, now.day).timetuple()))
from_date = int(time.mktime(datetime.date(now.year, now.month, now.day - days).timetuple()))
url = f'https://api.stackexchange.com/2.3/questions?' \
      f'fromdate={from_date}&todate={to_date}' \
      f'&order=desc&sort=activity&tagged={tags}&site=stackoverflow'
request = requests.get(url).json()

for index, item in enumerate(request["items"], start=1):
    print(f'====== Question {index}/{len(request["items"])} ======')
    print(f'Author: {item["owner"]["display_name"]}\nTitle: {item["title"]}\nLink: {item["link"]}\n')
