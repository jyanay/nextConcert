from typing import List
import requests
from bs4 import BeautifulSoup
import json
from models import ConcertEvent

# We will be scraping songkick.com for concert dates
# Setting up URL and params
SONGKICK_SEARCH_URL = 'https://www.songkick.com/search?page=1&per_page=10&query='
SONGKICK_PARAMS = '&type=artists'
SONGKICK_URL = 'https://www.songkick.com'
client = requests.Session()


def getArtistUrl(band: str) -> str:
    # Returns a string of the URL needed to get the concert list

    # Setup and execute search query using requests
    search_query = f'{SONGKICK_SEARCH_URL}{band}{SONGKICK_PARAMS}'
    response = client.get(search_query)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')

        # We'll rely on songkicks search to provide the best match first
        # Could be improved by using regex to check all results
        artist_url = soup.find('li', class_='artist').findChild('a').attrs.get('href')
        return artist_url


def getNextConcerts(artist_url: str) -> List[str]:
    # Returns a list of all upcoming concerts for the artist

    # Setup and execute request to scrape concerts
    url = f'{SONGKICK_URL}{artist_url}'
    response = client.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    # Extract event list from soup, and return AttributeError if none are found
    try:
        event_list = soup.find('div', id='calendar-summary').find_all('li', class_='event-listing')
    except AttributeError:
        return AttributeError


    # Lucky us, they've got json on the page
    # Loop through events and extract data for each one from the hidden script tag with json
    concert_list = []
    for concert in event_list:
        data = json.loads(concert.find('script').string)
        title = data[0]['name']
        location_name = data[0]['location']['name']
        city = data[0]['location']['address']['addressLocality']
        country = data[0]['location']['address']['addressCountry']
        location = f'{city}, {country}'
        date = data[0]['startDate']
        band = data[0]['performer'][0]['name']
        # Append ConcertEvent objects to concert_list
        result = ConcertEvent(band, title, date, location_name, location)
        concert_list.append(result)

    return concert_list


if __name__ == '__main__':
    import sys
    artist = []
    for i in range(1, len(sys.argv)):
        artist.append(sys.argv[i])
    artist = ' '.join(artist)
    url = getArtistUrl(artist)
    result = getNextConcerts(url)
    if result == AttributeError:
        print(f'Sorry, unable to find any upcoming concerts for {artist}. Please try another artist.')
    else:
        print(result.pop(0))



