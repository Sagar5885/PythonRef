import requests
from pprint import pprint

def main():
    city = "New York"
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d264b6e99cd4aea6634803a829e555c6")
    weather = response.json()
    pprint(weather)
    print(weather['main']['temp'])
    print(weather['weather'][0]['description'])

if __name__ == '__main__':
    main()