from search import Search

class Kiwi:
    def __init__(self, param_code, max_price, max_stopovers, date_from, date_to, airlines):
        self.param_code = param_code
        self.max_price = max_price
        self.max_stopovers = max_stopovers
        self.date_from = date_from
        self.date_to = date_to
        self.airlines = airlines

    def get_data(self):
        final = {}
        one_way = Search(self.param_code, self.date_from, self.date_to, self.max_price, self.max_stopovers, self.airlines, False)
        roundtrip = Search(self.param_code, self.date_from, self.date_to, self.max_price, self.max_stopovers, self.airlines, True)
        one_way_data = one_way.get()
        roundtrip_data = roundtrip.get()
        for data in one_way_data:
            code = data['flyTo']
            city = data['cityTo']
            country = data['countryTo']['name']
            match = [e for e in roundtrip_data if e['flyTo'] == code]
            final[(code, city, country)] = (data['price'], match[0]['price'] if match else '', data['distance'])
        return final

    def execute(self):
        data = self.get_data()
        return data
