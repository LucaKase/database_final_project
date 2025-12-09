from flask import Flask, render_template, request
import mysql.connector
from routes.home import home_route
from routes.instructor_lesson import instructor_lesson_route
from routes.customer_lesson import customer_lesson_route
from routes.available_skis import available_skis_route
from routes.instructor_info import instructor_info_route
from routes.update_salary import update_salary_route
from routes.lessons_conditions import lesson_conditions_route
from routes.group_size import group_size_route
from routes.customer_by_nationality import customers_by_nationality_route
from routes.mountains_by_skills import mountains_by_skill_route
from routes.customer_revenue import customer_revenue_route

app = Flask(__name__)

try:
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="YourPassword",
        database="SkiSchool"
    )
    print("DB connected")
except mysql.connector.Error as err:
    print("Connection error:", err)


@app.route('/')
def home():
    return home_route()


@app.route('/lessons', methods=['GET', 'POST'])
def lessons():
    return instructor_lesson_route(db, request)


@app.route('/customer_lessons', methods=['GET', 'POST'])
def customer_lessons():
    return customer_lesson_route(db, request)


@app.route('/available_skis', methods=['GET', 'POST'])
def available_skis():
    return available_skis_route(db, request)


@app.route('/instructor_info', methods=['GET', 'POST'])
def instructor_info():
    return instructor_info_route(db, request)


@app.route('/update_instructor_salary', methods=['GET', 'POST'])
def update_instructor_salary():
    return update_salary_route(db, request)


@app.route('/lesson_conditions', methods=['GET', 'POST'])
def lesson_conditions():
    return lesson_conditions_route(db, request)


@app.route('/group_size', methods=['GET', 'POST'])
def group_size():
    return group_size_route(db, request)


@app.route('/customers_by_nationality')
def customers_by_nationality():
    return customers_by_nationality_route(db)


@app.route('/mountains_by_skill', methods=['GET', 'POST'])
def mountains_by_skill():
    return mountains_by_skill_route(db, request)


@app.route('/customer_revenue', methods=['GET', 'POST'])
def customer_revenue():
    return customer_revenue_route(db, request)


if __name__ == "__main__":
    app.run(debug=True)
