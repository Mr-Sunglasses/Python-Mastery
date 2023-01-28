import sqlite3

conn = sqlite3.connect('data.db')

cr = conn.cursor()


"""
NULL - NO value
INTEGER - Numbers
REAL - Decimals
TEXT - String
BLOB - img, video, mp3
"""

# cr.execute("""CREATE TABLE resources (
#     first_name text,
#     last_name text,
#     email text,
#     age integer
# )""")
# data_fields = int(input("How many Data Fields you want to Enter: "))
# for i in range(data_fields):
#     print(f"For the Entry {i}")
#     first_name = input("Please Enter the First name: ")
#     last_name = input("Please Enter the Last name: ")
#     email = input("Please Enter the Email: ")
#     age = int(input("Please Enter the age: "))
#     cr.execute(f"""INSERT INTO resources VALUES ({str(first_name)}, {str(last_name)}, {str(email)}, {int(age)})""")
#     print(f"Data of user {i} is written in the database")

# cr.execute(f"""INSERT INTO resources VALUES ("Srijan", "Srivastava", "ss02@gmail.com", 21)""")
# print(f"Data of user is written in the database")

# many_resources = [
#     ('Suyash', 'Srivastava', 'suyash@gmail.com', 22),
#     ('Arunima', 'Shukla', 'nima.s_1903@gmail.com', 21),
#     ('Ananya', 'Sharma', 'sharmaananya@gmail.com', 22)
# ]
#
# cr.executemany("INSERT INTO resources VALUES (?, ?, ?, ?)", many_resources)
# print(f"Data of user is written in the database")
# commit out data

# data_fields = int(input("How many Data Fields you want to Enter: "))
# many_resources = []
# for i in range(data_fields):
#     print(f"For the Entry {i}")
#     first_name = input("Please Enter the First name: ")
#     last_name = input("Please Enter the Last name: ")
#     email = input("Please Enter the Email: ")
#     age = int(input("Please Enter the age: "))
#     t = (first_name, last_name, email, age)
#     many_resources.append(t)
#     print(f"Data of user {i} is written in the database")
#
# cr.executemany("INSERT INTO resources values (?, ? , ? , ?)", many_resources)
# print(f"Data of user is written in the database")


# cr.execute("SELECT * FROM resources")
# cr.execute("SELECT rowid, * FROM resources")
# for i in cr.fetchall():
#     print(i)

# cr.execute("SELECT * FROM resources where age > 21")
#
# data = cr.fetchall()
# print(data)
#
# cr.execute("SELECT * FROM resources where first_name = 'Anjuman'")
# data2 = cr.fetchall()
# print(data2)


# cr.execute("SELECT * FROM resources where last_name LIKE 'Ha%'")
#
# data = cr.fetchall()
# print(data)

# cr.execute("""UPDATE resources SET first_name='Kanishak' WHERE last_name LIKE 'Pac%'""")
# cr.execute("""UPDATE resources SET first_name='Kanishak' WHERE rowid = 1""")

# cr.execute("DELETE FROM resources where rowid = 9")
# cr.execute("SELECT rowid, * FROM resources WHERE last_name LIKE 'Has$' OR first_name LIKE 'Anju%'")
cr.execute("SELECT * FROM resources WHERE age > 18 LIMIT 3 ")

DATA = cr.fetchall()
print(DATA)
# Commit into the database
conn.commit()

# close connection
conn.close()



# Droping a table cr.execute("DROP TABLE resources")