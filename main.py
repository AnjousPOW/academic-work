"""
   Тема: музыкальный поратл для хранения и прослушивания музыки.
   Описание:
          1) база данных:
             1.1) база данных пользователей (те кто зарегестрировался);
             1.2) база данных плейлистов;

          2) Функционал:
             2.1) Регистрация пользователя (для возможности добовления аудио и создания плейлистов) [+\-];
             2.2) Загрузка аудио и создание плейлистов и авотарок к ним [+\-];
                 2.2.1) Сохрание плейлистов для меню конкретного пользователя [+\-];
                 2.2.2) Редактирование созданного плейлиста (только тому пользователю кто его создал) [+\-];
             2.3) Сборка рейтинга оценок для плейлистов и аудиозаписей [+\-];
             2.4) Возможность прослушивания через телеграмм бот для зарегестрированых пользователей [+\-];

"""


class User:
    """Хранит данные пользователя"""

    def __init__(self, name, password):
        self.name = name
        self.password = password


class Playlist():
    """Хранит информацию о плейлисте"""

    def check_user(self):
        """Зарегестрирован ли пользователь"""
        if Login == True:
            pass

    def save_user(self):
        """кто из пользователей его сохранил"""
        pass

    def create_user(self):
        """кто из пользователей его создал"""
        pass

    def list_length(self):
        """Установлен максимальный размер плейлиста и недапуск превышение лимита"""
        pass

    def create_rating(self):
        """Предостовляет рейтинг плейлисту"""
        pass

    def user_save(self):
        """пользователи которые сохранили плейлист"""
        pass

    def __init__(self, listname, rating, length, create_user, save_user):
        self.listname = listname
        self.rating = rating
        self.length = length
        self.create_user = create_user
        self.save_user = save_user


class audio:
    """Хранит информацию о аудиозаписи: название, исполнитель, жанр"""
    def __init__(self, title, executor, genre):
        """название"""
        self.title = title
        """исполнитель"""
        self.executor = executor
        """жанр"""
        self.genge = genre


class Register(User):
    """Регистрация пользователя"""

    def register_user(self):
        pass


class Login(User):
    """Система логина"""

    def login_user(self):
        pass

