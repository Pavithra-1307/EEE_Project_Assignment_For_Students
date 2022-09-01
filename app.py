from flask import Flask, request, redirect, render_template
from models import mydb,Employee
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee_project.mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
mydb.init_app(app)


@app.before_first_request
def create_table():
    mydb.create_all()


@app.route('/')
def index():
    all_data = Employee.query.all()
    return render_template("index.html", employees=all_data)

@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        email = request.form['email']
        employee = Employee(employee_id=employee_id, name=name, age=age, position=position,email=email)
        mydb.session.add(employee)
        mydb.session.commit()
        return redirect('/data')


@app.route('/data')
def get_all_employees():
    employees = Employee.query.all()
    return render_template('datalist.html', employees=employees)


@app.route('/data/<int:id>')
def get_employee(id):
    employee = Employee.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee=employee)
    return f"Submitted id 123 is not found in employee database"


@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    employee = Employee.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            mydb.session.delete(employee)
            mydb.session.commit()
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            email = request.form['email']
            employee = Employee(employee_id=id, name=name, age=age, position=position, email=email)
            mydb.session.add(employee)
            mydb.session.commit()
            return redirect('/data')
        return f"Employee with id = {id} Does nit exist"
    return render_template('update.html', employee=employee)


@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    employee = Employee.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            mydb.session.delete(employee)
            mydb.session.commit()
            return redirect('/data')
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)
