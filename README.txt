Information : Pour utiliser les tests suivants, vous devez avoir installé une boutique PrestaShop en langue anglaise dans le pays France. (ou alors apporter les modifications nécessaires pour les vérifications, par exemple l’affichage des prix [séparateur « , » ou « . », « € » ou « $ » ou « £ » ou …].
Vous devez également créer l’utilisateur suivant avec les droits SuperAdmin dans le Back Office : 
Login : demo@prestashop
Mot de passe : demo_prestashop


1)	Installation
Pour utiliser les tests Python vous avez besoin d’installer :
-	Python (version 3)
-	pip

Les modules nécessaires à installer via pip sont :
-	cv2
-	logging
-	PyMouse
-	python-dateutil
-	pywinauto
-	selenium
-	six
-	smmap
-	sympy

2)	Lancement des tests

Se placer dans le dossier contenant l’automate et exécuter :

python runner.py --environment ADMINDEV --dataset modules -f search_module --browser Chrome --vm 192.168.8.205 --version-presta 1.7 --storename 1.7.0.0 --log-level INFO

-	environment : défini l’environnement de tests, à savoir l’url de la boutique, le login password pour le Back Office, si le mode dev est activé et l’emplacement du dossier de la boutique
-	dataset : défini quel dataset on souhaite utiliser
-	function : non obligatoire, défini la fonction du dataset que l’on souhaite tester. Si cette valeur n’est pas mise, on testera toutes les fonctions du dataset ‘supprimer « -f search_module» de l’url d’appel
-	Browser : défini quel browser on souhaite utiliser pour les tests (Chrome, Firefox ou IE)
-	vm : défini l’url de la vm sur laquelle se trouve le site. Si le code et le site sont sur la même machine, ne pas mettre cette option, par défaut c’est « localhost » qui sera utilisé)
-	version-presta : numéro de la version de prestashop (exemple : 1.7)
-	storename : nom de la boutique dans l’url du BO et FO
-	log-level : défini le niveau de log que l’on souhaite voir apparaitre.

##############################################################################################################

Information: To use the following test suites, you need to install a PrestaShop in English in country France. (or you may change some assertions like the separator “,” or “.”, “€” or “$” or “£” or …]
You need to create a user in Back Office with SuperAdmin rights and the following information’s:
Login: demo@prestashop
Password: demo_prestashop


1)	Installation
To use Python tests, you need to install:
-	Python (version 3)
-	pip

Required modules to install using pip are:
-	cv2
-	logging
-	PyMouse
-	python-dateutil
-	pywinauto
-	selenium
-	six
-	smmap
-	sympy

2)	How to launch tests

You need to go on your folder with Python tests and execute the following command line :

python runner.py --environment ADMINDEV --dataset modules -f search_module --browser Chrome --vm 192.168.8.205 --version-presta 1.7 --storename 1.7.0.0 --log-level INFO

-	environment: create the environment variable, like Url of your store, login / password you want to use for Back Office, if dev mode is activate and the folder of your store.
-	dataset: select the dataset we want to use for the test
-	function (optional): select the function in the dataset you want to use. If this value is not push in the command line, we will test all the function of the dataset
-	Browser: to select the browser we want to use for the test (Chrome, Firefox ou IE)
-	Vm (optional): Use it if your store is not the same computer of the automate (by default, when this variable is not push in the command line, we use « localhost » to find the store)
-	Version-presta: version of the PrestaShop site (examples: 1.7 or 1.6)
-	storename : Name of your store
-	Log-level: to select which kind of level you want.
