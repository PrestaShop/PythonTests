import time
from screens.login_admin_page_screen import loginAdminPageScreen
from commons.logger import Logger
from commons.Context import Context 
from screens.admin_page_menu_screen import adminPageScreen



class admin_page():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, scenario, module, get_dataset=False):
        cls.context = Context()
        cls.context.scenario = scenario
        cls.context.module = module
            
    def orders(self):
        Logger().info("Go to the orders menu")
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            adminPageScreen().go_to_admin_menu('CustomerThreads','CustomerThreads_return')
            time.sleep(5)
            Logger().success("Go to the orders menu")
        except:
            raise

    def catalog(self):
        Logger().info("Go to the catalog menu")
        try:
            loginAdminPageScreen().connect(Context().environment.login, Context().environment.password)
            time.sleep(3)
            adminPageScreen().go_to_admin_menu('Catalog')
            time.sleep(5)
            Logger().success("Go to the catalog menu")
        except:
            raise