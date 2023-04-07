from exam_python_OOP_10_april_2022.project import Movie
from exam_python_OOP_10_april_2022.project import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if username in [user.username for user in self.users_collection]:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if username not in [user.username for user in self.users_collection]:
            raise Exception("This user does not exist!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie.title in [movie.title for movie in self.movies_collection]:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        movie.owner.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        movie_title = movie.title
        if movie_title not in [movie.title for movie in self.movies_collection]:
            raise Exception(f"The movie {movie_title} is not uploaded!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie_title}!")

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        movie_title = movie.title
        if movie_title not in [movie.title for movie in self.movies_collection]:
            raise Exception(f"The movie {movie_title} is not uploaded!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie_title}!")

        self.movies_collection.remove(movie)
        movie.owner.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie_title} movie."

    def like_movie(self, username: str, movie: Movie):
        movie_title = movie.title
        user = [user for user in self.users_collection if user.username == username][0]
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie_title}!")

        if movie_title in [m.title for m in user.movies_liked]:
            raise Exception(f"{username} already liked the movie {movie_title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie_title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        movie_title = movie.title
        user = [user for user in self.users_collection if user.username == username][0]

        if movie_title not in [movie.title for movie in user.movies_liked]:
            raise Exception(f"{username} has not liked the movie {movie_title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1

        return f"{username} disliked {movie_title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        ordered_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        result = ''
        for movie in ordered_movies:
            if movie == ordered_movies[0]:
                result += movie.details()
            else:
                result += f"\n{movie.details()}"

        return result

    def __str__(self):
        result = ''

        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            result += f"All users: {', '.join([user.username for user in self.users_collection])}\n"

        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join([movie.title for movie in self.movies_collection])}"

        return result
