# Web Scraping

This Repository is used for learning web scraping by python

## Dependencies
- python3.7+
- python scrapy

## Scrapers

### Whisky Scraper

Whisky scraper is located in `whiskyscraper` directory.
The scraper collects data from [whiskyshop](www.whiskyshop.com) and saves it in a file.

Usage:

`cd whiskyscraper`
Save into a json: `scrapy crawl whisky -O whisky.json`
Save into a csv: `scrapy crawl whisky -O whisky.csv`
