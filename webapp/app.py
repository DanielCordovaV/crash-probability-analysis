from flask import Flask, render_template, request, redirect
import process as ps
import webbrowser

app = Flask(__name__)


@app.route('/check')
def sanity_check():
    return 'Si está funcionando', 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/analysis')
def analysis():
    return render_template('display_type.html'), 200


@app.route('/variables', methods=['GET', 'POST'])
def variables():
    display_type = request.form.get("display_type")

    if display_type == 'live':
        return render_template('tableu.html')
    elif display_type == 'live02':
        return render_template('tableu02.html')
    elif display_type == 'live03':
        return render_template('tableu03.html')
    elif display_type == 'live04':
        return render_template('tableu04.html')
    elif display_type == 'calc':
        return render_template('calc.html')

    return render_template('variables.html', display_type=display_type), 200


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    mes = request.form.get("mes")
    day_of_week = request.form.get("day_of_week")
    weather = request.form.get("weather")
    ciudad = request.form.get("ciudad")
    time = request.form.get("time")

    probabilidad = ps.get_probabilidad(mes=mes, day_of_week=day_of_week, weather=weather, ciudad=ciudad, time=time  )

    return render_template('calculate.html', probabilidad=round(probabilidad * 100, 3)), 200


@app.route('/')
def home():
    return render_template('index.html'), 200


@app.route('/home')
def main_menu():
    return render_template('index.html'), 200


@app.route('/visualize', methods=['GET', 'POST'])
def visualize():
    variable = request.form.get("variable")

    ps.run(variable)

    n = ps.get_id()
    n = int(n) - 1

    webbrowser.open_new_tab(f'http://localhost:5000/static/result{n}.jpg')

    return render_template('display_type.html'), 200


if __name__ == '__main__':
    app.run()
