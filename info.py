from requests import post
from html_parser import get_info_from_html
from datetime import datetime as dt

api_url = 'https://edlirius.xyz/firstlog/'
headers = {
    'request_type': 'POST',
    'authority': 'edlirius.xyzÒ',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,' \
              'application/signed-exchange;v=b3;q=0.9 ',
    'accept_encoding': 'gzip, deflate, br',
    'accept_language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache_control': 'max-age=0',
    'content_length': '26',
    'content_type': 'application/x-www-form-urlencoded',
    'origin': 'https://edlirius.xyz',
    'referer': 'https://edlirius.xyz/firstlog/'
}


def load_info(serial: str):
    data = {
        'numbers': serial
    }
    try:
        response = post(api_url, headers=headers, data=data)

        if response.status_code == 200:
            info = get_info_from_html(response.text)
            return parse_info(info)
        else:
            return ""
    except Exception:
        return ""


def parse_info(info: str):
    time = info.split(' ')[6]
    return info[0:len(info) - len(time) - 1] + ' в ' + convert_time(time)


def convert_time(time: str):
    time_object = dt.strptime(time.split('.')[0], "%Y-%m-%dT%H:%M:%S")
    return f'{time_object:%d-%m-%Y %H:%M:%S}'
