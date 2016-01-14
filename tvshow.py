import webbrowser

class TvShow():
 
    def __init__(self, show_title, show_storyline, starring,
                 poster_image, trailer_youtube):
        self.title = show_title
        self.storyline = show_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.starring = starring

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
