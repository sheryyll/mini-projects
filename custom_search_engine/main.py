from exa_py import Exa
from dotenv import dotenv_values

config = dotenv_values('.env')  

exa = Exa(config['API_KEY'])

query = input('Search here: ')

response = exa.search(
    query,
    num_results=5,
    type='keyword',
    include_domains=['https://www.twitter.com']
)

for result in response.results:
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print()
