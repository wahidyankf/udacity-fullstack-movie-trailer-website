import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    # initiate the class, which takes 4 arguments:
    # movie title, poster image, youtube trailer, and story line
    def __init__(self, movie_title, poster_image, trailer_youtube, story_line):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.story_line = story_line

    # make a class method to show a trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

