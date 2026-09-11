import requests


artist = input("Which artist would you like to find a song from? ")
# song = input("What song would you like to see the lyrics for? ")

suggestion = requests.get(f'https://api.lyrics.ovh/suggest/{artist}')
suggestion = suggestion.json()
print(suggestion)
for track in suggestion['data']:
    print(track['title'])
# lyrics = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song}")
# lyrics = lyrics.json()
#making sure the first half of the lyrics thing doesnt print along with the error
# if 'lyrics' not in lyrics:
#     print('Error - could not find lyrics')
# else:
#     print(f"The lyrics for {song} by {artist} are:")
#     print(lyrics['lyrics'])

