import requests


main_ref = 'https://superheroapi.com/api/2619421814940190/search/'
superheros_names = [
    'Hulk',
    'Captain_America',
    'Thanos'
]
max_intelligence = -1
superhero_name = ''
for name in superheros_names:
    superhero_info = requests.get(f'{main_ref}{name}').json()
    superhero_intelligence = int(superhero_info['results'][0]['powerstats']['intelligence'])
    if max_intelligence < superhero_intelligence:
        max_intelligence = superhero_intelligence
        superhero_name = name
print(superhero_name)
