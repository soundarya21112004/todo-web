from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import time

app = Flask(__name__)

# DB config
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ✅ THIS WAS MISSING
db = SQLAlchemy(app)

# Table model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))

# ✅ Wait & create table properly
while True:
    try:
        with app.app_context():
            db.create_all()
        print("✅ Table created")
        break
    except Exception as e:
        print("⏳ Waiting for DB...")
        time.sleep(2)

@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_content = request.form.get('task')
    new_task = Task(content=task_content)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)