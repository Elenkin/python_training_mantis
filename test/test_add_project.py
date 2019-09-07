from model.projects import Projects
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app, db):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    project = Projects(name=random_string("Project_name", 15), description="Описание")
    old_project_list = db.get_projects_list()
    print(old_project_list)
    print (len(old_project_list))
    app.projects.create_project(project)
    new_project_list = db.get_projects_list()
    old_project_list.append(project)
    print(new_project_list)
    print(len(new_project_list))
    assert sorted(new_project_list, key=Projects.id_or_max) == sorted(old_project_list, key=Projects.id_or_max)
