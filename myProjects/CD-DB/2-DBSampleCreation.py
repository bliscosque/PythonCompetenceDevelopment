import sys, os, random
from PySide6.QtSql import QSqlDatabase,QSqlQuery

# Para fazer dump: c:\sqlite\sqlite3.exe .\emp.db .dump >> emp.sql

class CreateEmployeeData:
    # Connect to DB
    database=QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName(os.path.dirname(os.path.abspath(__file__))+"/emp.db")
    if not database.open():
        print("Unable to open DB file")
        sys.exit(1)
    
    
    query=QSqlQuery()
    # erase all...
    query.exec("DROP TABLE employee")
    query.exec("DROP TABLE department")

    query.exec("""CREATE TABLE employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                first_name VARCHAR(30) NOT NULL,
                last_name VARCHAR(30) NOT NULL,
                email VARCHAR(40) NOT NULL,
                department_id VARCHAR(20) REFERENCES department(id))""")
    
    query.prepare("""INSERT INTO employee (
                  first_name, last_name, 
                  email, department_id) 
                  VALUES (?, ?, ?, ?)""")
    
    departments={"HR": 1, "sales": 2, "IT": 3}
    department_names=list(departments.keys())
    department_codes=list(departments.values())

    for i in range(1,11):
        f_name=f'f_name{i}'
        l_name=f'l_name{i}'
        email=(l_name[3:]+f_name[3:]+'@dot.com')
        dept=random.choice(department_codes)
        query.addBindValue(f_name)
        query.addBindValue(l_name)
        query.addBindValue(email)
        query.addBindValue(dept)
        query.exec()
    
    # create dept query
    dept_query=QSqlQuery()
    dept_query.exec("""CREATE TABLE department (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    department_name VARCHAR(40) NOT NULL)""")

    dept_query.prepare("INSERT INTO department (department_name) VALUES(?)")

    for name in department_names:
        dept_query.addBindValue(name)
        dept_query.exec()

    print("DB CREATED")

if __name__=='__main__':
    CreateEmployeeData()
    sys.exit(0)