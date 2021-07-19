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
    hero_hp = hp
    hero_attack = attack
    m_counter = monster_counter
    win_count = 10
    print(
        f"Ты — рыцарь в фантастической стране. Задача — одолеть ",
        str(win_count),
        " чудовищ, чтобы спасти королевство от нападения!",
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
            print(f"Твой счет ", str(m_counter), " из ", str(win_count))

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
        f"На горизонте чудовище с ",
        str(monster_hp),
        " жизнями и с силой атаки ",
        str(monster_attack),
        ". У тебя жизнь: ",
        str(x),
        " и сила атаки: ",
        str(y),
    )

    # Действия
    print("БОЙ! 1 - сражаться, 2 - убежать, чтобы набраться сил")
    answer = get_input()
    if answer in "1":
        print("СРАЖЕНИЕ!")
        if y >= monster_hp and x > monster_attack:
            x = x - monster_attack
            z = z + 1
            print(f"УСПЕХ! В бою твоя жизнь сократилась до ", str(x))
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
        f"Найден МЕЧ с силой атаки ",
        str(sword_attack),
        "Старый ",
        str(x),
        ". 1 - взять себе, 2 - пройти мимо",
    )
    answer = get_input()
    if answer in "1":
        x = sword_attack
        print(f"Новая сила атаки: ", str(x))
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
    print(f"ЯБЛОЧКО! Количество жизней увеличилось на ", str(apple_hp), " и равно ", str(x))
    return x


def get_input() -> str:
    """Ввод игрока.

    :return: answer
    :rtype: str
    """
    while True:
        answer = input()
        if answer in ("1", "2"):
            return answer
        print("Действие не распознано. Введи еще раз 1 или 2")


if __name__ == "__main__":
    game()
