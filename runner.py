from commons.Context import Context 
from commons.Configuration import Configuration
import json


if __name__ == '__main__':
    #Reading the conf & cli args
    test_conf_token = 'test'
    configuration = Configuration(test_conf_token)



def main_function():
    """
    @summary: function to run the test specified in the command line wioth the good parameters
    """
    config = Configuration() #va lire le fichier global.cfg dans dossier conf et les variable passees dans la ligne de commande)
    
    for file_name in config.datasets_file_name: #parcours les dataset pour trouver le bon et recuperer les donnees
        if file_name != "":
            json_data=open("datasets/" + file_name + ".json")
            datas = json.load(json_data)
            relaunch = []
            final_status = True
            for data in datas:
                if data['function'] == config.function_test or config.function_test == None:
                    test_status = False
                    my_line = (data['page'] + "||" + data['function']  + "||" + data['log']).split('||')
                
                    if config.function_test == None:
                        config._fct_test = my_line[1]
                    my_test = __import__('tests.' + my_line[0])
                    test_file = getattr(my_test, my_line[0])
                    test_class = getattr(test_file, my_line[0])
                    test_fct = getattr(test_class(),my_line[1])
                    var_exist = 0
                    if  data['variables'] is not None:
                        my_var_test = {}
                        try:
                            for my_key,my_value in data['variables'][0].items():
                                my_var_test[my_key] = my_value
                                var_exist = 1
                        except:
                            Context().logger.failure("Issue store variables for the test")
                    try:
                        if config.back == False:
                            Context().launch_browser2(clean_session=True)
                        try:
                            if config.back == False:
                                if Configuration().vm == None: 
                                    url = Context().environment.url.replace('str(i)',Configuration().storename).replace('str(j)','localhost')
                                else:
                                    url = Context().environment.url.replace('str(i)',Configuration().storename).replace('str(j)',Configuration().vm)
                                Context().goto_url(url)
                            if var_exist == 1:
                                test_status_save = test_status
                                test_status = test_fct(my_var_test)
                            else:
                                test_status_save = test_status
                                test_status = test_fct()
                        except:
                            pass
                    except:
                        Context().logger.error("Issue to find the specified browser")
                    Context().quit_browser()
                    if test_status == True:
                        Context().logger.success("Test OK for ({0})".format(my_line[2]))
                    else:
                        Context().logger.failure("Test KO for ({0})".format(my_line[2]))
                        if data not in relaunch:
                            datas.append(data)
                            relaunch.append(data)
                            test_status = test_status_save
                            Context().logger.failure("Test ({0}) failed for the first time, we will relaunch it".format(my_line[2]))
                        else :
                                final_status = False
            if final_status == False:
                import sys
                sys.exit(1) 


if __name__ == '__main__':
    main_function()

