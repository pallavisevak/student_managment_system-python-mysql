import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sms2"
)
mycursor = mydb.cursor()
# mycursor.execute("create table exam(exam_id INT AUTO_INCREMENT PRIMARY KEY,course_id INT,FOREIGN KEY (course_id) REFERENCES course(course_id), class_id INT,FOREIGN KEY (class_id) REFERENCES classroom(class_id),exam_name VARCHAR(20),exam_date DATE,exam_time TIME,max_marks INT)")
sql = "INSERT INTO exam(course_id,class_id,exam_name,exam_date,exam_time,max_marks) VALUES (%s,%s,%s,%s,%s,%s)"
val=[
(1,1,'english','2024-12-25','12:57 p.m.',100),
(2,2,'c','2024-08-04','12:00 p.m.',100),
(3,3,'english','2024-02-25','10:03 a.m.',100),
(4,4,'english','2024-03-01','11:30 a.m.',100),
(5,5,'english','2023-06-05','8:59 a.m.',100),
(6,6,'python','2023-05-26','11:26 a.m.',100),
(7,7,'english','2024-11-21','12:34 p.m.',100),
(8,8,'html','2023-11-27','9:36 a.m.',100),
(9,9,'physics','2024-11-02','12:27 p.m.',100),
(10,10,'chemistry','2024-04-26','11:54 a.m.',100),
(11,11,'computer','2023-11-17','10:52 a.m.',100),
(12,12,'c++','2023-01-31','12:06 p.m.',100),
(13,13,'english','2023-06-18','8:05 a.m.',100),
(14,14,'chemistry','2024-12-17','8:34 a.m.',100),
(15,15,'python','2023-03-18','12:23 p.m.',100),
(16,16,'physics','2023-10-10','1:19 p.m.',100)

]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")


# mycursor = mydb.cursor()
#
# sql = "DROP TABLE classes"
#
# mycursor.execute(sql)


