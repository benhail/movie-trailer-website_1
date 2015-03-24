#
# fresh_tomatoes.py
# Creates the HTML page for the Movie Trailer Website
#
# (c) 2015 Benhail Acosta - benhail.acosta@gmail.com

import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''

<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes with deep cooking...!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        /* Red */
$bgDefault      : #e74c3c;
$bgHighlight    : #c0392b;
$colDefault     : #ecf0f1;
$colHover       : #ffbbbc;
        /* --- Style --- */
.navbar-default {
    background-color: $bgDefault;
    border-color: $bgHighlight;
    .navbar-brand {
        color: $colDefault;
        &:hover, &:focus {
            color: $colHover; }}
    .navbar-nav {
        > li {
            > a {
                color: $colDefault;
                &:hover, &:focus {
                    color: $colHover;   }}}
        .active {
            > a, > a:hover, > a:focus {
                color: $colHover;
                background-color: $bgHighlight; }}
        .open {
            > a, > a:hover, > a:focus {
                color: $colHover;
                background-color: $bgHighlight;
                .caret {
                    border-top-color: $colHover;
                    border-bottom-color: $colHover; }}}
        > .dropdown {
            > a {
                .caret {
                    border-top-color: $colDefault;
                    border-bottom-color: $colDefault; }
                &:hover, &:focus {
                    .caret {
                        border-top-color: $colHover;
                        border-bottom-color: $colHover; }}}}}
    .navbar-toggle {
        border-color: $bgHighlight;
        &:hover, &:focus {
            background-color: $bgHighlight; }
        .icon-bar {
            background-color: $colDefault; }}}
@media (max-width: 767px) {
    .navbar-default .navbar-nav .open .dropdown-menu > li > a {
        color: $colDefault;
        &:hover, &:focus {
            color: $colHover;
            background-color: $bgHighlight; }}
}

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>

    <script>
    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });

    // Start playing the video whenever the trailer modal is opened
    $(document).on('click', '.movie-button-play', function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
          'id': 'trailer-video',
          'type': 'text-html',
          'src': sourceUrl,
          'frameborder': 0
        }));
    });

    // Animate in the movies when the page loads
    $(document).ready(function () {
      $('.movie-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
      });
    });

    // modals handling
      function launch_modal(id) {
     // Hide all modals using class if required.
     $('.modal').modal('hide');
     $('#'+id).modal('show');
  }

    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>

<!-- Movie player modal -->
  <div class="modal" id="trailer">
    <div class="modal-dialog">
      <div class="modal-content">
        <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
          <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
        </a>
        <div class="scale-media" id="trailer-video-container">
        </div>

      </div>
    </div>
  </div>

<!-- Page top -->
<!-- Main Page Content -->
<div class="container">
  <div class="navbar navbar-header navbar-fixed-top" role="navigation">
    <div class="container">
      <div class="navbar-header">
        <a class="navbar-brand" href="#">ALL NEW! Fresh Tomatoes Movie Trailers - </a>
      </div>
    </div>
  </div>
</div>
<div class="container">
      {movie_tiles}
</div>
  </body>
</html>
'''

# The page tile HTML code which is populated and completed
# in the create_movie_tiles_content method and placed on
# {movie_tiles} tag on the main_page_content variable
movie_tile_content = '''
<div class="col-md-6 col-lg-4 text-center" data-toggle="modal">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal{k}">
      <span class="glyphicon glyphicon-paperclip"></span> More details!
    </button>
    <button type="button" class="btn btn-primary movie-button-play"
    data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
      <span class="glyphicon glyphicon-film"></span> Play Trailer
    </button>
    <p></p><p/><p/>
</div>

<!-- Movie information Modal -->
<div class="modal fade" id="myModal{k}" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">{movie_title}</h4>
      </div>
      <div class="modal-body">
        <h4>Plot</h4>
        <p>{movie_story}</p>
        <h4>Release year</h4>
        <p> {movie_year}</p>
        <h4>Starring</h4>
        <p>{movie_stars}</p>
        <h4>Director</h4>
        <p>{movie_director}</p>
      </div>
    </div>
    </div>
</div>
'''



def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    kount = 1
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', \
            movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_story=movie.storyline,
            movie_director=movie.director,
            movie_rating=movie.rating,
            movie_stars=movie.stars,
            movie_year=movie.release_year,
            k=kount
        )
        kount += 1

    return content

def open_movies_page(movies):
    """
    Creates the movie site HTML and launches it in the browser

    Args:
        movies: a list of Movie type objects

    Receives the Movie object lists and creates the fresh_tomatoes.html file
    """

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically
    # generated content
    rendered_content = main_page_content.format( \
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
