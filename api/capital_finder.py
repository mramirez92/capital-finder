# https://restcountries.com/v3.1/name/peru/capital/lima
#
# https://restcountries.com/v3.1/capital/lima

from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["country"])
            data = r.json()
            country_info = []
            for country_data in data:
                name = country_data["capital"][0]
                # name = country_data["name"][0]
                # capital = country_data["capital"][0]
                country_info.append(name)
                # country_info.append(capital)
            city_capital = f" Y is the capital of {country_info[0]}"
        else:
            city_capital = "City not found"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(city_capital.encode())
        return
