PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                first_name VARCHAR(30) NOT NULL,
                last_name VARCHAR(30) NOT NULL,
                email VARCHAR(40) NOT NULL,
                department_id VARCHAR(20) REFERENCES department(id));
INSERT INTO employee VALUES(1,'f_name1','l_name1','ame1ame1@dot.com','2');
INSERT INTO employee VALUES(2,'f_name2','l_name2','ame2ame2@dot.com','1');
INSERT INTO employee VALUES(3,'f_name3','l_name3','ame3ame3@dot.com','1');
INSERT INTO employee VALUES(4,'f_name4','l_name4','ame4ame4@dot.com','3');
INSERT INTO employee VALUES(5,'f_name5','l_name5','ame5ame5@dot.com','1');
INSERT INTO employee VALUES(6,'f_name6','l_name6','ame6ame6@dot.com','2');
INSERT INTO employee VALUES(7,'f_name7','l_name7','ame7ame7@dot.com','2');
INSERT INTO employee VALUES(8,'f_name8','l_name8','ame8ame8@dot.com','3');
INSERT INTO employee VALUES(9,'f_name9','l_name9','ame9ame9@dot.com','2');
INSERT INTO employee VALUES(10,'f_name10','l_name10','ame10ame10@dot.com','3');
CREATE TABLE department (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    department_name VARCHAR(40) NOT NULL);
INSERT INTO department VALUES(1,'HR');
INSERT INTO department VALUES(2,'sales');
INSERT INTO department VALUES(3,'IT');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('employee',10);
INSERT INTO sqlite_sequence VALUES('department',3);
COMMIT;
