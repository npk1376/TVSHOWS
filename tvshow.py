# this call will prompt Python to open the module 'webbrowser' on
# the users's computer for the dynamic webpage
import webbrowser

# defining a class, which will have a few paremeters, such as
# title, storyline, cast, etc.
# the first parameter - 'self' will refer to each of the instances
# (objects) of this class. Those instances are created in
# another file.
class TvShow():
 
    def __init__(self, show_title, show_storyline, starring,
                 poster_image, trailer_youtube):
        self.title = show_title
        self.storyline = show_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.starring = starring
 # defining a function, called 'show_trailer', passing it the 
 # parameter 'self'. The function users Python's built-in function
 # 'open' inside the module 'webbrowser' and gets the appropriate
 # parameter 'trailer_youtube_url' for the appropriate 'self'-item.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
