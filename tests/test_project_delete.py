
import random


def test_delete_some_project(app, db):
    app.session.login("administrator", "root")
    if db.get_project_list() == 0:
        app.project.create(Project(name="New project", description="new_descr"))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = db.get_project_list()
    assert len(old_projects) - 1 == app.project.count()
    old_projects.remove(project)
    assert old_projects == new_projects
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_project_list(), key=Project.id_or_max)