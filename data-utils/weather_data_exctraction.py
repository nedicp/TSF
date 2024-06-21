from utils import process_weather_data

input_file = 'CANU_export.csv'

cities = ["02BAR010", "02HNOV10", "02ULCN10", "02CTNJ20", "02PDGR10", "02NIKS10", "02KOLS10", "02PLJV10",
          "02ZBLJ10", "02BERA20", "02DANL20", "02BUDV20", "02BPLJ20"]

features = ["Ta1h", "Ha1h", "GRa1h", "BRV36H", "PRV36H", "RRa1h", "Pa1h"]

city_dataframes = process_weather_data(input_file, cities, features)


for city, df in city_dataframes.items():
    df.to_csv(f"{city}_weather_data.csv", index=False)

