# -*- coding: utf-8 -*-
from commons.Context import Context 
from screens.install_shop_screen import installationScreen



class install_shop_page():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, scenario, module, get_dataset=False):
        cls.context = Context()
        cls.context.scenario = scenario
        cls.context.module = module
            
    def install_shop(self,var_test):
        new_store = False
        Context().logger.info("Creation of a new store")
        try:
            new_store = installationScreen().install_shop(var_test)
            Context().logger.info("New store is created")
        except:
            Context().logger.warning("Issue to create the new store")
        return new_store

    def reinstall_shop(self,var_test):
        new_store = False
        Context().logger.info("Reinstallation of an existing store")
        try:
            new_store = installationScreen().reinstall_shop(var_test)
            Context().logger.info("reinstallation is ok")
        except:
            Context().logger.warning("Issue to reinstall the store")
        return new_store