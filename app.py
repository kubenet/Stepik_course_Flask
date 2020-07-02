"""
    Проект первой недели по курсу "Flask с нуля"
    Ссылка на курс: https://stepik.org/course/61900

Задание:
        1. Распишите роуты, выведите тексты:
        – главной /, (выведите здесь будет главная);
        – направления /departures/<departure>/ (выведите здесь будет направление);
        – тура /tours/<id>/ (выведите здесь будет тур).

        2. Скопируйте шаблоны в папку templates:
        – index.html главной;
        – departure.html направления;
        – tour.html тура.

        3. Выведите нужный шаблон для каждого роута:
        – index.html для главной;
        – departure.html для направления;
        – tour.html для тура.

        Бонусная часть: (это не обязательно делать, но облегчит выполнение главы 2)

        1. Выведите на странице /
        <h1>Все туры:</h1>
        Куба: <a href="/tours/1/">Marina Lake Hotel & Spa 62000 4* </a>
        Вьетнам: <a href="/tours/2/">Baroque Hotel 85000 5* </a>
        Пакистан: <a href="/tours/3/">Voyager Resort 63000 3* </a>
        ...

        2. Выведите на странице /departures/<departure>
        <h1>Туры по направлению Новосибирск:</h1>
        Куба: <a href="/tours/1/">Marina Lake Hotel & Spa 62000 4* </a>
        Пакистан: <a href="/tours/3/">Voyager Resort 63000 3* </a>
        Индия: <a href="/tours/9/">Seascape Resort</a>
        ...

        3. Выведите на странице – тура /tours/<id>/

        <h1>Куба: Marina Lake Hotel & Spa 62000:</h1>
        <p>6 ночей</p>
        <p>Стоимость: 62000 Р</p>
        <p>Отель выглядит уютно. Он был построен из красного соснового дерева и украшен синими камнями. Высокие округлые окна добавляют общий стиль дома и были добавлены в дом в довольно симметричном образце.</p>

        Получите данные здесь:
        https://github.com/kushedow/flask-html/blob/master/Project%201/data.py

"""

from flask import Flask, render_template  # подключаем модули
import data

app = Flask(__name__)  # объявляем экземпляр фласка


@app.route('/')  # объявим путь к главной странице
def index():
    return render_template('index.html', title=data.title, subtitle=data.subtitle, description=data.description,
                           tours=data.tours, departures=data.departures)  # используем шалбон страницы


@app.route('/departures/<departure>/')  # путь отобразить направления
def departures(departure):
    return render_template('departure.html', departure=departure)


@app.route('/tours/<id_tour>/')  # путь просмотра тура
def tours(id_tour):
    return render_template('tour.html', id=id_tour)


app.run('0.0.0.0', 8000, debug=True)  # запустим сервер на 8000 порту, режим отладки включенен.
