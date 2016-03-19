class Movie:
    title = None
    poster_image_url = None
    trailer_youtube_url = None

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
