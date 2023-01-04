from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')

        keys_list = {
            'did': director,
            'gid': genre,
            'year': year
        }

        movies = movie_service.get_all(keys_list)

        ret_val = MovieSchema(many=True).dump(movies)
        return ret_val, 200

    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return '', 201, {"location": f'/movies/{movie.id}'}


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return MovieSchema().dump(movie), 200

    def put(self, mid):
        req_json = request.json
        if 'id' not in req_json:
            req_json['id'] = mid
        movie_service.update(req_json)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
