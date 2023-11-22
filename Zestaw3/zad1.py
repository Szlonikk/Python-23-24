import json

with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

trams = {}
for tram in data['tramwaje']:
    linia = int(tram['linia'])
    przystanki = tuple(stop['nazwa'].split()[0] for stop in tram['przystanek'])
    trams[linia] = przystanki

with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(trams, file, ensure_ascii=False)

sorted_trams = sorted(trams.items(), key=lambda x: len(x[1]), reverse=True)
for linia, przystanki in sorted_trams:
    print(f'Numer linii {linia} - Liczba przystanków: {len(przystanki)}')

common_stops = set.union(*(set(przystanki) for przystanki in trams.values()))

print(f'\nLiczba wszystkich przystanków obsługiwanych przez tramwaje: {len(common_stops)}')
