import fresh_tomatoes
import media

titanic = media.Movie(
    "Titanic",
    """A seventeen-year-old aristocrat falls in love with a kind, but poor
    artist aboard the luxuriousm ill-fated R.M.S. Titanic.""",
    "http://ia.media-imdb.com/images/M/MV5BMjExNzM0NDM0N15BMl5BanBnXkFtZTcwMzkxOTUwNw@@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0",
    'PG-13',
    '1997'
)

school_of_rock = media.Movie(
    "School of Rock",
    """When struggling musician Dewey Finn finds himself out of work, he
    takes over his roommate's job as an elementary school substitute teacher
    and turns class into a rock band.""",
    "http://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_SX214_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=5afGGGsxvEA",
    'PG_13',
    '2003'
)

moulin_rouge = media.Movie(
    "Moulin Rouge",
    """A poet falls for a beautiful courtesan whom a jealous duke covets in this
    stylish musical, with music drawn from familiar 20th century sources""",
    "http://ia.media-imdb.com/images/M/MV5BMTk5Mjg0MzM3MV5BMl5BanBnXkFtZTcwMTEyMjcxMQ@@._V1_SY317_CR2,0,214,317_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=dtEgAx80NC4",
    "PG-13",
    "2001"
)

ice_age = media.Movie(
    "Ice Age",
    """Set during the Ice Age, a sabertooth tiger, a sloth, and a woolly mammoth
    find a lost human infant, and they try to return him to his tribe""",
    "http://ia.media-imdb.com/images/M/MV5BMjEyNzI1ODA0MF5BMl5BanBnXkFtZTYwODIxODY3._V1_SX214_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=cMfeWyVBidk",
    "PG",
    "2002"
)

shrek = media.Movie(
    "Shrek",
    """After his swamp is filled with magical creatures, an ogre agrees to rescue
    a princess for a villainous lord in order to get his land back.""",
    "http://ia.media-imdb.com/images/M/MV5BMTk2NTE1NTE0M15BMl5BanBnXkFtZTgwNjY4NTYxMTE@._V1_SX214_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=ooJJX3R42WM",
    "PG",
    "2001"
)

# Create list of favorite movies
movies = [titanic, school_of_rock, moulin_rouge, ice_age, shrek]

# Create movies page
fresh_tomatoes.open_movies_page(movies)
