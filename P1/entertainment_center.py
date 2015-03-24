#
# entertainment_center.py
# Creates the Movie objects for the Movie Trailer Website and
# using fresh_tomatoes module as helper construct the HTML needed
# to launch website
#
# (c) 2015 Benhail Acosta - benhail.acosta@gmail.com

import media
import fresh_tomatoes

""" Create each movie object """
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc&spfreload=10",
    "John Lasseter",
    "G",
    "Tom Hanks (Woody), Tim Allen (Buzz Lightyear)",
    "1995")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8&spfreload=10",
    "James Cameron",
    "PG-13",
    "Sam Worthington, Zoe Saldana, Sigourney Weaver",
    "2009")

fight_club = media.Movie(
    "Fight Club",
    "An unnamed guy creates a fight club with a soap maker",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg&spfreload=10",
    "David Fincher",
    "R",
    "Brad Pitt, Edward Norton, Helena Bonham Carter",
    "1999")

school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc&spfreload=10",
    "Richard Linklater",
    "PG-13",
    "Jack Black, Mike White, Joan Cusack",
    "2003")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat is a chef in Paris",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk&spfreload=10",
    "Brad Bird, Jan Pinkava",
    "G",
    "Brad Garrett, Lou Romano, Patton Oswalt",
    "2007")

star_wars_episode_three = media.Movie(
    "Star Wars: Episode III",
    "Sith Lord Darth Sidious steps out of the shadows, at which time Anakin"\
    " succumbs to his emotions",
    "https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_"\
    "Revenge_of_the_Sith_poster.jpg",
    "https://www.youtube.com/watch?v=WHSU3KSK8dw&spfreload=10",
    "George Lucas",
    "PG-13",
    "Hayden Christensen, Natalie Portman, Ewan McGregor",
    "2005")

big_fish = media.Movie(
    "Big Fish",
    "A son tries to learn more about his dying father by reliving stories"\
    " and myths he told about his life.",
    "https://upload.wikimedia.org/wikipedia/en/3/35/Big-fish-movie-poster.jpg",
    "https://www.youtube.com/watch?v=lfW8qaJL1Fs&spfreload=10",
    "Tim Burton",
    "PG-13",
    "Ewan McGregor, Albert Finney, Billy Crudup",
    "2003")

""" Construct Movie objects list """
movies = [toy_story, avatar, fight_club, school_of_rock, ratatouille, \
    star_wars_episode_three, big_fish]

""" pass Movie objects list to create and launch web site
    using fresh_tomatoes module 'open_movies_page' method
"""
fresh_tomatoes.open_movies_page(movies)
