import pymysql.cursors
from fixture.db import DbFixture

connection = pymysql.connect(host="127.0.0.1", database="bugtracker", user="root", password="")
try:
    cursor = connection.cursor()
    cursor.execute("select * from mantis_project_table")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()

db = DbFixture(host="127.0.0.1", database="bugtracker", user="root", password="")
try:
    projects = db.get_projects_list()
    for project in projects:
        print(project)
    print(len(projects))
finally:
    db.destroy()


