import requests
from newsapi.newsapi_client import NewsApiClient
import random

# Stocks price checker API
STOCKS_PRICE_API_URL = "https://www.alphavantage.co/query"
STOCKS_PRICE_API_KEY = "MIUGEQRN5YDDL5OE"
symbol = "TSLA"
interval = "60min"
SP_PARAMETERS = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": symbol,
    "interval": interval,
    "apikey": STOCKS_PRICE_API_KEY,
}

sp_response = requests.get(url=STOCKS_PRICE_API_URL, params=SP_PARAMETERS)
data = sp_response.json()["Time Series (60min)"]

data_date = list(data.keys())[0].split(" ")[0]

# News API
NEWS_API_KEY = "abd8ad9e79e9498c8fd58c72bb0cf1f1"
NEWS_API_SOURCES = "bloomberg, " \
                   "australian-financial-review," \
                   "business-insider," \
                   "business-insider-uk," \
                   "die-zeit," \
                   "financial-post," \
                   "fortune," \
                   "handelsblatt," \
                   "info-money,"

# according to sample data, stocks price data will be 4 days late from time_now
# we will try work with the latest info


def is_changed_alot():
    data_values_list = list(data.values())

    today_close_price = data_values_list[0]["4. close"]
    yesterday_close_price = data_values_list[24]["4. close"]

    today_close_price, yesterday_close_price = float(today_close_price), float(yesterday_close_price)

    percentage = round(today_close_price / yesterday_close_price * 100)

    if percentage > 110 or percentage < 90:
        return True, percentage
    else:
        return False, percentage


def get_news():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    all_articles = newsapi.get_everything(q='tesla', sources=NEWS_API_SOURCES)["articles"]

    # Sample key - value for time
    # "publishedAt": "2022-08-01T12:30:59Z"

    time_relevance_articles = []

    for articles in all_articles:
        articles_datetime = articles["publishedAt"]
        articles_date = articles_datetime.split("T")[0]
        if articles_date == data_date:
            time_relevance_articles.append(articles)

    return time_relevance_articles


is_changed_alot_result = is_changed_alot()

# if is_changed_alot_result[0] is False:
#     exit("Nothing much happened")
news = get_news()
random_news = random.choice(news)
print(random_news["title"])
print(random_news["description"])

