import requests
choice = input("Do you want song recommendations from an artist or the lyrics for a specific song? (a/s): ")
#suggestions
if choice == 'a':
    artist = input("Which artist would you like to find a song from? ")
    suggestion = requests.get(f'https://api.lyrics.ovh/suggest/{artist}')
    suggestion = suggestion.json()
    print(suggestion)
    for track in suggestion['data']:
        print(f"{track['title']} by {track['artist']}")

#lyric finder oooo
elif choice == 's':
    artist = input("What artist do you want to find a song from? ")
    song = input("What song do you want the lyrics for? ")
    lyrics = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song}")
    lyrics = lyrics.json()
    if 'lyrics' not in lyrics:
        print('Error - could not find lyrics')
    else:
        print(f"The lyrics for {song} by {artist} are:")
        print(lyrics['lyrics'])

