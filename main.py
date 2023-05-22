"""Import Flask and wtforms"""
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

import calorie
import temperature

# Flask is an object that represents a web app

app = Flask(__name__)


class CalorieHomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CalorieFormPage(MethodView):

    def get(self):
        # initialize CalorieForm instance
        calorie_form = CalorieForm()
        return render_template('calorie_form_page.html', cal_form=calorie_form)

    def post(self):
        # Data entered in the form is got by CalorieForm instance initiating and request method of flask
        cal_form = CalorieForm(request.form)
        weight = cal_form.weight.data
        height = cal_form.height.data
        age = cal_form.age.data
        city = cal_form.city.data
        country = cal_form.country.data

        cal_temperature = temperature.Temperature(country, city).get()
        cal_result = calorie.Calorie(float(weight), float(height), float(age), cal_temperature)

        # return weight
        return render_template('calorie_form_page.html',
                               result=True,
                               cal_form=cal_form,
                               weight=cal_result.weight,
                               height=cal_result.height,
                               age=cal_result.age,
                               kcal=cal_result.calculate()
                               )


class CalorieForm(Form):
    weight = StringField('Weight: ', default=70)
    height = StringField('Height: ', default=180)
    age = StringField('Age: ', default=30)

    city = StringField('City: ', default='Madrid')
    country = StringField('Country: ', default='Spain')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=CalorieHomePage.as_view('home_page'))
app.add_url_rule('/form', view_func=CalorieFormPage.as_view('calorie_form_page'))

app.run(debug=True)
