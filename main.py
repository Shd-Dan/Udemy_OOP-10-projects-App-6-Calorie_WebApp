"""Import Flask and wtforms"""
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template

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


class CalorieForm(Form):
    weight = StringField('Weight: ')
    height = StringField('Height: ')
    age = StringField('Age: ')

    city = StringField('City: ')
    country = StringField('Country: ')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=CalorieHomePage.as_view('home_page'))
app.add_url_rule('/form', view_func=CalorieFormPage.as_view('calorie_form_page'))

app.run()
