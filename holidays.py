import requests
from datetime import datetime
from selectolax.parser import HTMLParser


def market_holidays_2022_list():
    url = "http://www.nasdaqtrader.com/trader.aspx?id=calendar"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    src = requests.get(url, headers=headers)
    calendar = HTMLParser(src.text)
    holiday = calendar.css('tr > td:first-child')
    holiday_list = []
    for item in holiday:
        holiday_date = datetime.strptime(item.text(), "%B %d, %Y")
        holiday_list.append(holiday_date.date())
    return holiday_list


market_holidays_2022_list()