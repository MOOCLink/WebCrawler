WebCrawler
==========

For crawler programs to get Coursera, EdX, and Udacity data

## Requirements
#### Python 2.7 with the following libraries:
* Scrapy
* Requests
* JSON

## Running the crawlers
#### Coursera
To collect data from Coursera, run:
`python coursera/scrape_coursera.py`

#### edX
To collect data from edX, navigate to the `edx/` directory and run:
`scrapy crawl edx`

#### Udacity
To collect data from Udacity, navigate to the `udacity/` directory and run:
`scrapy crawl udacity`
