# Дополнительное практическое задание по модулю: "Классы и объекты"
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname        # имя пользователя
        self.password = hash(password)  # хэш пароля
        self.age = age                  # возраст

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title              # заголовок
        self.duration = duration        # продолжительность
        self.time_now = time_now        # секунда остановки
        self.adult_mode = adult_mode    # ограничение по возрасту


class UrTube:
    users = []                          # список пользователей
    videos = []                         # список видео
    current_user = None                 # текущий пользователь

    # Поиск пользователя в списке по имени
    # Если пользователь найден и пароль верный, то current_user меняется на найденного
    def log_in(self, nickname, password):
        user = self.__get_instance('users', 'nickname', nickname)
        if user is not None:
            if user.password == hash(password):
                self.current_user = user
            else:
                print('Неверный пароль')
        else:
            print(f'Пользователь {nickname} не найден')

    # Добавление пользователя в список, если пользователя с таким же именем ещё не существует
    # После регистрации вход выполняется автоматически
    def register(self, nickname, password, age):
        if self.__get_instance('users', 'nickname', nickname) is None:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    # Сброс текущего пользователя
    def log_out(self):
        self.current_user = None

    # Добавление неограниченного кол-ва видео в список, если видео с таким же названием ещё не существует
    def add(self, *videos):
        for video in videos:
            if self.__get_instance('videos', 'title', video.title) is None:
                self.videos.append(video)

    # Поиск названий всех видео в списке, содержащих поисковое слово без учета регистра
    def get_videos(self, search_string):
        return [video.title for video in self.videos if video.title.lower().__contains__(search_string.lower())]

    # Поиск видео в списке по названию
    # Если видео найдено, то ведётся отчёт секунд просмотра
    # После окончания текущее время просмотра данного видео сбрасывается
    def watch_video(self, title):
        if self.current_user is not None:
            video = self.__get_instance('videos', 'title', title)
            if video is not None:
                if video.adult_mode and self.current_user.age > 18:
                    for sec in range(video.time_now, video.duration):
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        time.sleep(1)
                    video.time_now = 0
                    print('Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    # Универсальный поиск
    def __get_instance(self, list_, attribute, value):
        return next((instance for instance in self.__getattribute__(list_)
                     if instance.__getattribute__(attribute) == value), None)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
