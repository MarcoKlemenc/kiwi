from search import Search

class Kiwi:
    def __init__(self, param_mode, param_code, max_price, max_stopovers):
        self.param_mode = param_mode
        self.param_code = param_code
        self.max_price = max_price
        self.max_stopovers = max_stopovers

    def get_data(self, mode):
        from_airports = []
        final = {}
        req = Search(self.param_code, None, '01/07/2018', '31/12/2018', "R" in mode, self.max_price, self.max_stopovers)
        for data in req.get():
            code = data['flyTo']
            city = data['cityTo']
            country = data['countryTo']['name']
            if "A" in mode:
                from_airports.append((code, city, country))
            if "D" in mode:
                final[(code, city, country)] = (data['price'], data['distance'])
        if "A" in mode:
            i = 1
            for airport in from_airports:
                req = Search(airport[0], self.param_code, '01/07/2018', '31/12/2018', "R" in mode, None, self.max_stopovers)
                data = req.get()
                if data and (data[0]['price'] <= int(max_price) or "R" in mode):
                    final[(airport[0], airport[1], airport[2])] = (data[0]['price'], data[0]['distance'])
                print ("{:.2f}%".format(100 * i / len(from_airports)))
                i += 1
        return final

    def execute(self):
        if "C" not in self.param_mode:
            data = self.get_data(self.param_mode)
        else:
            data = {}
            data_r = self.get_data(self.param_mode[:1] + "R")
            data_d = self.get_data("D")
            data_a = self.get_data("A")
            for k, v in data_r.items():
                d = data_d.get(k)[0]
                a = data_a.get(k)[0]
                if d and a:
                    data[k] = "{:.4f}".format(v[0] / (d + a))
        return data
