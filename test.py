import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

data = response.json()

print(data)

all_crafts = []
for person in data['people']:
    if person['craft'] not in all_crafts:
        all_crafts.append(person['craft'])

print("Many peole are currently in space")
print("All those in space are either on one fo the following ships:")
counter = 1
for craft in all_crafts:
    print(f"{counter} - {craft}")
    counter +=1
user_choice = input("Whih spacecraft are you interested in? (choose a number): ")
craft_chosen = all_crafts[int(user_choice) -1]

print(f"The current crew of the {craft_chosen} includes:")
for person in data['people']:
    if person['craft'] == craft_chosen:
        print(f" - {person['name']}")
# counter = 0
# for names in data['people']:
#     counter +=1
# print(counter)
