import time
class User:
    def __init__(self, nickname='', password='', age=0):
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
    current_user = User()
    users = []
    videos = []

    def log_in(self, nickname, password):
        for i in range(len(self.users) - 1):
            if self.users[i].nickmame == nickname and self.users[i].password == hash(password):
                self.current_user = self.users[i]
                print(f'Добро пожаловать {self.users[i].nickmame}')
            else:
                print('Логин или пароль неверны')

    def register(self, nickname, password, age):
        new_user = User(nickname, hash(password), age)
        if len(self.users) <= 1:
            self.users.append(new_user)
            self.current_user = new_user
            print(f'{self.current_user.nickname}, добро пожаловать!')
        else:
            for i in range(len(self.users) - 1):
                if nickname == self.users[i].nickname:
                    print(f'Пользователь {nickname} уже зарегистрирован')
                else:
                    self.users.append(new_user)
                    self.current_user = new_user
                    print(f'{self.current_user.nickname}, добро пожаловать!')

    def log_out(self):
        print(f'{self.current_user.nickname} вышел')
        self.current_user = User()


    def add(self, *args):
        for i in range(len(args)):
            if isinstance(args[i], Video):
                self.videos.append(args[i])

    def get_videos(self, search_video):
        res = ''
        for i in range(len(self.videos)):
            if search_video.lower() in self.videos[i].title.lower():
                res += f'{self.videos[i].title}\n'
        return res
    def watch_video(self, video_name):
        start = time.time()

        for i in range(len(self.videos) - 1):

            if video_name.lower() == self.videos[i].title.lower():
                print(f'Просмотр "{self.videos[i].title}"')
                if self.current_user.age < 18 and self.videos[i].adult_mode == True:
                    print(f'{self.current_user.nickname} Вам меньше 18 лет')
                else:
                    while int(time.time() - start) <= int(self.videos[i].duration):
                        print(int(time.time() - start), end=' ')
                        time.sleep(1)
                    print('\n')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2025 года', 200)

# Добавление видео
ur.add(v1, v2, v3)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.register('vasya_pupkin', 'lolkekcheburek', 15)

ur.watch_video('Для чего девушкам парень программист?')
ur.log_out()
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
