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

python runner.py --environment ADMINDEV --dataset modules -f search_module --browser Chrome --vm 192.168.8.205 --storename 1.7.0.0 --log-level INFO --version-presta

-	environment : défini l’environment de tests, à savoir l’url de la boutique, le login / password pour le Back Office et si le mode "dev" est à true ou false. (si le mode dev est à true = ADMINDEV, sinon ADMIN)
-	dataset : défini quel dataset on souhaite utiliser
-	function : non obligatoire, défini la fonction du dataset que l’on souhaite tester. Si cette valeur n’est pas mise, on testera toutes les fonctions du dataset (supprimer « -f search_module» de l’url d’appel)
-	browser : défini quel browser on souhaite utiliser pour les tests (Chrome, Firefox ou IE)
-	vm : défini l’url de la vm surlaquelle se trouve le site. Si le code et le site sont sur la même machine, ne pas mettre cette option (par défaut c’est « localhost » qui sera utilisé)
-	version-presta : défini la version de prestashop qui est utilisée
-   storename : Nom de la boutique coté BO et FO
-	log-level : défini le niveau de log que l’on souhaite voir apparaitre.
