from bs4 import BeautifulSoup
import pandas as pd
import requests


response = requests.get('https://en.wikipedia.org/wiki/Road_safety_in_Europe')
url = response.text
soup = BeautifulSoup(url, 'html.parser')

table = soup.find(class_='wikitable sortable')

df = pd.read_html(table.prettify())[0]

new_df = df.rename(columns={
    'Country': 'Country',
    'Area  (thousands of km  2  )  [23]': 'Area',
    'Population in 2018  [24]': 'Population',
    'GDP per capita in 2018  [25]': 'GDP per capita',
    'Population density  (inhabitants per km  2  ) in 2017  [26]': 'Population density',
    'Vehicle ownership  (per thousand inhabitants) in 2016  [27]': 'Vehicle ownership',
    'Total Road Deaths in 2018  [29]': 'Total road deaths',
    'Road deaths  per Million Inhabitants in 2018  [29]': 'Road deaths per Million Inhabitants',

})

new_df.drop(['Road Network Length  (in km) in 2013  [28]',
             'Number of People Killed  per Billion km  [29]',
             'Number of Seriously Injured in 2017/2018  [29]'],
            axis=1, inplace=True)

year_column = [2018 for i in range(29)]
new_df.insert(1, 'Year', year_column)

sorted_df = new_df.sort_values(by='Road deaths per Million Inhabitants')

# Converts the dataframe to csv
sorted_df.to_csv("myfile.csv", index=False)
