1)	Installation
Pour utiliser les tests Python vous avez besoin d�installer :
-	Python (version 3)
-	pip

Les modules n�cessaires � installer via pip sont :
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

Se placer dans le dossier contenant l�automate et ex�cuter :

python runner.py --environment ADMINDEV --dataset modules -f search_module --browser Chrome --vm 192.168.8.205 --storename 1.7.0.0 --log-level INFO --version-presta

-	environment : d�fini l�environment de tests, � savoir l�url de la boutique, le login / password pour le Back Office et si le mode "dev" est � true ou false. (si le mode dev est � true = ADMINDEV, sinon ADMIN)
-	dataset : d�fini quel dataset on souhaite utiliser
-	function : non obligatoire, d�fini la fonction du dataset que l�on souhaite tester. Si cette valeur n�est pas mise, on testera toutes les fonctions du dataset (supprimer � -f search_module� de l�url d�appel)
-	browser : d�fini quel browser on souhaite utiliser pour les tests (Chrome, Firefox ou IE)
-	vm : d�fini l�url de la vm surlaquelle se trouve le site. Si le code et le site sont sur la m�me machine, ne pas mettre cette option (par d�faut c�est � localhost � qui sera utilis�)
-	version-presta : d�fini la version de prestashop qui est utilis�e
-   storename : Nom de la boutique cot� BO et FO
-	log-level : d�fini le niveau de log que l�on souhaite voir apparaitre.
