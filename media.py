import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    # make a class method to show a trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
