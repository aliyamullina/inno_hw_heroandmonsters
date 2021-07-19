import random
import sys
from typing import Tuple

# Счетчик поверженных героем чудовищ:
monster_counter = 0

# Текущее состояние здоровье героя:
hp = 10

# Текущая сила удара героя:
attack = 10


def game() -> None:
    """Главная функция, запустив которую начнется игра."""
    print('Текстовая игра "Герой и чудовища".')
    hero_hp = hp
    hero_attack = attack
    m_counter = monster_counter
    win_count = 10
    print(
        "Ты — рыцарь в фантастической стране. Задача — победить",
        win_count,
        "чудовищ, чтобы спасти королевство от " "нападения и тем самым выиграть игру!",
    )
    while m_counter < win_count:
        # Рандомно вывести события из monsters(), swords(), apples()
        events = [monsters, apples, swords]
        current_event = random.choice(random.choices(events, weights=[0.3, 0.6, 0.1]))

        if current_event == apples:
            hero_hp = apples(hero_hp)
        elif current_event == swords:
            hero_attack = swords(hero_attack)
        else:
            hero_hp, hero_attack, m_counter = monsters(hero_hp, hero_attack, m_counter)
            print("Твой счет", m_counter, "из", win_count)

        if m_counter == win_count:
            print("ПОБЕДА")
            sys.exit()

        if hero_hp == 0:
            print("ПОРАЖЕНИЕ")
            sys.exit()


def monsters(x: int, y: int, z: int) -> Tuple[int, int, int]:
    """Монстры.

    :param x: жизнь героя
    :param y: сила атаки героя
    :param z: число атакованных монстров
    :return: x, y, z
    :rtype: int
    """
    # Количество жизней чудовищ
    monster_hp = random.randint(1, 10)

    # Силы атаки чудовищ
    monster_attack = random.randint(1, 10)

    # Сражение с чудовищем:
    print(
        "На горизонте чудовище с",
        monster_hp,
        "жизнями и с силой атаки",
        monster_attack,
        "У тебя жизнь:",
        x,
        "и сила атаки:",
        y,
    )

    # Действия
    print("БОЙ! 1 - сражаться, 2 - убежать, чтобы набраться сил")
    answer = getInput()
    if answer in "1":
        print("СРАЖЕНИЕ!")
        if y >= monster_hp and x > monster_attack:
            x = x - monster_attack
            z = z + 1
            print("УСПЕХ! В бою твоя жизнь сократилась до", x)
            return x, y, z
        else:
            x = 0
            return x, y, z
    else:
        print("Фух! Удалось убежать!")
        return x, y, z


def swords(x: int) -> int:
    """Мечи.

    :return: x
    :rtype: int
    :type x: int
    """
    # Силы атаки мечей
    sword_attack = random.randint(11, 15)

    # Действия
    print(
        "Найден МЕЧ с силой атаки",
        sword_attack,
        "Старый",
        x,
        "1 - взять себе, 2 - пройти мимо",
    )
    answer = getInput()
    if answer in "1":
        x = sword_attack
        print("Новая сила атаки:", x)
        return x
    else:
        print("Проходишь мимо...")
        return x


def apples(x: int) -> int:
    """Яблочки.

    :return: x
    :rtype: int
    :type x: int
    """
    apple_hp = random.randint(3, 5)
    x = x + apple_hp
    print("ЯБЛОЧКО! Количество жизней увеличилось на", apple_hp, "и равно", x)
    return x


def getInput() -> str:
    """Ввод игрока.

    :return: answer
    :rtype: str
    """
    print("Введи цифру 1 или 2")
    while True:
        answer = input()
        if answer in ("1", "2"):
            return answer
        print("Действие не распознано. Введи еще раз 1 или 2")


if __name__ == "__main__":
    game()
