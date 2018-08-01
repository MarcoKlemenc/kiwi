import requests

class Search:

    def __init__(self, fly_from, fly_to, date_from, date_to, roundtrip, max_price, max_stopovers, airlines):
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.date_from = date_from
        self.date_to = date_to
        self.roundtrip = roundtrip
        self.max_price = max_price
        self.max_stopovers = max_stopovers
        self.airlines = airlines

    def _get_response(self, request):
        try:
            return requests.get(request).json()
        except:
            return {}

    def _build_query(self):
        q = 'https://api.skypicker.com/flights?flyFrom={}&dateFrom={}&dateTo={}&oneforcity=1&curr=ARS'.format(self.fly_from, self.date_from, self.date_to)
        if self.fly_to:
            q += '&to={}'.format(self.fly_to)
        if self.roundtrip:
            q += '&returnFrom={}&returnTo={}'.format(self.date_from, self.date_to)
        if str(self.max_price).isdigit():
            q += '&price_to={}'.format(self.max_price)
        if str(self.max_stopovers).isdigit():
            q += '&maxstopovers={}'.format(self.max_stopovers)
        if self.airlines:
            q += '&selectedAirlines={}'.format(self.airlines)
        return q

    def get(self):
        return self._get_response(self._build_query()).get('data')
