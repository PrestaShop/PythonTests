# -*- coding: utf-8 -*-
import time
from screens.login_admin_page_screen import loginAdminPageScreen
from commons.Context import Context 
from screens.admin_page_new_menu_screen import adminPageScreen
from screens.catalog_product_screen import catalogProductScreen



class admin_catalog_page():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, scenario, module, get_dataset=False):
        cls.context = Context()
        cls.context.scenario = scenario
        cls.context.module = module
            
    def modify_product(self,var_test):
        found_product = False
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            try:
                adminPageScreen().go_to_admin_menu('Catalog','Catalog_products')
                Context().logger.info("Go on catalog - products menu")
            except:
                Context().logger.warning("Issue to go on catalog - products menu")
                raise
            time.sleep(3)
            try:
                found_product = catalogProductScreen().modify_product(var_test)
                Context().logger.info("the product has been modified")
            except:
                Context().logger.warning("Issue to modify the product")
                raise
            time.sleep(3)
            try:
                loginAdminPageScreen().disconnect()
            except:
                Context().logger.warning("Issue with log out")
                raise
            return found_product
        except:
            raise

    def add_product(self,var_test):
        new_product = False
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            try:
                adminPageScreen().go_to_admin_menu('Catalog')
                Context().logger.info("Go on catalog - products menu")
            except:
                Context().logger.warning("Issue to go on catalog - products menu")
                raise
            time.sleep(3)
            new_product = catalogProductScreen().add_product(var_test)
            if new_product == True:    
                Context().logger.info("the new product has been added")
            else:
                Context().logger.warning("Issue to add the new product")
            time.sleep(5)
            try:
                loginAdminPageScreen().disconnect(product_page=False)
            except:
                Context().logger.warning("Issue with log out")
                raise
            return new_product
        except:
            raise
        
    def product_catalog_sort(self,var_test):
        new_product = False
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            try:
                adminPageScreen().go_to_admin_menu('Catalog')
                Context().logger.info("Go on catalog - products menu")
            except:
                Context().logger.warning("Issue to go on catalog - products menu")
                raise
            time.sleep(3)
            try:
                new_product = catalogProductScreen().product_catalog_sort(var_test)
                Context().logger.info("the catalog has been checked")
            except:
                Context().logger.warning("Issue to check the category")
                raise
            time.sleep(3)
            try:
                loginAdminPageScreen().disconnect(product_page=False)
            except:
                Context().logger.warning("Issue with log out")
                raise
            return new_product
        except:
            raise