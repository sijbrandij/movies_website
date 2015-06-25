class Movie():
    '''Create movie instances to use in movie website'''

    def __init__(self, title, storyline, image, trailer_youtube_url, rating, year):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = rating
        self.year = year
