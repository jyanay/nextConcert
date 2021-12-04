class ConcertEvent:
    def __init__(self, band, event_name, date, venue, location):
        self.band = band
        self.event_name = event_name
        self.date = date
        self.location = location
        self.venue = venue

    def __repr__(self):
        return f'{self.event_name} @ {self.venue} on {self.date} in {self.location}'

    def __str__(self):
        return f'{self.event_name} @ {self.venue} on {self.date} in {self.location}'
