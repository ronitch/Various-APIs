import requests
import json

country_code = {
    "India" : "newdelhi",
    "Japan" : "tokyo",
    "Germany" : "hamburg"
}

q = country_code["India"]

url_lockey = f"http://dataservice.accuweather.com/locations/v1/cities/search"

params_locationkey = {
    "apikey" : "", # Put your API Key from Accuweather here
    "q" : country_code["India"],
    "language": "en-us"
}

response_lockey = requests.get(url=url_lockey, params=params_locationkey)

if response_lockey.status_code == 200:
    print("Data retrieved successfully!")
    data_lockey = response_lockey.json()
    indiadata = "newdelhi_lockey.json"

    with open(indiadata, "w") as file:
        json.dump(data_lockey, file, indent=4)  
    
    print(f"Data stored at: {indiadata}")

else:
    e = response_lockey.status_code
    print("Location Key retrieval failed! Check Status Code: ", e)


with open("newdelhi_lockey.json", "r") as file:
    delhi_locdetails = json.load(file)
    delhi_locationKey = delhi_locdetails[0]["Key"]
    print(f"The Location Key is: {delhi_locationKey}")

forecast_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{delhi_locationKey}"

params_forecast = {
    "apikey": "",
    "language": "en-in"
}

response_forecast = requests.get(forecast_url, params=params_forecast)

if response_forecast.status_code == 200:
    forecast_response = response_forecast.json()
    forecast_data = "forecast_json.json"
    print(f"Data stored at: {forecast_data}")
    with open("forecast_json.json", "w") as file:
       json.dump(forecast_response, file)

else:
    print("Retrieval of forecast failed with Status Code: ", response_forecast.status_code)


