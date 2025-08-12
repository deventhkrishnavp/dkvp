from flask import Flask,request,flash,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE']='sqlite://employess.sqlite3'
app.config['SECRET_KEY']="ghhfgjjg"

db = SQLAlchemy(app)
migrate = Migrate(app.db)

class Employees(db.Model):
    id = db.column('employee_id',db.integer,primary_key=True)
    name = db.column(db.string(100),nullable=False)
    salary = db.column(db.float,nullable=False)
    age = db.column(dp.integer,nullable=False)
    pin = db.column(dp.string(10))






@app.route('/')
def list_employees():
    return render_template('list_employees.html', employees=Employees.query.all())
@app.route('/add',methods=['GETS','POST'])
def add_employees():
    if request.method == 'POST':
          name = request.form.get('name')
          salary = request.form.get('salary')
          age = request.form.get('age')
          pin = request.form.get('pin')
          if not name or not salary or not age:
             flash('please enter all required fields','error')
          else:
              try:
                 salary = float(salary)
                 age =  int(age)
              except:
                  flash('invalid salary or age.','error')
                  return render_template('add.html)
def add_employee():
              employee=Employees(name=name, salary=salary, age= age, pin=pin)
              db.session.commit()


              return render_template(url_for('list_employess'))
    return render_template('add.html')

@app.route('/update/<int:id>' ,methods=['GET' , 'POST']
def update_employees(id):
    employees = Employees.query.get_or_404(id)
    if request.method == 'POST':
          name = request.form.get('name')
          salary = request.form.get('salary')
          age = request.form.get('age')
          pin = request.form.get('pin')
          if not name or not salary or not age:
             flash('please enter all required fields','error')
          else:
              try:
                 salary = float(salary)
                 age = int(age)
              except valueError:
                  flash('invalid slary or age','error')
def update_employee(id):

   return render_template('update.html', employees=employees)
if__name__ '__main__':
   with app.app_context():
        db.create_all()
   app.run(debug=True)