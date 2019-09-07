from model.projects import Projects
import random

def test_del_project(app, db):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    if len(db.get_projects_list()) == 0:
        project = Projects(name="Project_4", description="Описание")
        app.projects.create_project(project)
    old_project_list = db.get_projects_list()
    print(old_project_list)
    print(len(old_project_list))
    project = random.choice(old_project_list)
    app.projects.dell_progect()
    new_project_list = db.get_projects_list()
    old_project_list.remove(project)
    print(new_project_list)
    print(len(new_project_list))
    assert sorted(new_project_list, key=Projects.id_or_max) == sorted(old_project_list, key=Projects.id_or_max)