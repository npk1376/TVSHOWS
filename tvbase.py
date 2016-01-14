import website
import tvshow
# Create instances of the TvShow class, which was defined in the file tvshow.py
x_files = tvshow.TvShow("X-Files", "Two FBI agents investigate paranormal "
                        #title of the show, its storyline and cast
                        "activities and entertain conspiracy theories of the US"
                        " government.", "David Duchovny, Gillian Anderson",
                        #the url for the poster image
                        "https://www.movieposter.com/posters/archive/main/"
                        #the url for the trailer video on youtube
                        "100/MPW-50006", "https://www.youtube.com/watch?v=_"
                        "1SmJUBT5q0")
#the next 4 instances are created in the same manner
sherlock = tvshow.TvShow("Sherlock", "The new rendishion of the classical "
                         "stories. Sherlock Holmes of the 21st century.",
                         "Benedict Cumberbatch, Martin Freeman",
                         "http://img10.deviantart.net/faa7/i/2012/005/7/e/"
                         "sherlock_poster_by_vuel-d4leulr.jpg",
                         "https://www.youtube.com/watch?v=Nj7ZSUkTTVI")

the_fall = tvshow.TvShow("The Fall", "A 'why-done-it', not a 'who-done-it' "
                         "What makes the killer tick?",
                         "Gillian Anderson, Jamie Dornan",
                         "http://img11.deviantart.net/f79c/i/2013/161/c/8/the_"
                         "fall_dvd_artwork_by_jaimcferran-d68kj7x.jpg",
                         "https://www.youtube.com/watch?v=tP5Tl04gv3g")

criminal_minds = tvshow.TvShow("Criminal Minds", "BAU of the FBI catching "
                               "killers by getting into their brains. "
                               "Figuratively, of course!",
                               "Thomas Gibson, A.J. Cook, Matthew Gray Gubler",
                               "http://ecx.images-amazon.com/images/I/51zvTT3yA9"
                               "L.jpg","https://www.youtube.com/watch?v="
                               "VXAMRuG6W4I")

the_americans = tvshow.TvShow("The Americans", "The intricate spy games of the "
                              "KGB vs. CIA.", "Keri Russell, Matthew Rhys",
                              "http://stuffpoint.com/the-"
                              "americans/image/467394-the-americans-the"
                              "-americans-poster.jpg", "https://www.youtube.com"
                              "/watch?v=YGr75NZ5y34")

#put all the show into an array which will be passed as an argument to the
#function open_movies_page
tvShows = [x_files, sherlock, the_fall, criminal_minds, the_americans]
website.open_movies_page(tvShows)

