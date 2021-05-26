from model.project import Project
import random


def test_delete_some_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name="New project", description="new_descr"))
    old_projects = db.get_project_list()
    project2 = random.choice(old_projects)
    app.project.delete_project_by_id(project2.id)
    new_projects = db.get_project_list()
    assert len(old_projects) - 1 == app.project.count()
    old_projects.remove(project2)
    assert old_projects == new_projects


def test_delete_project_with_soap(app):
    username = "administrator"
    password = "root"
    if len(app.soap.get_project_list(username, password)) == 0:
        app.project.create(Project(name="New project", description="new_descr"))
    old_projects = app.soap.get_project_list(username, password)
    project2 = random.choice(old_projects)
    app.project.delete_project_by_id(project2.id)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) - 1 == app.project.count()
    old_projects.remove(project2)
    assert len(old_projects) == len(new_projects)




