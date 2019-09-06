

class projectHelper:
    def __init__(self, app):
        self.app = app

    def create_project(self):
        self.open_manage_page()
        self.fill_form_create_project()

    def fill_form_create_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("Project_name")
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("description")
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()