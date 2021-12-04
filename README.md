## nextConcert README
### Usage
Along with a flask based webserver, you can also run the script via the command-line.


From the project folder, simply run: python3 scraper.py YOUR BAND HERE

### Thoughts
For something like this, you'd probably want to rotate proxies with each
request to avoid being blocked/limited.

To improve performance, you could store the results in something like redis
and flush them regularly. Checking if a band exists in the cache before making a request.

Ideally, if it couldn't find an upcoming concert for an artist via one page/api, we'd have
a list of multiple sources that it could iterate through to provide better results.

