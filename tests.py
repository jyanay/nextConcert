import pytest
from application import app
from models import ConcertEvent


# Tests for data models

def test_concert_event():
    event = ConcertEvent('Metallica', 'Metallica World Tour', '10/29/2022', 'The Staples Center', 'Los Angeles, USA')
    assert event.event_name == 'Metallica World Tour'
    assert event.band == 'Metallica'
    assert event.date == '10/29/2022'
    assert event.venue == 'The Staples Center'
    assert event.location == 'Los Angeles, USA'


# Tests for routes

def test_index():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data

'''
Would ideally test for what exactly it's responding in response.data, as well as test the post method and if expected results
are returned for both unfound artists and found artists, but.... Time.
'''