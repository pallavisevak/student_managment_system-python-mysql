import mysql.connector
mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="sms2"
)
mycursor=mydb.cursor()
# #crate table of student
# mycursor.execute("create table teachers2(teacher_id INT AUTO_INCREMENT PRIMARY KEY,class_id INT,FOREIGN KEY(class_id) REFERENCES classes3(class_id),fname VARCHAR(20),lname VARCHAR(20),dob VARCHAR(20),gender VARCHAR(20),address VARCHAR(50),mobile VARCHAR(20),email VARCHAR(20))")


sql = "INSERT INTO teachers2(class_id,fname,lname,dob,gender,address,mobile,email) VALUES (%s,%s, %s,%s,%s,%s,%s,%s)"
val=[

(1,'Kennan','Bentley','1996-10-24','male','Hastings','0800 747 3314','kennan@google.com'),
(2,'Isadora','Hudson','1997-05-15','female','Beverley','0845 46 40','isadora997@protonmail.com'),
(3,'Nissim','Chase','1998-07-31','male','Greenlaw','913452****','nissim@yahoo.com'),
(4,'Kiayada','Puckett','2000-01-19','male','Aberdeen','056 7176 6377','kiayada2016@yahoo.com'),
(5,'Axel','Burch','2000-07-26','male','Burntisland','0800 1111','axel6284@outlook.com'),
(6,'Dawn','Henson','1999-04-12','male','Peterhead','0845 46 46','dawn6526@aol.com'),
(7,'Daphne','Brady','2002-09-08','male','East Linton','0800 1111','daphne4194@yahoo.com'),
(8,'Eaton','Jarvis','1997-04-13','male','Peterborough','913452****','eaton@yahoo.com'),
(9,'Ezekiel','Duffy','1999-08-04','male','Macduff','913452****','ezekiel@outlook.com'),
(10,'Carlos','Price','1997-05-11','male','Dingwall','056 7210 2862','carlos4235@yahoo.com'),
(11,'Gail','Daugherty','2001-10-02','female','Subiaco','0800 1111','gail@protonmail.com'),
(12,'Nelle','Head','1997-05-14','male','Falkirk','0800 1111','nelle347@protonmail.com'),
(13,'Yuri','Leach','1998-07-19','female','Penicuik','913452****','yuri738@yahoo.com'),
(14,'Althea','David','2001-06-29','female','Chesterfield','0845 46 46','althea@outlook.com'),
(15,'Kareem','Coffey','1996-09-12','female','Darwin','0845 46 45','kareem4049@outlook.com'),
(16,'Cain','Holden','1997-09-07','female','Cockburn','0800 1111','cain@protonmail.com'),


]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")