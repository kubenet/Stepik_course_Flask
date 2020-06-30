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
"""

from flask import Flask, render_template  # подключаем модули

app = Flask(__name__)  # объявляем экземпляр фласка


@app.route('/')  # объявим путь к главной странице
def index():
    return render_template('index.html')  # используем шалбон страницы


@app.route('/departures/<departure>/')  # путь отобразить направления
def departures(departure):
    return render_template('departure.html', departure=departure)


@app.route('/tours/<id_tour>/')  # путь просмотра тура
def tours(id_tour):
    return render_template('tour.html', id=id_tour)


app.run('0.0.0.0', 8000, debug=True)  # запустим сервер на 8000 порту, режим отладки включенен.
