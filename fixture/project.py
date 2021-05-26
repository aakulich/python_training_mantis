from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init project creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
       # self.return_to_projects_page()
        self.project_cache = None
        return project

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)


    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_id(id)
        #submit deletion
        #wd.find_element_by_link_text("Delete Project").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None


    def select_project_by_id(self, id):
        wd = self.app.wd
        t = str(id)
        wd.find_element_by_xpath('//a[@href = "manage_proj_edit_page.php?project_id=' + str(id) + '"]').click()

    def count(self):
        wd = self.app.wd
        self.open_projects_page()
        c = len(wd.find_elements_by_xpath('//a[contains(@href, "manage_proj_edit_page.php?project_id=")]'))
        return c


