from flask import Flask, request, redirect, render_template
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# ☛ Req -4 : Import db, Employee from models.py module
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# ☛ Req -5 : Create app object from Flask
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# ☛ Req -6 : Create database name called employee_project.db
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///<db_name>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# binding the instance to a specific Flask application
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# ☛ Req -7 : Create a method/function called landing_page() which should return a string 'You have landed EEE project-2022'
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        # ☛ Req -8 : Above if condition should render a template file called createpage.html
        # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = Employee(employee_id=employee_id, name=name, age=age, position=position)
        db.session.add(employee)
        db.session.commit()
        # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        # ☛ Req -9 : Above if condition should redirect to URI '/data'
        # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@app.route('/data')
def get_all_employees():
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # ☛ Req -10 : Fetch/Query all the rows and assign it to a variable called "employees"
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    return render_template('datalist.html', employees=employees)


@app.route('/data/<int:id>')
def get_employee(id):
    employee = Employee.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee=employee)
    return <text_will_go_here>
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # ☛ Req -11 : if given employee id was not found it should return a text called "Submitted id 123 is not found in employee database
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    employee = Employee.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = Employee(employee_id=id, name=name, age=age, position=position)
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"

    return render_template('update.html', employee=employee)


@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    employee = Employee.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
            # ☛ Req -12 : Ensure given record (1) get deleted and (2) Committed
            # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
            return redirect('/data')

    return render_template('delete.html')


if __name__ == '__main__':
    # """""""""""""""""""""""""""""""""""
    # ☛ Req -13 : Run app in debug mode
    # """""""""""""""""""""""""""""""""""
