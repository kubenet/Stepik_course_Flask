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

from flask import Flask, render_template
from data import tours as tour, departures as depart, subtitle, description, title

app = Flask(__name__)  # объявляем экземпляр фласка


@app.route('/')  # объявим путь к главной странице
def index():
    return render_template('index.html', title=title, tours=tour, subtitle=subtitle, departures=depart,
                           description=description)


@app.route('/departures/<string:departure>')  # путь отобразить направления
def departures(departure):

    lst_depart = []    # список индексов туров из соответстующих направлению
    price_depart = []  # список цен подходящих туров
    count_nights = []  # список кол-во ночей подходящих туров

    for t in tour:
        if departure == tour[t]['departure']:
            lst_depart.append(t)
            price_depart.append(tour[t]['price'])
            count_nights.append(tour[t]['nights'])
    return render_template('departure.html', title=title, tours=tour, subtitle=subtitle,
                           lst_departures=lst_depart, departures=depart, city=departure,
                           description=description, price_depart=price_depart, count_nights=count_nights)


@app.route('/tours/<int:id>/')  # путь просмотра тура
def tours(id):
    return render_template('tour.html', title=title, tour_title=tour[id]['title'],
                           country=tour[id]['country'], departures=depart[tour[id]['departure']], lst_departures=depart,
                           nights=tour[id]['nights'], description=tour[id]['description'],
                           picture=tour[id]['picture'], price=tour[id]['price'], stars=tour[id]['stars'])


app.run('0.0.0.0', 8000, debug=True)  # запустим сервер на 8000 порту, режим отладки включенен.
