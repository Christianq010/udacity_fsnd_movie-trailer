import webbrowser


class Movie(object):
    """This Movie class provides a way to store our movie information/ format
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance method of Class must take self as argument
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)