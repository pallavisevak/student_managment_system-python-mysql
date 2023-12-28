import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sms2"
)
mycursor = mydb.cursor()
# mycursor.execute("create table classes(class_id INT AUTO_INCREMENT PRIMARY KEY,c_name VARCHAR(50),teacher_id INT REFERENCES teachers(teacher_id))")
# mycursor.execute("create table classroom(class_id INT AUTO_INCREMENT PRIMARY KEY,c_name VARCHAR(50),section VARCHAR(20),teacher_id INT,FOREIGN KEY(teacher_id) REFERENCES teachers2(teacher_id),course_id INT,FOREIGN KEY(course_id) REFERENCES courses2(course_id))")
sql = "INSERT INTO classroom(c_name,section,teacher_id,course_id) VALUES (%s,%s,%s,%s)"
val=[
('A101','A',1,1),
('B205','B',2,2),
('C309','C',3,3),
('D412','D',4,4),
('E514','E',5,5),
('F617','F',6,6),
('G720','G',7,7),
('H823','H',8,8),
('I926','I',9,9),
('J1030','J',10,10),
('A101','K',11,1),
('B205','L',12,2),
('C309','M',13,3),
('D412','N',14,4),
('E514','O',15,5),
('F617','P',16,6)
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")


# mycursor = mydb.cursor()
#
# sql = "DROP TABLE classes2"
#
# mycursor.execute(sql)
