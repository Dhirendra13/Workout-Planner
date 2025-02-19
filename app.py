from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dhirendra@13",
    database="workout_planner"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM workouts")
    workouts = cursor.fetchall()
    return render_template('index.html', workouts=workouts)

@app.route('/add', methods=['POST'])
def add():
    user_name = request.form['user_name']
    workout_name = request.form['workout_name']
    date = request.form['date']

    cursor = db.cursor()
    cursor.execute("INSERT INTO workouts (user_name, workout_name, date) VALUES (%s, %s, %s)", (user_name, workout_name, date))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
