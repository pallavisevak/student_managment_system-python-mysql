import mysql.connector
mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="sms2"
)
mycursor=mydb.cursor()
# mycursor.execute("create table course(course_id INT AUTO_INCREMENT PRIMARY KEY,course VARCHAR(50),description VARCHAR(20),class_id INT,FOREIGN KEY(class_id) REFERENCES classroom(class_id))")

sql = "INSERT INTO course(course,description,class_id) VALUES (%s,%s,%s)"
val=[
('Mathematics','Mathematics for Beginners',1),
('Computer Science','Introduction to Computer Science',2),
('Psychology','Introduction to Philosophy',3),
('Science','study of earth',4),
('Biology','hearth of human',5),
('Chemistry','byzantine',6),
('Physics','Introduction to kynamatics',7),
('designing','Creative Writing Workshop',8),
('Art History','World History: Ancient Civilizations',9),
('aviation','Introduction to Astrophysics',10)
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")