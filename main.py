from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(FlaskForm):
    pr_city = IntegerField('Пробег город, км', validators=[DataRequired()])
    pr_state = IntegerField('Пробег трасса, км', validators=[DataRequired()])
    med_trip_city = IntegerField('Средняя поездка город, км', validators=[DataRequired()])
    med_trip_state = IntegerField('Средняя поездка трасса, км', validators=[DataRequired()])
    taxi_rate_city = FloatField('Тариф город, руб', validators=[DataRequired()])
    taxi_rate_state = FloatField('Тариф трасса, руб', validators=[DataRequired()])
    rate_boarding_ = FloatField('Стоимость посадки, руб', validators=[DataRequired()])
    include_trip = IntegerField('Включенные км', validators=[DataRequired()])
    submit = SubmitField('Рассчитать')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/count')
def count():
    return render_template('count.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
