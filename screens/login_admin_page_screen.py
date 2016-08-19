from commons import ui
import time


class loginAdminPageScreen():    
    
    def __init__(self):
        self._objects = {
                        'email'  : ("xpath", "//*[@id = 'email']"),
                        'password'  : ("xpath", "//*[@id = 'passwd']"),
                        'btn_connection'  : ("xpath", "//*[@name='submitLogin']"),
                        'profil'  : ("xpath", "//*[@class = 'employee-dropdown dropdown']/div"),
                        'logout'  : ("xpath", "//*[@id = 'header_logout']"),
                        
                        
                         }
    def connect(self,login,password):
        time.sleep(2)
        ui.set_text(self._objects['email'], login)
        ui.set_text(self._objects['password'], password)     
        ui.click(self._objects['btn_connection'])

    def disconnect(self):
        time.sleep(2)
        ui.click(self._objects['profil'])
        time.sleep(3)
        ui.click(self._objects['logout'])

