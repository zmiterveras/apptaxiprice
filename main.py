from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(FlaskForm):
    mes = 'Значение должно быть числом вида: 2 или 2.3'
    pr_city = FloatField('Пробег город, км', validators=[DataRequired(mes)])
    pr_state = FloatField('Пробег трасса, км', validators=[DataRequired(mes)])
    med_trip_city = FloatField('Средняя поездка город, км', validators=[DataRequired(mes)])
    med_trip_state = FloatField('Средняя поездка трасса, км', validators=[DataRequired(mes)])
    taxi_rate_city = FloatField('Тариф город, руб', validators=[DataRequired(mes)])
    taxi_rate_state = FloatField('Тариф трасса, руб', validators=[DataRequired(mes)])
    rate_boarding = FloatField('Стоимость посадки, руб', validators=[DataRequired(mes)])
    include_trip = FloatField('Включенные км', validators=[DataRequired(mes)])
    submit = SubmitField('Рассчитать')


def counter(name):
    p_city = (name[0] / name[2]) * name[6] + (name[0] - name[7] * (name[0] / name[2])) * name[4]
    p_route = (name[1] / name[3]) * name[6] + (name[1] - name[7] * (name[1] / name[3])) * name[5]
    p = p_city + p_route
    return p_city, p_route, p


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/count', methods=['GET', 'POST'])
def count():
    name = []
    form = NameForm()
    if form.validate_on_submit():
        pr_city = form.pr_city.data
        pr_state = form.pr_state.data
        med_trip_city = form.med_trip_city.data
        med_trip_state = form.med_trip_state.data
        taxi_rate_city = form.taxi_rate_city.data
        taxi_rate_state = form.taxi_rate_state.data
        rate_boarding = form.rate_boarding.data
        include_trip = form.include_trip.data
        name.extend([pr_city, pr_state, med_trip_city, med_trip_state, taxi_rate_city, taxi_rate_state, rate_boarding,
                     include_trip])
        p_city, p_state, p = counter(name)
        return render_template('response.html', p_city=p_city, p_state=p_state, p=p)
    else:
        return render_template('count.html', form=form)


@app.errorhandler(404)
def page_not_found():
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
