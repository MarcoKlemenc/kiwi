import sys
from search import Search

param_mode = sys.argv[1]
param_code = sys.argv[2]
max_price = sys.argv[3]
max_stopovers = sys.argv[4]

def get_data(mode):
    from_airports = []
    final = {}
    req = Search(param_code, None, '01/07/2018', '31/12/2018', "R" in mode, max_price, max_stopovers)
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
            req = Search(airport[0], param_code, '01/07/2018', '31/12/2018', "R" in mode, None, max_stopovers)
            data = req.get()
            if data and (data[0]['price'] <= int(max_price) or "R" in mode):
                final[(airport[0], airport[1], airport[2])] = (data[0]['price'], data[0]['distance'])
            print ("{:.2f}%".format(100 * i / len(from_airports)))
            i += 1
    return final

if "C" not in param_mode:
    data = get_data(param_mode)
else:
    data = {}
    data_r = get_data(param_mode[:1] + "R")
    data_d = get_data("D")
    data_a = get_data("A")
    for k, v in data_r.items():
        d = data_d.get(k)[0]
        a = data_a.get(k)[0]
        if d and a:
            data[k] = "{:.4f}".format(v[0] / (d + a))

with open('{} {} {} {}.txt'.format(param_mode, param_code, max_price, max_stopovers), 'w', encoding='utf-8') as f:
    for k, v in data.items():
        f.write("{}\t{}\t{}\t{}, {}\n".format(k[0], v[0], int(v[1]), k[1], k[2]))
