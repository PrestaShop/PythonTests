from commons import ui
import time


class loginAdminPageScreen():
    def __init__(self):
        self._objects = {
            'email': ("xpath", "//*[@id = 'email']"),
            'password': ("xpath", "//*[@id = 'passwd']"),
            'btn_connection': ("xpath", "//*[@name='submitLogin']"),
            'profil': ("xpath", "//*[@class = 'dropdown']//a//span//img"),
            'profil_other_page': ("xpath", "//*[@class = 'employee-dropdown dropdown']/div/i"),
            'logout': ("xpath", "//*[@id = 'header_logout']"),

        }

    def connect(self, login, password):
        time.sleep(2)
        ui.set_text(self._objects['email'], login)
        ui.set_text(self._objects['password'], password)
        ui.click(self._objects['btn_connection'])

    def disconnect(self, product_page=True):
        time.sleep(2)
        if (product_page) :
            ui.click(self._objects['profil'])
        else:
            ui.click(self._objects['profil_other_page'])
        time.sleep(3)
        ui.click(self._objects['logout'])

