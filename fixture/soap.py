from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app




    def can_login(self, username, password):
        client = Client(self.app.config["soap"]["soap_url"])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False




    def get_project_list(self, username, password):
        client = Client(self.app.config["soap"]["soap_url"])
        try:
            list = client.service.mc_projects_get_user_accessible(username, password)
            return list
        except WebFault:
            return False



