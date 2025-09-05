#post lab 
import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('student_record_postlab.db')
cursor = conn.cursor()

# Create students table if it doesn't exist
# Composite primary key -> (Enrollment, Subject)
cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL,
                    PRIMARY KEY (Enrollment, Subject)
                )''')
conn.commit()

# Insert multiple student records (multiple subjects per student)
student_record = [
    (92400133020,'SALONI RAMAVAT','PWP',95),
    (92400133020,'SALONI RAMAVAT','Python',88),
    (92400133020,'SALONI RAMAVAT','DBMS',92),

    (92400133104,'AVANI KAVATHIYA','PWP',85),
    (92400133104,'AVANI KAVATHIYA','Python',80),

    (92400133120,'IRA BHOGAYATA','PWP',90),
    (92400133120,'IRA BHOGAYATA','Maths',84),

    (92400133059,'PINAL GONDALIYA','PWP',93),
    (92400133059,'PINAL GONDALIYA','Python',87),
    (92400133059,'PINAL GONDALIYA','DBMS',91),

    (92400133060,'SHREYA VACHANI','PWP',75),
    (92400133060,'SHREYA VACHANI','Maths',70)
]

# Insert records
cursor.executemany('''INSERT OR REPLACE INTO student_record (Enrollment, name, subject, Mark) 
                      VALUES (?, ?, ?, ?)''', student_record)
conn.commit()

# Fetch all student records
print("All Student Records (Multiple Subjects):")
cursor.execute('SELECT * FROM student_record ORDER BY Enrollment')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fetch students with Marks > 90
cursor.execute('SELECT name, subject, Mark FROM student_record WHERE Mark > 90')
high_marks = cursor.fetchall()
print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

# Update Mark for Ashutosh in Python
cursor.execute('''UPDATE student_record SET Mark = 94 
                  WHERE name = 'ASHUTOSH KUMAR SINGH' AND subject = 'Python' ''')
conn.commit()

cursor.execute('SELECT name, subject, Mark FROM student_record WHERE name = "ASHUTOSH KUMAR SINGH"')
print("\nUpdated Records for ASHUTOSH KUMAR SINGH:")
for row in cursor.fetchall():
    print(row)

# Delete a subject record for DEVENDRASINH
cursor.execute('''DELETE FROM student_record WHERE name = 'DEVENDRASINH DOLATSINH JADEJA' AND subject="Maths" ''')
conn.commit()

# Verify deletion
cursor.execute('SELECT * FROM student_record WHERE name = "DEVENDRASINH DOLATSINH JADEJA"')
print("\nRemaining records for DEVENDRASINH DOLATSINH JADEJA:")
for row in cursor.fetchall():
    print(row)

# Calculate average mark per student
print("\nAverage Marks per Student:")
cursor.execute('''SELECT name, AVG(Mark) FROM student_record GROUP BY Enrollment''')
for row in cursor.fetchall():
    print(f"{row[0]} : {row[1]:.2f}")

# Calculate average mark per subject
print("\nAverage Marks per Subject:")
cursor.execute('''SELECT Subject, AVG(Mark) FROM student_record GROUP BY Subject''')
for row in cursor.fetchall():
    print(f"{row[0]} : {row[1]:.2f}")

# Close connection
conn.close()