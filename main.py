from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "100.27.62.167"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_employees"  

# Get all employees
@app.get("/employees")
def get_employees():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    mydb.close()
    return {"employees": result}

# Get an employee by ID
@app.get("/employees/{id}")
def get_employee(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM employees WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"employee": result}

# Add a new employee
@app.post("/employees")
def add_employee(item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    name = item.name
    age = item.age
    cursor = mydb.cursor()
    sql = "INSERT INTO employees (name, age) VALUES (%s, %s)"
    val = (name, age)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Employee added successfully"}

# Modify an employee
@app.put("/employees/{id}")
def update_employee(id:int, item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    name = item.name
    age = item.age
    cursor = mydb.cursor()
    sql = "UPDATE employees set name=%s, age=%s where id=%s"
    val = (name, age, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Employee modified successfully"}

# Delete an employee by ID
@app.delete("/employees/{id}")
def delete_employee(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM employees WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "Employee deleted successfully"}