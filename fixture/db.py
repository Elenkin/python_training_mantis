import pymysql.cursors
from model.projects import Projects

class DbFixture:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password, autocommit=True)

    def get_projects_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, description from mantis_project_table")
            for row in cursor:
                (id, name, status, description) = row
                list.append(Projects(id=str(id), name=name, status=status, description=description))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
