# -*- coding: utf-8 -*-
import time
from screens.login_admin_page_screen import loginAdminPageScreen
from commons.Context import Context 
from screens.admin_page_new_menu_screen import adminPageScreen
from screens.module_screen import ModuleScreen



class admin_module_page():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, scenario, module, get_dataset=False):
        cls.context = Context()
        cls.context.scenario = scenario
        cls.context.module = module
            
    def search_module(self,var_test):
        module_check = False
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            try:
                adminPageScreen().go_to_admin_menu('Modules')
                Context().logger.info("Go on modules - modules menu")
            except:
                Context().logger.warning("Issue to go on modules - modules  menu")
                raise
            
            time.sleep(3)
            
            try:
                module_check = ModuleScreen().search_module(var_test)
                Context().logger.info("the module was found")
            except:
                Context().logger.warning("Issue with the module test")
                raise
            
            time.sleep(3)
            
            try:
                loginAdminPageScreen().disconnect()
            except:
                Context().logger.warning("Issue with log out")
                raise
            return module_check
        except:
            raise
        
    
    def check_categorie(self,var_test):
        module_check = False
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            try:
                adminPageScreen().go_to_admin_menu('Modules','Modules_modules')
                Context().logger.info("Go on modules - modules menu")
            except:
                Context().logger.warning("Issue to go on modules - modules  menu")
                raise
            
            time.sleep(3)
            
            try:
                module_check = ModuleScreen().check_categorie(var_test)
                Context().logger.info("the module was found")
            except:
                Context().logger.warning("Issue with the module test")
                raise
            
            time.sleep(3)
            
            try:
                loginAdminPageScreen().disconnect()
            except:
                Context().logger.warning("Issue with log out")
                raise
            return module_check
        except:
            raise
        
    def sort_modules(self,var_test):
        module_check = False
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            try:
                adminPageScreen().go_to_admin_menu('Modules','Modules_modules')
                Context().logger.info("Go on modules - modules menu")
            except:
                Context().logger.warning("Issue to go on modules - modules  menu")
                raise
            
            time.sleep(3)
            
            try:
                module_check = ModuleScreen().sort_modules(var_test)
                Context().logger.info("the module was found")
            except:
                Context().logger.warning("Issue with the module test")
                raise
            
            time.sleep(3)
            
            try:
                loginAdminPageScreen().disconnect()
            except:
                Context().logger.warning("Issue with log out")
                raise
            return module_check
        except:
            raise