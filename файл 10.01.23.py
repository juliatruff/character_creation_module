# Импортируем функцию стандартного модуля random.
from random import randint

# Вот она — новая глобальная константа.
DEFAULT_ATTACK = 5
# Новая константа — стандартное значение защиты.
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
# Вынесим диапазон очков урона в виде кортежа в константу
# Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
# Новая переменная класса — диапазон значения защиты.
    RANGE_VALUE_DEFENCE = (1, 5)
# Добавьте две новые константы для класса Character:
# Значение очков урона, для базового класса, оно будет равно 15.
    SPECIAL_BUFF = 15
# Название умения, значение — 'Удача';
    SPECIAL_SKILL = 'Удача'
# Объявляем конструктор класса.

    def __init__(self, name):
        self.name = name


# Объявляем метод атаки
# Вместо диапазона записана переменная класса.
# Оператор * распаковывает передаваемый кортеж.
    def attack(self):
        value_attack = 5 + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

# Объявляем метод защиты.
# Вычисляем значение защиты в переменной value_defence.
    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

# Объявляем метод специального умения.
# Здесь описано тело метода special().
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

# Новый метод базового класса.
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


# Далее описываем классы-наследники.
class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'

    warrior = Warrior('Кодослав')
    print(warrior)
    print(warrior.attack())
# Вывод в терминал:
# Warrior — дерзкий воин ближнего боя. Сильный, выносливый и отважный.
# Кодослав нанёс урон противнику, равный 8

    def choice_char_class() -> str:

       """
    Возвращает строку с выбранным
    классом персонажа.
    """
    approve_choice: str  = None
    char_class: str  = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class
