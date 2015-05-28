__author__ = 'xz346'

import requests
import sys
def construct_url(q, num_of_days, key)  :
    url = 'http://api.worldweatheronline.com/free/v2/weather.ashx?q=%s&format=json&num_of_days=%d&key=%s' \
      % (q, num_of_days, key)
    return url

def call_weather_api(url) :
    r = requests.get(url)
    response = r.json()
    return response

def main() :
    q = sys.argv[1]
    num_of_days = int(sys.argv[2])
    key = "ddd48ba4eb492c9750032b9a1d1be"

    returnURL = construct_url(q, num_of_days, key)
    returnResponse = call_weather_api(returnURL)

    print(returnResponse)
    return

if __name__ == '__main__':
    main()