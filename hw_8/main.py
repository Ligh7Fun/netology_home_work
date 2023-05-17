import requests

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
resp = requests.get(url)
data = resp.json()
super_hero_intelligence = {}

for super_hero in data:
    if super_hero["name"] in ['Hulk', 'Captain America', 'Thanos']:
        super_hero_intelligence[super_hero["name"]] = super_hero["powerstats"]["intelligence"]

print(f'Most intelligent Super Hero is {max(super_hero_intelligence)}')
