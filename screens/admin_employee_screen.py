import time
from commons import ui
from commons.Context import Context


class adminemployeeScreen():    
    
    def __init__(self):
        self._objects = {
                        'employees_table' : ("css",".table.employee"),
                        'employees_table_number' : ("xpath","//*[@class='badge']"),
                        'employees_table_id_desc' : ("xpath","//table[@class='table employee']//tr[1]/th/span/a[1]"),
                        'employees_table_check' : ("xpath","//*[@class='table employee']//tbody//tr[1]"),
                        'employees_table_check2': ("xpath","//*[@class=\"table employee\"]//tbody//tr[str(i)]"),
                        'employees_table_active' : ("xpath","//*[@class='table employee']//tbody//tr[1]//td[7]/a"),
                        'add_employees' : ("css","#page-header-desc-employee-new_employee"),
                        'add_employee_firstname': ("css","input#firstname"),
                        'add_employee_lastname': ("css","input#lastname"),
                        'add_employee_email': ("css","input#email"),
                        'add_employee_password': ("css","input#passwd"),
                        'add_employee_nl_on' : ("xpath","//label[@for='optin_on']"),
                        'add_employee_nl_off' : ("xpath","//label[@for='optin_off']"),
                        'add_employee_active_on' : ("xpath","//label[@for='active_on']"),
                        'add_employee_active_off' : ("xpath","//label[@for='active_off']"),
                        'add_employee_profile_SuperAdmin' : ("xpath","//*[@id = 'id_profile']/option[text()='SuperAdmin']"),
                        'add_employee_save' : ("css","#employee_form_submit_btn"),
                        'table_test' : ("xpath","//*[@class='table employee']//tbody//tr[2]"),
                         }

    def add_employees(self,var_test):
        if ui.get_text(self._objects['employees_table_number']) == "1":
            max_id = ui.get_text(self._objects['employees_table_check']).split(" ")[0] 
        else:
            ui.click(self._objects['employees_table_id_desc'])
            max_id = ui.get_text(self._objects['employees_table_check']).split(" ")[0]            
        ui.click(self._objects['add_employees'])
        ui.wait_until(self._objects['add_employee_firstname'][1],60,1,self._objects['add_employee_firstname'][0])
        ui.native_set_text(self._objects['add_employee_firstname'], var_test.get("firstname"))
        ui.native_set_text(self._objects['add_employee_lastname'], var_test.get("lastname"))
        
        false_random = int(max_id) + 1
        my_email = (Context().browser.name + str(false_random) +  var_test.get("email")).replace(" ","")
        ui.set_text(self._objects['add_employee_email'], my_email)
        ui.set_text(self._objects['add_employee_password'], var_test.get("password"))
        if var_test.get("prestanl") == "yes":
            ui.click(self._objects['add_employee_nl_on'])
        if var_test.get("prestanl") == "no":
            ui.click(self._objects['add_employee_nl_off'])
        if var_test.get("active") == "yes":
            ui.click(self._objects['add_employee_active_on'])
        if var_test.get("active") == "no":
            ui.click(self._objects['add_employee_active_off'])
        my_profile = ("xpath","//*[@id = 'id_profile']/option[text()='" + var_test.get("profile") + "']")
        ui.click(my_profile)
        ui.click(self._objects['add_employee_save'])
        time.sleep(3)
        my_employee = {}
        my_employee.update({'old_max_id': max_id})
        my_employee.update({'my_email': my_email})
        my_employee.update({'firstname': var_test.get("firstname")})
        my_employee.update({'lastname': var_test.get("lastname")})
        my_employee.update({'profil': var_test.get("profile")})
        my_employee.update({'active': var_test.get("active")})
        return my_employee
        
       
    def check_employee(self,employee):    
        employee_found=False
        for i in range(1,10):
            row_employee = ui.def_object(self._objects['employees_table_check2'],i)
            new_employee = ui.get_text(row_employee)
            if employee['my_email']==str(new_employee.split(" ")[3]) :
                check_active = False
                if(employee['active']=="yes"):
                    if(ui.get_class(self._objects['employees_table_active'])=="list-action-enable action-enabled"): check_active = True
                else: 
                    if(ui.get_class(self._objects['employees_table_active'])=="list-action-enable action-disabled"): check_active = True
                if (new_employee.split(" ")[0] > employee['old_max_id'] and 
                    employee['firstname']==str(new_employee.split(" ")[1]) and 
                    employee['lastname']==str(new_employee.split(" ")[2]) and
                    employee['profil']==new_employee.split(" ")[4].split('\n')[0] and
                    check_active == True
                   ):
                    employee_found = True
                    break;
        return employee_found
     
