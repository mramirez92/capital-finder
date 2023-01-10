from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # global message
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # https://capital-finder-2.vercel.app/api/capital_finder?country=chile
        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["country"])
            data = r.json()
            country_info = []
            for country_data in data:
                capital = country_data["capital"][0]
                name = country_data["name"]["common"]
                country_info.append(capital)
                country_info.append(name)
                # country_info.append(capital)
            message = f"The capital of {country_info[1]} is {country_info[0]}."

        else:
            self.send_error(404, "Country not found.")

        if "capital" in dic:
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            country = []
            for country_data in data:
                capital = country_data["capital"][0]
                name = country_data["name"]["common"]
                country.append(capital)
                country.append(name)
            message = f"{country[0]} is the capital of {country[1]} ."
        else:
            self.send_error(404, "Capital not found.")

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
