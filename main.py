from google_play_scraper import app

result = app(
    'com.humble.SlayTheSpire',
    lang='en',
    country='us'
)


print(f"{result['price']}\n {result['free']}\n {result['sale']}\n {result['saleTime']}\n {result['version']}\n {result['recentChanges']}")