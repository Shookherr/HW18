from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_movies_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_movies_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_movies_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create_movie(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update_movie(self, data):
        movie = self.get_one(data.get('id'))
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        self.session.delete(self.get_one(mid))
        self.session.commit()
