class Movie:
    def __init__(self, title, score, category):
        self.title = title
        self.score = score
        self.category = category

# Function 1
def is_above_5_5(movie):
    return movie.score > 5.5

# Function 2
def filter_above_5_5(movies):
    return [movie for movie in movies if is_above_5_5(movie)]

# Function 3
def filter_by_category(movies, category):
    return [movie for movie in movies if movie.category == category]

# Function 4
def average_score(movies):
    return sum(movie.score for movie in movies) / len(movies) if movies else 0

# Function 5
def average_score_by_category(movies, category):
    category_movies = filter_by_category(movies, category)
    return average_score(category_movies)