import requests

API = '95e9eda81de49623b44c921a09cd570d'


def get_data(place, forecast_days, kind):

    run_time = forecast_days*8

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API}'

    req = requests.get(url=url)
    data = req.json()

    data_list = data['list']
    date = [item['dt_txt'] for item in data_list]

    if kind == 'Temperature':
        temp = [item['main']['temp']*0.1 for item in data_list]
        temp, date = temp[0:run_time], date[0:run_time]
        return date, temp
    else:
        sky = [item['weather'][0]['main'] for item in data_list]
        sky, date = sky[0:run_time], date[0:run_time]
        return sky, date


if __name__ == '__main__':
    example = get_data(place='london', forecast_days=1, kind='Sky')
    print(example)
