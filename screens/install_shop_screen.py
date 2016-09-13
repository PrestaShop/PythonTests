from commons import ui
import time, datetime
from commons.Context import Context
from commons.Configuration import Configuration
from screens.login_admin_page_screen import loginAdminPageScreen


class installationScreen():
    def __init__(self):
        self._objects = {
            'langue_list': ("xpath", "//select[@id='langList']"),
            'langue': ("xpath", "//select[@id=\"langList\"]//option[@value='str(i)']"),
            'next': ("css", "#btNext"),
            'valid_license': ("css", "#set_license"),
            'name': ("css", "#infosShop"),
            'activity': ("xpath", "//select[@id=\"infosActivity\"]//option[@value='str(i)'][1]"),
            'firstname': ("css", "#infosFirstname"),
            'lastname': ("css", "#infosName"),
            'email': ("css", "#infosEmail"),
            'password': ("css", "#infosPassword"),
            'password2': ("css", "#infosPasswordRepeat"),
            'dbServer': ("css", "#dbServer"),
            'dbName': ("css", "#dbName"),
            'dbLogin': ("css", "#dbLogin"),
            'dbPassword': ("css", "#dbPassword"),
            'dbprefix': ("css", "#db_prefix"),
            'btn_test_db': ("css", "#btTestDB"),
            'btn_create_db': ("css", "#btCreateDB"),
            'check_db': ("xpath", "//p[@id='dbResultCheck']"),
            'close_welcome_popup': ("xpath", "//i[@class='material-icons onboarding-button-shut-down']"),
        }

    def install_shop(self, var_test):
        install_ok = False
        import shutil, os
        test = os.listdir(Context().environment.store_source.strip())
        test = sorted(test, reverse=True)
        test2 = []
        for my_list in test:
            if Configuration().version_presta in my_list:
                test2.append(my_list)

        test2 = sorted(test2, key=len, reverse=True)
        if test2 == []:
            my_version = Configuration().version_presta
        else:
            try:
                my_version = test2[0].split('_')[0] + "_" + str(int(test2[0].split('_')[1]) + 1)
            except:
                my_version = test2[0] + "_" + "1"

        if Configuration().git == False:
            try:
                Context().logger.info("Creating folder ({0})".format(my_version))
                shutil.copytree(Context().environment.store_source.strip() + Configuration().version_presta,
                                Context().environment.store_source.strip() + my_version)
                Context().logger.info("Folder was created")
            except WindowsError:
                Context().logger.error("Issue to duplicate the folder")
        else:
            try:
                Context().logger.info("Create since git the folder {0})".format(my_version))
                if var_test.get('git_repo') == "":
                    grepo = Configuration().git_repo
                else:
                    grepo = var_test.get('git_repo')
                os.system("git clone --recursive " + grepo + " " + Context().environment.store_source + my_version)
                Context().logger.info("Folder was cloned since git")
            except WindowsError:
                Context().logger.error("Issue to clone the folder since git {0}".format())

        Context().launch_browser2(clean_session=True)
        my_url = "http://str(j)str(i)/install-dev/index.php"
        storename = ""
        if Configuration().storename != None:
            storename = Configuration().storename
        if Configuration().vm == None:
            url = my_url.replace('str(i)', storename).replace('str(j)', 'localhost')
        else:
            url = my_url.replace('str(i)', storename).replace('str(j)', Configuration().vm)

        Context().goto_url(url)
        lang = ui.def_object(self._objects['langue'], var_test.get("langue"))
        ui.click(self._objects['langue_list'])
        ui.click(lang)
        ui.click(self._objects['next'])

        ui.click(self._objects['valid_license'])
        ui.click(self._objects['next'])

        time.sleep(3)
        ui.click(self._objects['next'])

        ui.set_text(self._objects['name'], my_version, True)
        ui.set_text(self._objects['firstname'], var_test.get("firstname"), True)
        ui.set_text(self._objects['lastname'], var_test.get("lastname"), True)
        ui.set_text(self._objects['email'], var_test.get("email"), True)
        ui.set_text(self._objects['password'], var_test.get("password"), True)
        ui.set_text(self._objects['password2'], var_test.get("password"), True)
        ui.click(self._objects['next'])

        ui.set_text(self._objects['dbServer'], var_test.get("dbServer"))

        if var_test.get("dbName") == "":
            ui.set_text(self._objects['dbName'], my_version, True)
        else:
            ui.set_text(self._objects['dbName'], var_test.get("dbName"))
        ui.set_text(self._objects['dbLogin'], var_test.get("dbLogin"))
        ui.set_text(self._objects['dbPassword'], var_test.get("dbPassword"))

        if var_test.get("dbprefix") == "":
            ui.set_text(self._objects['dbprefix'], ((my_version.replace(".", "")).replace("_", "") + "_"), True)
        else:
            ui.set_text(self._objects['dbprefix'], var_test.get("dbprefix"))
        ui.click(self._objects['btn_test_db'])

        ui.wait_loader("//p[@id='dbResultCheck' and @class='waitBlock']", 30, 1)

        db_check = ui.get_class(self._objects['check_db'])
        if db_check == "errorBlock":
            try:
                ui.click(self._objects['btn_create_db'])
                Context().logger.info("DB doesn't exist, try to generate it")
                try:
                    ui.wait_until("//p[@id='dbResultCheck' and @class='okBlock']", 60, 1)
                    Context().logger.info("DB was generated without issue")
                    ui.click(self._objects['btn_test_db'])
                    ui.wait_loader("//p[@id='dbResultCheck' and @class='waitBlock']", 60, 1)
                    ui.find_element("xpath", "//p[@id='dbResultCheck' and @class='okBlock']")
                except:
                    try:
                        ui.wait_until("//p[@id='dbResultCheck' and @class='errorBlock']", 60, 1)
                        Context().logger.error("Issue to create the DB")
                    except:
                        Context().logger.error("Issue to have the status of the creation of the DB")
            except:
                Context().logger.info("DB with this prefix already exist, try with another prefix")
                ui.set_text(self._objects['dbprefix'], datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_", True)
                ui.click(self._objects['btn_test_db'])
                ui.wait_loader("//p[@id='dbResultCheck' and @class='waitBlock']", 30, 1)
                db_check = ui.get_class(self._objects['check_db'])
                if db_check == "errorBlock":
                    ui.click(self._objects['btn_create_db'])
                    Context().logger.info("DB doesn't exist, try to generate it")
                    try:
                        ui.wait_until("//p[@id='dbResultCheck' and @class='okBlock']", 60, 1)
                        Context().logger.info("DB was generated without issue")
                        ui.click(self._objects['btn_test_db'])
                        ui.wait_loader("//p[@id='dbResultCheck' and @class='waitBlock']", 60, 1)
                        ui.find_element("xpath", "//p[@id='dbResultCheck' and @class='okBlock']")
                    except:
                        try:
                            ui.wait_until("//p[@id='dbResultCheck' and @class='errorBlock']", 60, 1)
                            Context().logger.error("Issue to create the DB")
                        except:
                            Context().logger.error("Issue to have the status of the creation of the DB")
                elif db_check == "okBlock":
                    Context().logger.info("DB is ok")
                else:
                    Context().logger.error("Issue to have the status of the DB")
        elif db_check == "okBlock":
            Context().logger.info("DB is ok")
        else:
            Context().logger.error("Issue to have the status of the DB")
        ui.click(self._objects['next'])

        ui.wait_until("//div[@class='progress']", 120, 5)
        ui.wait_loader("//ul[@id='stepList_1']//li[6][not(@class)]", 600, 10)
        try:
            ui.find_element("xpath", "//ul[@id='stepList_1']//li[6][@class='ok']")
            Context().logger.info("Installation of the account is completed")
            try:
                Context().browser.close()
                Context().launch_browser2(clean_session=True)
                storename = ""
                if Configuration().storename != None:
                    storename = Configuration().storename
                if Configuration().vm == None:
                    url = Context().environment.url.replace('str(i)', storename).replace('str(j)', 'localhost/')
                else:
                    url = Context().environment.url.replace('str(i)', storename).replace('str(j)',
                                                                                         Configuration().vm + '/')
                Context().goto_url(url)
                loginAdminPageScreen().connect(var_test.get("email"), var_test.get("password"))
                time.sleep(3)
                if (ui.is_visible(self._objects['close_welcome_popup'])):
                    ui.click(self._objects['close_welcome_popup'])
                loginAdminPageScreen().disconnect()
                install_ok = True
            except:
                Context().logger.error("Issue to close the current browser and open a new one to the new store.")
        except:
            ui.take_screenshot("Exception.png")
            Context().logger.error("Issue to finalize the creation of the account")

        return install_ok

    def reinstall_shop(self, var_test):
        reinstall_ok = False
        Context().launch_browser2(clean_session=True)
        my_url = "http://str(j)str(i)/install-dev/index.php"
        storename = ""
        if Configuration().storename != None:
            storename = Configuration().storename
        if Configuration().vm == None:
            url = my_url.replace('str(i)', storename).replace('str(j)', 'localhost')
        else:
            url = my_url.replace('str(i)', storename).replace('str(j)', Configuration().vm)

        Context().goto_url(url)
        time.sleep(2)
        lang = ui.def_object(self._objects['langue'], var_test.get("langue"))
        ui.click(lang)
        ui.click(lang)
        time.sleep(5)
        ui.click(self._objects['next'])

        ui.click(self._objects['valid_license'])
        ui.click(self._objects['next'])

        time.sleep(3)
        ui.click(self._objects['next'])

        ui.set_text(self._objects['name'], Configuration().version_presta, True)
        ui.set_text(self._objects['firstname'], var_test.get("firstname"), True)
        ui.set_text(self._objects['lastname'], var_test.get("lastname"), True)
        ui.set_text(self._objects['email'], var_test.get("email"), True)
        ui.set_text(self._objects['password'], var_test.get("password"), True)
        ui.set_text(self._objects['password2'], var_test.get("password"), True)
        ui.click(self._objects['next'])

        ui.set_text(self._objects['dbServer'], var_test.get("dbServer"))
        if var_test.get("dbName") == "":
            ui.set_text(self._objects['dbName'], Configuration().storename, True)
        else:
            ui.set_text(self._objects['dbName'], var_test.get("dbName"))
        ui.set_text(self._objects['dbLogin'], var_test.get("dbLogin"))
        ui.set_text(self._objects['dbPassword'], var_test.get("dbPassword"))
        ui.click(self._objects['btn_test_db'])

        ui.wait_loader("//p[@id='dbResultCheck' and @class='waitBlock']", 30, 1)

        db_check = ui.get_class(self._objects['check_db'])
        if db_check == "errorBlock":
            try:
                ui.click(self._objects['btn_create_db'])
                Context().logger.info("DB doesn't exist, try to generate it")
                try:
                    ui.wait_until("//p[@id='dbResultCheck' and @class='okBlock']", 60, 1)
                    Context().logger.info("DB was generated without issue")
                    ui.click(self._objects['btn_test_db'])
                    ui.wait_loader("//p[@id='dbResultCheck' and @class='waitBlock']", 60, 1)
                    ui.find_element("xpath", "//p[@id='dbResultCheck' and @class='okBlock']")
                except:
                    try:
                        ui.wait_until("//p[@id='dbResultCheck' and @class='errorBlock']", 60, 1)
                        Context().logger.error("Issue to create the DB")
                    except:
                        Context().logger.error("Issue to have the status of the creation of the DB")
            except:
                Context().logger.info("DB with this prefix already exist, try with another prefix")
                ui.set_text(self._objects['dbprefix'], datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_", True)
                ui.click(self._objects['btn_test_db'])
                ui.wait_loader("//p[@id='dbResultCheck' and @class='waitBlock']", 30, 1)
                db_check = ui.get_class(self._objects['check_db'])
                if db_check == "errorBlock":
                    ui.click(self._objects['btn_create_db'])
                    Context().logger.info("DB doesn't exist, try to generate it")
                    try:
                        ui.wait_until("//p[@id='dbResultCheck' and @class='okBlock']", 60, 1)
                        Context().logger.info("DB was generated without issue")
                        ui.click(self._objects['btn_test_db'])
                        ui.wait_loader("//p[@id='dbResultCheck' and @class='waitBlock']", 60, 1)
                        ui.find_element("xpath", "//p[@id='dbResultCheck' and @class='okBlock']")
                    except:
                        try:
                            ui.wait_until("//p[@id='dbResultCheck' and @class='errorBlock']", 60, 1)
                            Context().logger.error("Issue to create the DB")
                        except:
                            Context().logger.error("Issue to have the status of the creation of the DB")
                elif db_check == "okBlock":
                    Context().logger.info("DB is ok")
                else:
                    Context().logger.error("Issue to have the status of the DB")
        elif db_check == "okBlock":
            Context().logger.info("DB is ok")
        else:
            Context().logger.error("Issue to have the status of the DB")
        ui.click(self._objects['next'])

        ui.wait_until("//div[@class='progress']", 120, 5)
        ui.wait_loader("//ul[@id='stepList_1']//li[6][not(@class)]", 600, 10)
        try:
            ui.find_element("xpath", "//ul[@id='stepList_1']//li[6][@class='ok']")
            Context().logger.info("Installation of the account is completed")
            try:
                Context().browser.close()
                Context().launch_browser2(clean_session=True)
                if Configuration().vm == None:
                    url = Context().environment.url.replace('str(i)', storename).replace('str(j)', 'localhost/')
                else:
                    url = Context().environment.url.replace('str(i)', storename).replace('str(j)',
                                                                                         Configuration().vm + '/')

                Context().goto_url(url)
                loginAdminPageScreen().connect(var_test.get("email"), var_test.get("password"))
                time.sleep(3)
                if (ui.is_visible(self._objects['close_welcome_popup'])):
                    ui.click(self._objects['close_welcome_popup'])
                loginAdminPageScreen().disconnect()
                reinstall_ok = True
            except:
                Context().logger.error("Issue to close the current browser and open a new one to the new store.")
        except:
            ui.take_screenshot("Exception.png")
            Context().logger.error("Issue to finalize the creation of the account")

        return reinstall_ok
