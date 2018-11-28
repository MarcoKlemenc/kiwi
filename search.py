import requests
from datetime import date, timedelta

class Search:

    def __init__(self, fly_from, date_from, date_to, max_price, max_stopovers, airlines, roundtrip):
        self.fly_from = fly_from
        self.date_from = date_from
        self.date_to = date_to
        self.max_price = max_price
        self.max_stopovers = max_stopovers
        self.airlines = airlines
        self.roundtrip = roundtrip

    def _get_response(self, request):
        try:
            return requests.get(request).json()
        except:
            return {}

    def _build_query(self):
        q = 'https://api.skypicker.com/flights?flyFrom={}&oneforcity=1&curr=ARS'.format(self.fly_from)
        if not self.date_from:
            today = date.today().strftime("%d/%m/%Y")
            today_next_year = (date.today() + timedelta(days=365)).strftime("%d/%m/%Y")
            q += '&dateFrom={}'.format(today, today_next_year)
        else:
            q += '&dateFrom={}'.format(self.date_from, self.date_from)
        if self.roundtrip:
            if not self.date_to:
                today = date.today().strftime("%d/%m/%Y")
                today_next_year = (date.today() + timedelta(days=365)).strftime("%d/%m/%Y")
                q += '&returnFrom={}&returnTo={}'.format(today, today_next_year)
            else:
                q += '&returnFrom={}&returnTo={}'.format(self.date_to, self.date_to)
        if str(self.max_price).isdigit() and not self.roundtrip:
            q += '&price_to={}'.format(self.max_price)
        if str(self.max_stopovers).isdigit():
            q += '&maxstopovers={}'.format(self.max_stopovers)
        if self.airlines:
            q += '&selectedAirlines={}'.format(self.airlines)
        return q

    def get(self):
        return self._get_response(self._build_query()).get('data')
