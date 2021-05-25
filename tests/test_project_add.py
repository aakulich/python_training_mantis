from model.project import Project
import string
import random



def random_proj_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



def test_project_add(app, db):
    app.session.login("administrator", "root")
    old_projects = db.get_project_list()
    project_name = random_proj_name("project_", 10)
    project = app.project.create(Project(name=project_name))
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


