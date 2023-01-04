# Здесь бизнес логика, в виде классов или методов. Сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, keys_list):
        if keys_list.get('did') is not None:
            return self.dao.get_movies_by_director(keys_list['did'])
        if keys_list.get('gid') is not None:
            return self.dao.get_movies_by_genre(keys_list['gid'])
        if keys_list.get('year') is not None:
            return self.dao.get_movies_by_year(keys_list['year'])
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create_movie(data)

    def update(self, data):
        return self.dao.update_movie(data)

    def delete(self, mid):
        self.dao.delete(mid)
