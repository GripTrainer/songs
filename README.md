# songs
Natural Language Processing of Song Data

### Getting Started
```
pip install requirements.txt
```

### Run Spider to fetch songs
```
scrapy crawl songs -o {outputdir}
```

### Change artist to scrape 

- Go to `songs/spiders/songs.py` 
- Add url to your artist in metrolyrics in `start_urls` 

### Medium Article
- https://medium.com/@lukebfalvey/the-natural-language-of-songs-1453e40ec120