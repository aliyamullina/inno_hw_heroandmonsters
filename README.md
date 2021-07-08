# heroAndMonsters
## Домашнее задание на тему "Циклы и функции". 
## Герой и чудовища
### Задание
Задача на умение следовать требованиям к программе и проверять программу по требованиям.
Написать текстовую игру «герой и чудовища». 
Игрок — рыцарь в фантастической стране. Ваша задача — победить 10 чудовищ, чтобы спасти королевство от нападения и тем самым выиграть игру.

### Дано
- Игра происходит по «ходам». Программа выводит на экран текст о том что происходит.
- Например: `«БОЙ! Вы встретили чудовище  4 жизнями и с силой удара 5»` (или что-то другое на ваш выбор главное чтобы было понятно).
- Управление событиями игры происходит с помощью `ввода с клавиатуры цифр, либо «1», либо «2»`.
- Например, программа выводит на экран `«1-атаковать чудовище, 2-убежать»` и приглашение к вводу либо `числа 1 либо 2`.
- При вводе любого другого текста должно быть показано сообщение о некорректном вводе и приглашение на ввод `«1» либо «2»` должно быть показано заново, пока пользователь не введёт `«1» либо «2»`.
- У рыцаря изначально `не менее 10 жизней` и `сила удара не менее 10`.
- Перед рыцарем `случайно возникает` либо `очередное чудовище`, либо `увеличивающее случайное число здоровья яблочко`, либо совершенно `новый меч со случайной силой атаки`. Игрок узнаёт об этом прочитав вывод программы на экран.
- При встрече с чудовищем, `у чудовища есть случайное число здоровья и атаки`, а `у игрока` - выбор (вводимый с клавиатуры) `1-сражаться`, `2-убежать`, чтобы набраться сил.
- При встрече с чудовищем нужно показать на экране `его жизни и силу удара`.
- В случае сражения рыцарь побеждает, если `число его атаки превосходит число жизней чудовища`. При этом чудовище отнимает у рыцаря число жизней, соответствующее его атаке.
- Если чудовище сильнее рыцаря, то есть, если сила атаки чудовища превосходит количество жизней рыцаря — рыцарь умирает, выводится сообщение `«ПОРАЖЕНИЕ! игра окончена»` и происходит завершение программы.
- При победе над 10 чудовищами, выводится сообщение  `"ПОБЕДА!"` (или что-то другое на ваш выбор) и происходит завершение программы.
- При обнаружении меча, на экран должна быть выведена его сила атаки и игроку даётся (вводимый с клавиатуры) выбор `1-взять меч себе выбросив старый`, `2-пройти мимо меча`. При взятии нового меча сила атаки рыцаря принимается равной силе атаки нового подобранного меча.
- При обнаружении яблочка — рыцарь съедает его, и узнаёт насколько он увеличил количество жизней и чему теперь равно его количество жизней. В случае нахождения яблочка игроку не даётся выбора действия.
- Границы случайных величин (`кол-ва жизней чудовищ`, `силы их атаки`, `силы атаки мечей` и `количество жизней, которое даёт яблочко`) предлагается определить самостоятельно, но так, чтобы в игру возможно было выиграть или проиграть
- Все атаки (и героя и чудовища) происходят одновременно. Если в одном ходу произошла и победа над последним чудовищем и смерть героя - то игра проиграна.

### Требуется
- Написать текстовую игру по требованиям описанным выше.
- Использовать циклы при написании программы
- Использовать функции при написании программы
- Не использовать сторонних библиотек
- Уместить код игры в одном файле

### Проверка качества кода
flake8 --max-line-length=120 .
pep257 .
mypy . --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs --check-untyped-defs  --disallow-untyped-decorators --ignore-missing-imports --pretty

### Требования для автоматической проверки решения юнит-тестами
- Главный (он же единственный) файл вашего решения называется `main.py`
- Главная функция, запустив которую начнется игра - это функция с названием `game()` без параметров
- Перед тем как дать игроку выбор драться с чудовищем или убежать, на экран должна быть выведена любая строка, в которой присутствует слово `БОЙ`. В этой же строке первое встреченное число будет обозначать число жизней чудовища, а второе - его силу удара.
- Перед тем как дать игроку выбор взять меч или пройти мимо него, на экран должна быть выведена любая строка, в которой присутствует слово `МЕЧ`, а также число обозначающее его силу атаки
- При победе в игре, на экран должна быть выведена любая строка, в которой присутствует слово `ПОБЕДА`
- При поражении в игре, на экран должна быть выведена любая строка, в которой присутствует слово `ПОРАЖЕНИЕ`
- Эти переменные должны быть глобальными: `monster_counter` - счетчик поверженных героем чудовищ, `hp` - текущее состояние здоровье героя, `attack` - текущая сила удара героя

### Как отправить ответ
Прикрепить ссылку на `merge-request` в вашем гитхаб или битбакет с Вашим решением. Нужен `merge-request` для удобства комментирования решения наставником

### Стенограмма видео лекции
Используйте `input` и `print`. 
Если у чудовища больше сила удара, чем жизней у героя — то поражение.
Если у чудовища жизней меньше, чем сила удара героя — то победа.
И при этом атака чудовища меньше, чем количество оставшихся жизней героя — победа, но жизни снимаются.
Количество жизни и количество атаки чудовищ генерируется случайно.
Последовательность событий — тоже случайно генерируется.
Использовать минимум 1 функцию.
Будет минимум 1 игровой вечный цикл.