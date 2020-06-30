"""
    Проект первой недели по курсу "Flask с нуля"
    Ссылка на курс: https://stepik.org/course/61900
"""

from flask import Flask, render_template  # сперва подключим модуль

app = Flask(__name__)  # объявим экземпляр фласка


@app.route('/')  # объявим путь /
def hello():
    return render_template('index.html')


@app.route('/departures/<departure>/')  # отобразить направления
def departures(departure):
    return render_template('departure.html', departure=departure)


@app.route('/tours/<id_tour>/')  # здесь будет тур
def tours(id_tour):
    return render_template('tour.html', id=id_tour)


app.run('0.0.0.0', 8000, debug=True)  # запустим сервер на 8000 порту!
