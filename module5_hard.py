from time import sleep, time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    time_now = 0

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode


class UrTube:
    current_user = ''
    users = {}
    videos = []
    age = None

    # def __init__(self):
    #     self.users = {}
    #     self.videos = {}

    def log_in(self, nickname, password):
        for user in self.users.keys():
            if user == nickname and password == self.users[nickname]:
                self.current_user = nickname
                print(f'Добро пожаловать {nickname}')
            else:
                print('Логин или пароль неверны')

    def register(self, nickname, password, age):
        # self.users[nickname]=password
        self.age = age
        for nick in self.users.keys():
            if nickname == nick:
                print('Пользователь уже зарегистрирован')
            else:
                self.users.update({nickname: password})
                self.current_user = nickname

    def log_out(self):
        self.current_user = ''

    def add(self, *args):
        for i in range(len(args)):
            if isinstance(args[i], Video):
                self.videos.append(args[i])

    def get_videos(self, search_video):
        for i in range(len(self.videos)):
            if search_video.lower() in self.videos[i].lower():
                print(self.videos[i])

    def watch_video(self, video_name):
        start = time.time()
        end = 0
        for i in range(len(self.videos)):
            if video_name.lower() == self.videos[i].lower():
                video_name = self.videos[i]
                print(f'Просмотр {video_name}')
            else:
                break
            continue
        while time.time() < self.videos[i].duration:


if __name__ == '__main__':
    stream = UrTube()
    stream.register(input('Логин: '), input('Пароль: '), input('Возраст: '))

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

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
