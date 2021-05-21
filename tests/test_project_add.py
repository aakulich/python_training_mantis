from model.project import Project





def test_project_add(app, db):
    old_projects = db.get_project_list()
    project = app.project.create(Project(name="proj", description="descr"))
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


