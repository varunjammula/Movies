class Movie:
    """
    Movie class that has 3 members, namely title of the movie, movie poster URL
    and Youtube link for movie trailer
    """
    title = None
    poster_image_url = None
    trailer_youtube_url = None

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """

        :param title: Title of the movie
        :param poster_image_url: Movie poster image URL
        :param trailer_youtube_url: Youtube link for movie trailer
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url