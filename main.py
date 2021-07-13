from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()

        return render_template('calories_form', caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(country=calories_form.country.data, city=calories_form.city.data)

        calorie = Calorie(weight=float(calories_form.weight.data, calories_form.height.data, ))