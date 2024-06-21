from datetime import datetime
import pandas as pd
import numpy as np


def generate_date_range(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 6, 1)
    date_range = pd.date_range(start=start_date, end=end_date, freq='h')
    return date_range


def process_weather_data(input_file, cities, features):
    # Read the CSV file
    df = pd.read_csv(input_file, parse_dates=[['godina', 'mjesec', 'dan', 'sat']])
    df.rename(columns={'godina_mjesec_dan_sat': 'Datum'}, inplace=True)

    full_date_range = generate_date_range(2015, 2024)

    city_dfs = {city: pd.DataFrame(index=full_date_range) for city in cities}

    for city in cities:
        #uzmemo samo podatke za posmatrani grad
        city_data = df[df['grad'] == city]

        for feature in features:
            #uzimamo redom feature po feature za posmatrani grad i stavaljamo
            #na korespondirajucu poziciju (svako mjerenje ima datum, vrijeme)
            feature_data = city_data[city_data['parametar'] == feature]
            #set_index ce postaviti kolonu 'Datum' feature_data df-a kao index
            #kako i city_dfs[city] i df imaju index 'Datum', pandas ce ovo po default-u da alignuje
            #ostalo postavlja za NaN
            city_dfs[city][feature] = feature_data.set_index('Datum')['vrijednost']

        #sanity-check
        #city_dfs[city] = city_dfs[city].reindex(full_date_range)

        city_dfs[city]['godina'] = city_dfs[city].index.year
        city_dfs[city]['mjesec'] = city_dfs[city].index.month
        city_dfs[city]['dan'] = city_dfs[city].index.day
        city_dfs[city]['sat'] = city_dfs[city].index.hour

        columns_order = ['godina', 'mjesec', 'dan', 'sat'] + features
        city_dfs[city] = city_dfs[city][columns_order]

    return city_dfs

