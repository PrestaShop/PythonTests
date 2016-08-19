# -*- coding: utf-8 -*-
import time
from screens.login_admin_page_screen import loginAdminPageScreen
from commons.Context import Context 
from screens.admin_page_new_menu_screen import adminPageScreen
from screens.admin_employee_screen import adminemployeeScreen



class admin_admin_page():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, scenario, module, get_dataset=False):
        cls.context = Context()
        cls.context.scenario = scenario
        cls.context.module = module
            
    def add_employee(self,var_test):
        found_employee = False
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            try:
                adminPageScreen().go_to_admin_menu('Preferences','Preferences_employees')
                Context().logger.info("Go on Back-office - employees menu")
            except:
                Context().logger.warning("Issue to go on Back-office - employees menu")
                raise
            time.sleep(3)
            try:
                new_employee = adminemployeeScreen().add_employees(var_test)
                Context().logger.info("the new employee has been added")
            except:
                Context().logger.warning("Issue to add the new employee")
                raise
            try:
                found_employee = adminemployeeScreen().check_employee(new_employee)
                Context().logger.info("Find informations about the employee")
            except:
                Context().logger.warning("Issue to find informations about the employee")
                raise
            time.sleep(3)
            try:
                loginAdminPageScreen().disconnect()
            except:
                Context().logger.warning("Issue with log out")
                raise
            return found_employee
        except:
            return False
            raise

    def delete_employee(self,employee=None):
            "A faire"
            Context().logger.info("Test a ecrire")
            
    def open_all_controller(self):
        open_controllers = True
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            try:
                adminPageScreen().open_all_contoller()
                Context().logger.info("Open all controllers")
            except:
                Context().logger.warning("Issue to open all controllers")
                open_controllers = False
                raise
            return open_controllers
        except:
            return False