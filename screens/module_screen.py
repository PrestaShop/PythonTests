# -*- coding: utf-8 -*-
from commons import ui
import time
from commons.Context import Context
from commons.Configuration import Configuration
from selenium.webdriver.common.keys import Keys
from commons.Test import Test
from screens.admin_page_menu_screen import adminPageScreen



class ModuleScreen():    
    
    def __init__(self):
        self._objects = {
                        'search' : ("css","input.pstaggerAddTagInput.module-tags-input"),
                        'nb_result_search' : ("xpath", "//span[@class=\"module-search-result-wording\"]"),
                        'block_module_first' : ("xpath","(//div[@class=\"row modules-list\"]/div)[str(i)]"),
                        'block_module' : ("xpath","(//div[@class=\"row modules-list\"]/div[not(@style)])[str(i)]"),
                        'list_module_first' : ("xpath","(//div[@class=\"row modules-list\"]/div)[str(i)]"),
                        'list_module' : ("xpath","(//div[@class=\"row modules-list\"]/div[not(@style)])[str(i)]"),
                        'sort_type' : ("xpath","//div[@class='module-sorting module-sorting-author pull-right']/select/option[@value='str(i)']"),
                        'categories' : ("xpath","//li[@class='module-category-menu']"),
                        'blocks_module_categorie' : ("xpath","//div[@class=\"module-item-grid col-12 col-xl-3 col-lg-4 col-md-6 col-sm-12\" and @style=\"display: block;\" and @data-categories=\"str(i)\"]"),
                        'list_categories' : ("css","#categories"),
                        'name_categories' : ("xpath","//li[@class='module-category-menu']"),
                        'categorie' : ("xpath","(//li[@class=\"module-category-menu\"]/a)[str(i)]"),
                        'blocks_module_categorie' : ("xpath","//div[@class=\"module-item-grid col-12 col-xl-3 col-lg-4 col-md-6 col-sm-12\" and @style=\"display: block;\" and @data-categories=\"str(i)\"]"),
                        'cancel_search' : ("xpath","//i[@class=' material-icons']"),
                        'grid_view' : ("css","#module-sort-grid"),
                        'list_view' : ("css","#module-sort-list"),
                        'rest_category_filter' : ("css",".module-category-reset"),
                        'block_module_name' : ("xpath","(//div[@class='module-item-grid col-12 col-xl-3 col-lg-4 col-md-6 col-sm-12']//div[@class='text-ellipsis module-name-grid'])[1]"),
                        'opened_module_title' : ("xpath", "//div[@class='modal-header module-modal-header']/div/div/h4"),
                        'opened_module_author' : ("xpath","//div[@class='modal-header module-modal-header']/div/div/div"),
                        'opened_module_desc' : ("xpath","(//div[@class='modal-body row module-modal-body']//div/div/div/p)[1]"),
                        'tab_installed_modules' : ("xpath","//a[@class=\"tab\"][1]"),
                        'installed_modules_nb_result_search' : ("xpath", "(//span[@class=\"module-search-result-wording\"])[str(i)]"),
                        'installed_list_module' : ("xpath","((//div[@class=\"row modules-list\"])[str(i)])/div[str(j)]"),
                        'installed_list_first_module' : ("xpath","((//div[@class=\"row modules-list\"])[str(i)])/div[1]"),
                        }
        
    def search_module(self,var_test):
       
        """
        try:
            ui.click(("css","a.hide-button"), test=True)
        except:
            None
        """
        
        if var_test.get('view') == "grid" :
            ui.click(self._objects['grid_view'])
            nb_modules=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
            i=1
            all_modules = []
            while i<=nb_modules:
                try:
                    def_module = ui.def_object(self._objects['block_module_first'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                except:
                    def_module = ui.def_object(self._objects['block_module'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                all_modules.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                i=i+1;
            
            my_search_grid = False
            ui.set_text(self._objects['search'], var_test.get('search_name'))
            my_elem = ui.find_element(self._objects['search'][0],self._objects['search'][1])
            time.sleep(2)
            my_elem.send_keys(Keys.ENTER)
            nb_search_result=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
            if nb_search_result > 0 :
                nb_found=0
                for modules_search in all_modules:
                    if var_test.get('search_name').lower() in modules_search[0].lower() or var_test.get('search_name').lower() in modules_search[1].lower() or var_test.get('search_name').lower() in modules_search[2].lower():
                        nb_found = nb_found +1 
                if nb_search_result == nb_found :
                    i=1
                    check_search = 0
                    order_module = []
                    while i<=nb_search_result:
                        def_module = ui.def_object(self._objects['block_module'], i)
                        my_module = ui.find_element(def_module[0],def_module[1])
                        check_module = {} 
                        order_module.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price')))
                        check_module['data-name']=my_module.get_attribute('data-name')
                        check_module['data-description']=my_module.get_attribute('data-description')
                        check_module['data-author']=my_module.get_attribute('data-author')
                        
                        for var in check_module:
                            if var_test.get('search_name').lower() in check_module.get(var).lower():
                                check_search = check_search +1 
                                break;
                        i = i+1
                    
                    ui.click(self._objects['cancel_search'])
                    nb_modules2=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])    
                    
                    if check_search == nb_search_result and nb_modules == nb_modules2:
                        my_search_grid = True
                    else:
                        Context().logger.error("Modules found by the search not matching with the search : " + var_test.get('search_name'))
                else:
                    Context().logger.error("Number of module found by the search is wrong. Number of module expected : " + str(nb_search_result) + " and number of module found : " + str(nb_found))
            else:
                Context().logger.warning("No module found with the following search : " + var_test.get('search_name'))
            
            return my_search_grid

        if var_test.get('view') == "list" :    

            ui.click(self._objects['list_view'])
            nb_modules=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
            i=1
            all_modules = []
            while i<=nb_modules:
                try:
                    def_module = ui.def_object(self._objects['list_module_first'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                except:
                    def_module = ui.def_object(self._objects['list_module'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                all_modules.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                i=i+1;
            
            my_search_list = False
            ui.set_text(self._objects['search'], var_test.get('search_name'))
            my_elem = ui.find_element(self._objects['search'][0],self._objects['search'][1])
            time.sleep(2)
            my_elem.send_keys(Keys.ENTER)
            nb_search_result=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
            if nb_search_result > 0 :
                nb_found=0
                for modules_search in all_modules:
                    if var_test.get('search_name').lower() in modules_search[0].lower() or var_test.get('search_name').lower() in modules_search[1].lower() or var_test.get('search_name').lower() in modules_search[2].lower():
                        nb_found = nb_found +1 
                if nb_search_result == nb_found :
                    i=1
                    check_search = 0
                    order_module = []
                    while i<=nb_search_result:
                        def_module = ui.def_object(self._objects['list_module'], i)
                        my_module = ui.find_element(def_module[0],def_module[1])
                        check_module = {} 
                        order_module.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price')))
                        check_module['data-name']=my_module.get_attribute('data-name')
                        check_module['data-description']=my_module.get_attribute('data-description')
                        check_module['data-author']=my_module.get_attribute('data-author')
                        
                        for var in check_module:
                            if var_test.get('search_name').lower() in check_module.get(var).lower():
                                check_search = check_search +1 
                                break;
                        i = i+1
                    
                    ui.click(self._objects['cancel_search'])
                    nb_modules2=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])    
                    
                    if check_search == nb_search_result and nb_modules == nb_modules2:
                        my_search_list = True
                    else:
                        Context().logger.error("Modules found by the search not matching with the search : " + var_test.get('search_name'))
                else:
                    Context().logger.error("Number of module found by the search is wrong. Number of module expected : " + str(nb_search_result) + " and number of module found : " + str(nb_found))
            else:
                Context().logger.warning("No module found with the following search : " + var_test.get('search_name'))

            
            #Go to installed modules and make a search
            try:
                ui.click(self._objects['tab_installed_modules'])
                
                i=1
                    
                def_module = ui.def_object(self._objects['installed_list_first_module'], i)
                first_installed_module = ui.find_element(def_module[0],def_module[1])
                
                check_module = {}
                check_module['data-name']=first_installed_module.get_attribute('data-name')
                check_module['data-description']=first_installed_module.get_attribute('data-description')
                check_module['data-author']=first_installed_module.get_attribute('data-author')
                check_module['data-tech-name']=first_installed_module.get_attribute('data-tech-name')
        
        
                ui.set_text(self._objects['search'], check_module.get('data-tech-name'))
                my_elem = ui.find_element(self._objects['search'][0],self._objects['search'][1])
                time.sleep(2)
                my_elem.send_keys(Keys.ENTER)
        
                found_module = ui.find_element(def_module[0],def_module[1])
                Test.assert_equals(check_module.get('data-name'), found_module.get_attribute('data-name'), "'name' not matching", "'name' is ok")
                Test.assert_equals(check_module.get('data-description'), found_module.get_attribute('data-description'), "'description' not matching", "'description' is ok")
                Test.assert_equals(check_module.get('data-author'),found_module.get_attribute('data-author'), "'author' not matching", "'authore' is ok")
                Test.assert_equals(check_module.get('data-tech-name'), found_module.get_attribute('data-tech-name'), "'data-tech-name' not matching", "'data-tech-name' is ok")
                
                ui.click(self._objects['cancel_search'])
            except:
                    my_search_list = False
                    ui.click(self._objects['cancel_search'])
                    raise
        
            return my_search_list
 
     
    def check_categorie(self,var_test):
        my_check_block = False
        """
        try:
                ui.click(("css","a.hide-button"), test=True)
        except:
            None
        """    
            
        if var_test.get('view') == "grid" : 
            ui.click(self._objects['grid_view'])
            nb_modules=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
            i=1
            all_modules = []
            while i<=nb_modules:
                try:
                    def_module = ui.def_object(self._objects['block_module_first'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                except:
                    def_module = ui.def_object(self._objects['block_module'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                all_modules.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                i=i+1;
            ui.click(self._objects['list_categories'])    
            all_categories=ui.find_elements(self._objects['name_categories'][0],self._objects['name_categories'][1])
            ui.click(self._objects['list_categories']) 
            j=0
            total=0
            for cat in all_categories:
                my_categorie=ui.def_object(self._objects['categorie'],j+1)
                ui.click(self._objects['list_categories']) 
                ui.click(my_categorie)
                ui.click(self._objects['cancel_search'])
                nb_result=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
                nb_found=0
                for modules_search in all_modules:
                    if modules_search[4] == cat.get_attribute('data-categories'):
                        nb_found = nb_found +1 
    
                if nb_found!=nb_result:
                    Context().logger.error("Issue to find the right modules for the category: " + cat.get_attribute('data-categories') + ", nb result filtered = " + str(nb_result) + " and nb found module = " + str(nb_found))
                else:
                    total=total+nb_found
                j=j+1   
             
            ui.click(self._objects['list_categories'])    
            ui.click(self._objects['rest_category_filter'])
                         
            
            if total == nb_modules:
                my_check_block = True
                
            return my_check_block
     
        if var_test.get('view') == "list" :
            ui.click(self._objects['list_view'])
            my_check_list = False
            nb_modules=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
            i=1
            all_modules = []
            while i<=nb_modules:
                try:
                    def_module = ui.def_object(self._objects['list_module_first'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                except:
                    def_module = ui.def_object(self._objects['list_module'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                all_modules.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                i=i+1;
            ui.click(self._objects['list_categories'])    
            all_categories=ui.find_elements(self._objects['name_categories'][0],self._objects['name_categories'][1])
            ui.click(self._objects['list_categories']) 
            j=0
            total=0
            for cat in all_categories:
                my_categorie=ui.def_object(self._objects['categorie'],j+1)
                ui.click(self._objects['list_categories']) 
                ui.click(my_categorie)
                ui.click(self._objects['cancel_search'])
                nb_result=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
                nb_found=0
                for modules_search in all_modules:
                    if modules_search[4] == cat.get_attribute('data-categories'):
                        nb_found = nb_found +1 
    
                if nb_found!=nb_result:
                    Context().logger.error("Issue to find the right modules for the category: " + cat.get_attribute('data-categories') + ", nb result filtered = " + str(nb_result) + " and nb found module = " + str(nb_found))
                else:
                    total=total+nb_found
                j=j+1   
                
            if total == nb_modules:
                my_check_list = True
            
            return my_check_list
 
    
    def sort_modules(self,var_test):
        """
        TODO:
        faire la seletion du tri par la position dans la liste et nom sa valeur (pb en changeant de langue)
        """ 
        
        if var_test.get('view') == "grid" : 
            my_order_grid = True
            """try:
                    ui.click(("css","a.hide-button"), test=True)
            except:
                None
            """
            nb_modules=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
            i=1
            all_modules = []
            while i<=nb_modules:
                try:
                    def_module = ui.def_object(self._objects['block_module_first'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                except:
                    def_module = ui.def_object(self._objects['block_module'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                if my_module.get_attribute('data-name') != "":
                    all_modules.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                else:
                    all_modules.append((my_module.get_attribute('data-tech-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                i=i+1;
            sort_type=[('name',0),('price',3),('price-desc',3)]
            for my_sort in sort_type:
                sort_def = ui.def_object(self._objects['sort_type'], my_sort[0])
                ui.click(sort_def)
                time.sleep(2)
                if "price" in my_sort[0]:
                    j=1
                    old_module_price = ""
                    while j<=nb_modules:
                        try:
                            def_module = ui.def_object(self._objects['block_module_first'], j)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        except:
                            try:
                                def_module = ui.def_object(self._objects['block_module'], j+1)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            except:
                                my_order_grid = False
                                raise
                        if old_module_price == "":
                            old_module_price = my_module.get_attribute('data-price')
                        if "desc" in my_sort[0]:
                            try:
                                Test.assert_less_or_equal(float(old_module_price), float(my_module.get_attribute('data-price')), "order " + my_sort[0] + " is not correct", "order " + my_sort[0] + " is correct ,,,, values: " + str(old_module_price) + "//" + str(my_module.get_attribute('data-price')))
                                old_module_price = my_module.get_attribute('data-price')
                            except:
                                my_order_grid = False
                                raise   
                        else:
                            try:
                                Test.assert_more_or_equal(float(old_module_price), float(my_module.get_attribute('data-price')), "order " + my_sort[0] + " is not correct", "order " + my_sort[0] + " is correct ,,,, values: " + str(old_module_price) + "//" + str(my_module.get_attribute('data-price')))
                                old_module_price = my_module.get_attribute('data-price')
                            except:
                                my_order_grid = False
                                raise   
                        j=j+1;    
                else:
                    all_modules = sorted(all_modules, key=lambda colonnes: colonnes[int(my_sort[1])].lower())
                    i=0
                    while i<nb_modules:
                        try:
                            def_module = ui.def_object(self._objects['block_module_first'], i+1)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        except:
                            try:
                                def_module = ui.def_object(self._objects['block_module'], i+1)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            except:
                                my_order_grid = False
                                raise
                        if my_module.get_attribute('data-name') != "":
                            try:
                                Test.assert_equals(all_modules[i][0], my_module.get_attribute('data-name'), "'name' not matching", "'name' is ok")
                                Test.assert_equals(all_modules[i][1], my_module.get_attribute('data-description'), "'description' not matching", "'description' is ok")
                                Test.assert_equals(all_modules[i][2], my_module.get_attribute('data-author'), "'author' not matching", "'author' is ok")
                                Test.assert_equals(all_modules[i][3], my_module.get_attribute('data-price'), "'price' not matching", "'price' is ok")
                            except:
                                Context().logger.error("Issue with the order function")
                                my_order_grid = False
                                raise
                        else:
                            Test.assert_equals(all_modules[i][0], my_module.get_attribute('data-tech-name'), "'name' not matching", "'name' is ok")
                        i = i+1
            
            return my_order_grid
            
        if var_test.get('view') == "list" : 
            my_order_list = True
            """
            try:
                    ui.click(("css","a.hide-button"), test=True)
            except:
                None
            """    
            ui.click(self._objects['list_view']) 
            nb_modules=int(ui.get_text(self._objects['nb_result_search']).split(" ")[0])
            i=1
            all_modules = []
            while i<=nb_modules:
                try:
                    def_module = ui.def_object(self._objects['list_module_first'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                except:
                    def_module = ui.def_object(self._objects['list_module'], i)
                    my_module = ui.find_element(def_module[0],def_module[1])
                if my_module.get_attribute('data-name') != "":
                    all_modules.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                else:
                    all_modules.append((my_module.get_attribute('data-tech-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                i=i+1;
            sort_type=[('name',0),('price',3),('price-desc',3)]
            for my_sort in sort_type:
                sort_def = ui.def_object(self._objects['sort_type'], my_sort[0])
                ui.click(sort_def)
                time.sleep(2)
                if "price" in my_sort[0]:
                    j=1
                    old_module_price = ""
                    while j<=nb_modules:
                        try:
                            def_module = ui.def_object(self._objects['list_module_first'], j)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        except:
                            try:
                                def_module = ui.def_object(self._objects['list_module'], j+1)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            except:
                                my_order_list = False
                                raise
                        if old_module_price == "":
                            old_module_price = my_module.get_attribute('data-price')
                        if "desc" in my_sort[0]:
                            try:
                                Test.assert_less_or_equal(float(old_module_price), float(my_module.get_attribute('data-price')), "order " + my_sort[0] + " is not correct", "order " + my_sort[0] + " is correct ,,,, values: " + str(old_module_price) + "//" + str(my_module.get_attribute('data-price')))
                                old_module_price = my_module.get_attribute('data-price')
                            except:
                                my_order_list = False
                                raise   
                        else:
                            try:
                                Test.assert_more_or_equal(float(old_module_price), float(my_module.get_attribute('data-price')), "order " + my_sort[0] + " is not correct", "order " + my_sort[0] + " is correct ,,,, values: " + str(old_module_price) + "//" + str(my_module.get_attribute('data-price')))
                                old_module_price = my_module.get_attribute('data-price')
                            except:
                                my_order_list = False
                                raise   
                        j=j+1;    
                else:
                    all_modules = sorted(all_modules, key=lambda colonnes: colonnes[int(my_sort[1])].lower())
                    i=0
                    while i<nb_modules:
                        try:
                            def_module = ui.def_object(self._objects['list_module_first'], i+1)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        except:
                            try:
                                def_module = ui.def_object(self._objects['list_module'], i+1)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            except:
                                my_order_list = False
                                raise
                        if my_module.get_attribute('data-name') != "":
                            try:
                                Test.assert_equals(all_modules[i][0], my_module.get_attribute('data-name'), "'name' not matching", "'name' is ok")
                                Test.assert_equals(all_modules[i][1], my_module.get_attribute('data-description'), "'description' not matching", "'description' is ok")
                                Test.assert_equals(all_modules[i][2], my_module.get_attribute('data-author'), "'author' not matching", "'author' is ok")
                                Test.assert_equals(all_modules[i][3], my_module.get_attribute('data-price'), "'price' not matching", "'price' is ok")
                            except:
                                Context().logger.error("Issue with the order function")
                                my_order_grid = False
                                raise
                        else:
                            Test.assert_equals(all_modules[i][0], my_module.get_attribute('data-tech-name'), "'name' not matching", "'name' is ok")
                        i = i+1
        
        
            #Go to installed modules and make a sort by name
            #my_order_list = True
            try:
                #ui.wait_until(self._objects['tab_installed_modules'], 60, 1)
                ui.click(self._objects['tab_installed_modules'])
                
                #save of installed modules
                def_object = ui.def_object(self._objects['installed_modules_nb_result_search'], 1)
                number_of_modules = int(ui.get_text((def_object[0],def_object[1])).split(" ")[0])
                
                if (number_of_modules > 1): 
                    
                    all_installed_modules = []
                    for i in range (1, number_of_modules+1): 
                        try:
                            def_module = ui.def_object(self._objects['installed_list_module_first'], 1)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        except:
                            def_module = ui.def_object(self._objects['installed_list_module'], 1, i)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        if my_module.get_attribute('data-name') != "":
                            all_installed_modules.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                        else:
                            all_installed_modules.append((my_module.get_attribute('data-tech-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                        i = i+1;
                
                #save of built-in modules
                def_object2 = ui.def_object(self._objects['installed_modules_nb_result_search'], 2)
                number_of_modules2 = int(ui.get_text((def_object2[0],def_object2[1])).split(" ")[0])
                
                if (number_of_modules2 > 1): 
                    
                    all_built_in_modules = []
                    for j in range (1, number_of_modules2+1): 
                        try:
                            def_module = ui.def_object(self._objects['installed_list_module_first'], 2)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        except:
                            def_module = ui.def_object(self._objects['installed_list_module'], 2, j)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        if my_module.get_attribute('data-name') != "":
                            all_built_in_modules.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                        else:
                            all_built_in_modules.append((my_module.get_attribute('data-tech-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                        j = j+1;
                        
                #save of theme modules
                def_object3 = ui.def_object(self._objects['installed_modules_nb_result_search'], 3)
                number_of_modules3 = int(ui.get_text((def_object3[0],def_object3[1])).split(" ")[0])
                
                if (number_of_modules3 > 1): 
                    
                    all_theme_modules = []
                    for k in range (1, number_of_modules3+1): 
                        try:
                            def_module = ui.def_object(self._objects['installed_list_module_first'], 3)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        except:
                            def_module = ui.def_object(self._objects['installed_list_module'], 3, k)
                            my_module = ui.find_element(def_module[0],def_module[1])
                        if my_module.get_attribute('data-name') != "":
                            all_theme_modules.append((my_module.get_attribute('data-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                        else:
                            all_theme_modules.append((my_module.get_attribute('data-tech-name'),my_module.get_attribute('data-description'),my_module.get_attribute('data-author'),my_module.get_attribute('data-price'),my_module.get_attribute('data-categories')))
                        k = k+1;        
                        
                my_sort = ui.def_object(self._objects['sort_type'], 'name')
                ui.click(my_sort)
                for a in range(1,4):
                    #installed modules
                    if (number_of_modules > 1): 
                        
                        all_installed_modules = sorted(all_installed_modules, key=lambda colonnes: colonnes[0].lower())
                        for i in range (1, number_of_modules): 
                            try:
                                def_module = ui.def_object(self._objects['installed_list_module_first'], 1)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            except:
                                def_module = ui.def_object(self._objects['installed_list_module'], 1, i)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            if my_module.get_attribute('data-name') != "":
                                Test.assert_equals(all_installed_modules[i-1][0], my_module.get_attribute('data-name'), "'name' not matching", "'name' is ok")
                            else:
                                Test.assert_equals(all_installed_modules[i-1][0], my_module.get_attribute('data-tech-name'), "'name' not matching", "'name' is ok")
                            i = i+1;
                            
                            
                            
                    #built-in modules
                    if (number_of_modules2 > 1): 
                        
                        all_built_in_modules = sorted(all_built_in_modules, key=lambda colonnes: colonnes[0].lower())
                        for j in range (1, number_of_modules2): 
                            try:
                                def_module = ui.def_object(self._objects['installed_list_module_first'], 2)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            except:
                                def_module = ui.def_object(self._objects['installed_list_module'], 2, j)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            if my_module.get_attribute('data-name') != "":
                                Test.assert_equals(all_built_in_modules[j-1][0], my_module.get_attribute('data-name'), "'name' not matching", "'name' is ok")
                            else:
                                Test.assert_equals(all_built_in_modules[j-1][0], my_module.get_attribute('data-tech-name'), "'name' not matching", "'name' is ok")
                            j = j+1;
                            
                    #theme modules
                    if (number_of_modules3 > 1): 
                        
                        all_theme_modules = sorted(all_theme_modules, key=lambda colonnes: colonnes[0].lower())
                        for k in range (1, number_of_modules3): 
                            try:
                                def_module = ui.def_object(self._objects['installed_list_module_first'], 3)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            except:
                                def_module = ui.def_object(self._objects['installed_list_module'], 3, k)
                                my_module = ui.find_element(def_module[0],def_module[1])
                            if my_module.get_attribute('data-name') != "":
                                Test.assert_equals(all_theme_modules[k-1][0], my_module.get_attribute('data-name'), "'name' not matching", "'name' is ok")
                            else:
                                Test.assert_equals(all_theme_modules[k-1][0], my_module.get_attribute('data-tech-name'), "'name' not matching", "'name' is ok")
                            k = k+1;        
            except:
                    my_order_list = False
                    raise

            return my_order_list

