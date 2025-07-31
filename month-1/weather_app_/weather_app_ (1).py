import requests
key='8c4cb95607a2196784e651ad4441fae9'
city='cairo'

url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'

response=requests.get(url)

#response

#response.json()['main']

import requests
import pandas as pd

def weather_API():
    tries=0
    while True:

        if tries==0:
            choosen_city=input('enter the city name : ')
        else:
            choosen_city=input('enter another city name : ')

        key='8c4cb95607a2196784e651ad4441fae9'
        url=f'https://api.openweathermap.org/data/2.5/weather?q={choosen_city}&units=metric&appid={key}'
        response=requests.get(url)

        if response.status_code == 200:
            weather_data=response.json()['main']
            print(f"\n🌤️ Weather in {choosen_city.title()} 🌤️\n")

            df = pd.DataFrame(weather_data.items(), columns=['Parameter', 'Value'])
            print(df.to_string(index=False))
            print("*"*20)


        else:
            print(f'city {choosen_city} is not found 😔\n')

        tries+=1
        try_again=input('try again 🤷‍♀️? "y/n"')
        print("\n")
        if try_again !="y":
            print("🕊️ good bye")
            break
        else:
            continue

weather_API()
