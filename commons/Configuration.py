import os
from commons.singleton import singleton
from argparse import ArgumentParser
from configparser import SafeConfigParser

@singleton
class Configuration(object):

    def __init__(self, test_conf_token, is_cli=True, folder=""):
        self._environment_file_path = None
        self._project_path = None
        self._jenkins_path = None
        self._browser = None
        self._environment = None
        self._language = None
        self._datasets_file_name = None
        self._log_level = None
        self._function_test = None
        self._timeout = None
        self._root_folder = folder
        self._status = "ALL"
        self._log_status = None
        self._job_jenkins = None
        self._build_jenkins = None
        self._fct_test = None
        self._storename = None
        self._back = None
        self._version_presta = None
        self._security = None
        self._git = None
        self._git_repo = None
        self._vm = None
        self._test_conf_token = test_conf_token
        self._read_conf()
        if is_cli:
            self._read_cli()

          
    def _read_conf(self):
        """
        @summary: read the conf.cfg file (in conf folder) to store the values
        """
        parser = SafeConfigParser()
        parser.read(os.path.join(self._root_folder, "conf", "global.cfg"))
        self._environment_file_path = os.path.join(self._root_folder, *parser.get("paths", "environment_file_path").split('/'))
        self._project_path = os.path.join(self._root_folder, *parser.get("paths", "project_path").split('/'))
        self._browser = parser.get(self._test_conf_token, 'browser')
        self._version_presta = parser.get(self._test_conf_token, 'version_presta')
        self._log_level = parser.get(self._test_conf_token, 'log_level')
        self._git_repo = parser.get(self._test_conf_token, 'git_repo')

    def _read_cli(self):
        """
        @summary: read the parameters in the command line execution
        """
        cli_parser = ArgumentParser()
        group = cli_parser.add_argument_group()
        group.add_argument("-b", "--browser", help="Specify the browser name {Firefox|IE|Chrome}", type=str)
        group.add_argument("-e", "--environment", help="Name of the environment as defined in environment.xml", type=str)
        group.add_argument("-l", "--language", help="language of the environment", type=str)
        group.add_argument("-s", "--scope", help="Which scope to run (smoketest, MAT, regression, cleanup)", type=str)
        group.add_argument("-d", "--datasets-file-name", help="First part of the name of the py datasets file, separated by a space (ex.: banner, message)", nargs="+", type=str)
        group.add_argument("--log-level", help="Test log level", type=str)
        group.add_argument("-t", "--stability-threshold", help="Percent of failed tests under which they are rerun", type=int)
        group.add_argument("-r", "--record", help="connect to the local vnc server to record test", type=str, default="none")
        group.add_argument("-f", "--function-test", help="The name of the test function", type=str)
        group.add_argument("--timeout", help="Kill the test after x minutes", type=int)
        group.add_argument("--status", help="Only run the tests with the specified status", type=str)
        group.add_argument("--log-status", help="log status of execution for reporting", action="store_true")
        group.add_argument("--job-jenkins", help="name of the jenkins job launching the test", type=str)
        group.add_argument("--build-jenkins", help="number of the jenkins build", type=str)
        group.add_argument("-sn", "--storename", help="Specify the version of the store", type=str)
        group.add_argument("--back", help="tests should be back end only", action="store_true")
        group.add_argument("-vp", "--version-presta", help="Specify the version PrestaShop", type=str)
        group.add_argument("--security", help="Go through a proxy and launch scanning", action="store_true")
        group.add_argument("--git", help="Use it to indicate the installation of presta site comes of git", action="store_true")
        group.add_argument("-gr", "--git-repo", help="Specify the version PrestaShop", type=str)
        group.add_argument("-vm", "--vm", help="Specify we use a vm or the localhost", type=str)
        
        cli_args = cli_parser.parse_args()

        self._browser = cli_args.browser if cli_args.browser and cli_args.browser != "" else self._browser
        self._environment = cli_args.environment if cli_args.environment and cli_args.environment != "" else self._environment
        self._language = cli_args.language if cli_args.language and cli_args.language != "" else self._language
        self._datasets_file_name = cli_args.datasets_file_name if cli_args.datasets_file_name and cli_args.datasets_file_name != "" else self._datasets_file_name
        self._log_level = cli_args.log_level if cli_args.log_level and cli_args.log_level != "" else self._log_level
        self._function_test = cli_args.function_test if cli_args.function_test and cli_args.function_test != "" else self._function_test
        self._timeout = cli_args.timeout if cli_args.timeout and cli_args.timeout != "" else self._timeout
        self._log_status = cli_args.log_status
        self._status = cli_args.status.upper() if cli_args.status and cli_args.status != "" else self._status
        self._job_jenkins = cli_args.job_jenkins
        self._build_jenkins = cli_args.build_jenkins
        self._storename = cli_args.storename if cli_args.storename and cli_args.storename != "" else self._storename
        self._back = cli_args.back
        self._version_presta = cli_args.version_presta if cli_args.version_presta and cli_args.version_presta != "" else self._version_presta
        self._security = cli_args.security
        self._git = cli_args.git
        self._git_repo = cli_args.git_repo if cli_args.git_repo and cli_args.git_repo != "" else self._git_repo
        self._vm = cli_args.vm
        self._store_name = cli_args.storename
        
    def test_match(self, test_function):
        val = True
        if self._function_test is not None:
            if self._function_test.lower() != str(test_function.__name__).lower():
                val = False
        return val

    @property
    def environment_file_path(self):
        return self._environment_file_path

    @environment_file_path.setter
    def environment_file_path(self, value):
        self._environment_file_path = value

    @property
    def project_path(self):
        return self._project_path

    @project_path.setter
    def project_path(self, value):
        self._project_path = value

    @property
    def jenkins_path(self):
        return self._jenkins_path

    @jenkins_path.setter
    def jenkins_path(self, value):
        self._jenkins_path = value

    @property
    def misc_path(self):
        return self._misc_path

    @property
    def browser(self):
        return self._browser

    @browser.setter
    def browser(self, value):
        self._browser = value

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, value):
        self._environment = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

    @property
    def datasets_file_name(self):
        return self._datasets_file_name

    @datasets_file_name.setter
    def datasets_file_name(self, value):
        self._datasets_file_name = value

    @property
    def log_level(self):
        return self._log_level

    @log_level.setter
    def log_level(self, value):
        self._log_level = value

    @property
    def function_test(self):
        return self._function_test

    @function_test.setter
    def function_test(self, value):
        self._function_test = value

    @property
    def timeout(self):
        return self._timeout

    @property
    def root_folder(self):
        return self._root_folder

    @property
    def status(self):
        return self._status

    @property
    def log_status(self):
        return self._log_status

    @property
    def job_jenkins(self):
        return self._job_jenkins

    @property
    def build_jenkins(self):
        return self._build_jenkins

    @property
    def storename(self):
        return self._storename

    @storename.setter
    def storename(self, value):
        self._storename = value
        
    @property
    def back(self):
        return self._back
    
    @property
    def version_presta(self):
        return self._version_presta

    @version_presta.setter
    def version_presta(self, value):
        self._version_presta = value
        
    @property
    def security(self):
        return self._security
    
    @property
    def git(self):
        return self._git
    
    @property
    def git_repo(self):
        return self._git_repo

    @git_repo.setter
    def git_repo(self, value):
        self._git_repo = value
    
    @property
    def vm(self):
        return self._vm