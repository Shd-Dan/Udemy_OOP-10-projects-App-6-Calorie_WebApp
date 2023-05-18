"""Import Flask and wtforms"""
from flask.views import MethodView
from wtforms import Form
from flask import Flask

# Flask is an object that represents a web app

app = Flask(__name__)


class CalorieHomePage(MethodView):

    def get(self):
        return "Hello"


class CalorieFormPage(MethodView):

    def get(self):
        return print('Form Page')


class CalorieForm(Form):
    pass


app.add_url_rule('/', view_func=CalorieHomePage.as_view('home_page'))
app.add_url_rule('/form', view_func=CalorieFormPage.as_view('calorie_form_page'))

app.run()
