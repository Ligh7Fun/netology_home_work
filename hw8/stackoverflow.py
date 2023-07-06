import datetime
import time
import requests

tags = 'Python'
days = 2

page = 1
pagesize = 100
has_more = True
count_questions = 0

now = datetime.datetime.today()
to_date = int(time.mktime(datetime.date(now.year, now.month, now.day).timetuple()))
from_date = int(time.mktime(datetime.date(now.year, now.month, now.day - days).timetuple()))

while has_more:
    url = f'https://api.stackexchange.com/2.3/questions?' \
          f'fromdate={from_date}&todate={to_date}' \
          f'&order=desc&sort=activity&tagged={tags}&site=stackoverflow' \
          f'&pagesize={pagesize}&page={page}'

    request = requests.get(url).json()

    print(f'*** Page #{page} ***')

    for index, item in enumerate(request["items"], start=1):
        print(f'====== Question {index}/{len(request["items"])} ======')
        print(f'Author: {item["owner"]["display_name"]}\nTitle: {item["title"]}\nLink: {item["link"]}\n')

    count_questions += len(request["items"])
    has_more = request["has_more"]
    page += 1

print(f'Total pages: {page-1}')
print(f'Total questions: {count_questions}')
