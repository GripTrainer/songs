import re
import scrapy

class SongSpider(scrapy.Spider):
    name = 'songs'
    start_urls = [
        'http://www.metrolyrics.com/ed-sheeran-lyrics.html',
        'http://www.metrolyrics.com/jay-z-lyrics.html',
        'http://www.metrolyrics.com/taylor-swift-lyrics.html',
        'http://www.metrolyrics.com/jonas-brothers-lyrics.html',
        'http://www.metrolyrics.com/2pac-lyrics.html',
        'http://www.metrolyrics.com/kanye-west-lyrics.html',
        'http://www.metrolyrics.com/red-hot-chili-peppers-lyrics.html'
    ]

    def parse(self, response):
        for song in response.css('.switchable a.title.hasvidtable'):
            yield response.follow(song, callback=self.parse_song)

        for page in response.css('.pagination a'):
            yield response.follow(page)
    
    def parse_song(self, response):
        verses = response.css('.verse::text').extract()
        lyrics = ' '.join(verses)
        clean_lyrics = lyrics.replace('\n', '')
        artist = re.search('"musicArtistName":"([^"]+)"', response.text)[1]
        song = re.search('"musicSongTitle":"([^"]+)"', response.text)[1]
        yield {
            'artist': artist,
            'song': song,
            'lyrics': clean_lyrics
        }


    