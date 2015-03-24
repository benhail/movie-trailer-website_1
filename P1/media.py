#
# media.py
# (c) 2015 Benhail Acosta - benhail.acosta@gmail.com

import webbrowser

class Movie () :
    """ Class Movie - provides with variables and methods to store and manage
    movie information

    Attributes:
        title: A string with the movie title
        story_line: A string with a plot description
        poster_image_url: A string with an URL to the movie poster
        trailer_youtube_url: A string with an URL to the movie video trailer
        director: A string with the director name
        rating: A string with the movie rating
        stars: A string with the name(s) of movie star(s)
        release_year: a string with movie release year
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
                 director, rating, stars, release_year):
        """
        Constructor for the Movie object. Initializes instance variables

        Args:
            movie_title:        string with the movie title
            movie_storyline:    string with short plot description
            poster_image:       URL pointing to JPG/GIF/PNG poster of movie
            trailer_youtube:    URL to a YouTube video with a trailer of movie
            director:           string with movie director info
            rating:             string with rating info
            stars:              string with names of strarring roles
            release_year:       string with year of release

        Return:
            no return. Just to initialize instance variables
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.rating = rating
        self.stars = stars
        self.release_year = release_year

    def show_trailer(self):
        """
        Using webbrowser module, open the trailer video in the
        instance variable trailer_youtube_url within a web browser
        """
        webbrowser.open(self.trailer_youtube_url)
