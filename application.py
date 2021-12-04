from flask import Flask, render_template, request
from scraper import getArtistUrl, getNextConcerts

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def next_concert():
    if request.method == 'POST':
        artist_url = getArtistUrl(request.form.get('artist'))
        result = getNextConcerts(artist_url)
        if result == AttributeError:
            return render_template('results.html', not_found=result, artist=request.form.get('artist'))
        return render_template('results.html', result=result, artist=request.form.get('artist'))
    return render_template('index.html')


if __name__ == '__main__':
    application.run()
