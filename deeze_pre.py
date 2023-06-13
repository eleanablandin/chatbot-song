import requests

def get_data():
    url = 'https://api.deezer.com/chart'
    response = requests.get(url)
    data = response.json()
    songs = data['tracks']['data']
    return songs

def process_songs(songs):
    text = ''
    for song in songs:
        title = song['title']
        artist = song['artist']['name']
        text += title + ' ' + artist + ' '
    
    text = text.lower()
    unique_characteres = sorted(list(set(text)))
    
    #characteres to indices
    char_to_ind = {char:ind for ind, char in enumerate(unique_characteres)}

    #indices to characteres
    ind_to_char = {ind:char for ind, char in enumerate(unique_characteres)}

    return text, char_to_ind, ind_to_char

process_data = process_songs(get_data())


