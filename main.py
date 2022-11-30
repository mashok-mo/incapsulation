class Character:
    def __init__(self, x, y, health, name):
        self.__x = x
        self.__y = y
        self.__health = health
        self.__name = name

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def health(self):
        return self.__health
    @property
    def name(self):
        return self.__name

    @health.setter
    def health(self, health):
        if 0 < health <= 100:
            self.__health = health
        else:
            print("Неверное значение здоровья")

    def move(self, direction, distance):
        if direction == '1':
            self.__y += distance
        elif direction == '2':
            self.__x += distance
        elif direction == '3':
            self.__y -= distance
        elif direction == '4':
            self.__x -= distance
        else:
            return('Неверная команда')

    def display_info(self):
        return (f'Персонаж {self.name} переместился в точку {self.x, self.y}, здоровье {self.health}')

def main():
    name = input('Введите имя игрока: ')
    health = int(input('Введите здоровье игрока: '))
    print('Введите координаты игрока')
    x = int(input('x: '))
    y = int(input('y: '))
    character = Character(x,y, 0, name)
    character.health = health
    while character.health == 0:
        health = int(input('Введите здоровье игрока: '))
        character.health = health
    while True:
        stop = input('Хотите передвинуть персонажа? да/нет ')
        if stop == 'да':
            direction = input('Введите направление движения:\n1 - вверх, 2 - вправо, 3 - вниз, 4 - влево\n')
            distance = int(input('Введите расстояние: '))
            character.move(direction, distance)
            print(character.display_info())
        elif stop == 'нет':
            break
        else:
            print('Неверная команда')

main()