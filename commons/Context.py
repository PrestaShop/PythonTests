# -*- coding: utf-8 -*-

import time
from threading import Timer
from commons.winKeyPress import press_esc
from selenium import webdriver

from commons.Environment import Environment
from commons.logger import Logger
from commons.exceptions import NotKnown
from commons.singleton import singleton
from commons.Configuration import Configuration


@singleton
class Context(object):
    """
    Modelizing the local sandbox for the test
    """
    _test = None
    _browser = None
    _browserName = None
    _chrome_log_file_stdout = None
    _chrome_log_file_stderr = None
    _currentFrame = None
    _environment = None
    _environmentName = None
    _logger = None
    _module = None
    _scenario = None
    _implicit_wait = 20

    def __init__(self):
        """
        @param test: an instance of commons.Test
        """
        self._configuration = Configuration()
        if self._logger is None:
            self._logger = Logger(name=__name__,
                                  browser_name=self._configuration.browser,
                                  language=self._configuration.language)
        self._environmentName = self._configuration.environment
        self.generate_environment()
        self._browserName = self._configuration.browser

    def set_implicit_wait_default(self):
        self._browser.implicitly_wait(self._implicit_wait)
          
    def close_chrome_log_files(self):
        self._chrome_log_file_stderr.close()
        self._chrome_log_file_stdout.close()

    def quit_browser(self):
        context = self
        if "IE" in context.browserName:
            timer_stop_IE_crash = Timer(60, press_esc)
            timer_stop_IE_crash.start()
        try:
            context.browser.quit()
        # pylint: disable=W0703
        except Exception as e:
            context.logger.warning("Couldn't close browser : " + str(e))
        if "IE" in context.browserName:
            timer_stop_IE_crash.cancel()
        if context.browserName == "Chrome":
            try:
                import urllib.request as url_request

                url_request.urlopen("http://127.0.0.1:9515/shutdown")
                time.sleep(3)
                context.close_chrome_log_files()
            # pylint: disable=W0703
            except Exception as exc:
                context.logger.warning("Couldn't close chrome webdriver : " + str(exc))
        if context.browserName == "Safari":
            context._seleniumSafari.shut_down_selenium_server()
            time.sleep(3)
            context.close_safari_log_files()

    def generate_environment(self):
        """
        Generate a commons.Environment instance and storing it into _environment
        """
        try:
            if self._environment is None:
                self._environment = Environment.fromfilepath(self._environmentName,
                                                             self._configuration.environment_file_path)
        except Exception:
            raise

    def goto_environment_url(self):
        """
        Pointing the browser to the _environment url (used for login)
        """
        try:
            self._browser.get(self._environment.url)
        except Exception as e:
            self.logger.error("Error going to environment '" + self._environment.url + "' : " + str(e))
            raise

    def goto_url(self, url):
        """
        Pointing the browser to the _environment url (used for login)
        """
        try:
            self._browser.get(url)
        except Exception as e:
            self.logger.error("Error going to url '" + url + "' : " + str(e))
            raise

    def switch_to_frame(self, frames, depth=None):
        """
        @summary: telling the _browser to work inside the frame
        @param frames: array of frame name
        @param depth: int, if the frame does not have a "name" attribute input the desired nesting level of the frame
        @returns None
        """
        if depth is None:
            if not frames[-1] == self._currentFrame:
                for frameName in frames:
                    try:
                        if not frameName == self._currentFrame:
                            if frameName == "main":
                                Context().browser.switch_to_default_content()
                            else:
                                if frameName[0:4] == "#id#":
                                    Context().browser.switch_to_frame(Context().browser.find_elements_by_id(frameName[4:])[0])
                                else:
                                    Context().browser.switch_to_frame(frameName)
                            self._currentFrame = frameName
                    except Exception as e:
                        self.logger.error("Error switching to frame '" + str(frameName) + "' : " + str(e))
                        raise
        else:
            Context().browser.switch_to_default_content()
            for _1 in range(0, depth):
                Context().browser.switch_to_frame(Context().browser.find_elements_by_tag_name("iframe")[0])
            self._currentFrame = "Depth " + str(depth)

    def cookies_header(self):
        cookie_array = []
        for cookie in self._browser.get_cookies():
            cookie_array.append(cookie["name"] + "=" + cookie["value"])
        return {"Cookie": ";".join(cookie_array)}
    
    
    def launch_browser2(self, clean_session=False):
        """
        Instantiating a webdriver given the _browserName
        """
        try:
            if self._browserName[0:2] == "IE":
                if clean_session:
                    self._browser = webdriver.Ie(log_level="TRACE", log_file="iedriver_stdout.log",
                                                 capabilities={'ie.ensureCleanSession': True})
                else:
                    self._browser = webdriver.Ie(log_level="TRACE", log_file="iedriver_stdout.log")
            elif self._browserName == "RemoteIE":
                self._browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                                 desired_capabilities={'browserName': 'internet explorer'})
            elif self._browserName == "RemoteFF":
                self._browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                                 desired_capabilities={'browserName': 'firefox'})
            
            elif self._browserName == "Firefox":
                fp = webdriver.FirefoxProfile()
                fp.set_preference('app.update.auto', False)
                fp.set_preference('app.update.enabled', False)
                fp.native_events_enabled = False
                proxy = None
                if self._configuration.security:
                    self.logger.info("we use a proxy")
                    fp.accept_untrusted_certs = True
                    proxy = webdriver.Proxy()
                    proxy.http_proxy = "localhost:9080"
                    proxy.ssl_proxy = "localhost:9080"
                self._browser = webdriver.Firefox(firefox_profile=fp, proxy=proxy)
            elif self._browserName == "Chrome":
                # dirty way to launch chromedriver as the current webdriver fail after the xth command
                import subprocess

                self._chrome_log_file_stdout = open('chromedriver_stdout.log', 'w')
                self._chrome_log_file_stderr = open('chromedriver_stderr.log', 'w')
                subprocess.Popen("chromedriver", stdout=self._chrome_log_file_stdout,
                                 stderr=self._chrome_log_file_stderr)
                time.sleep(2)
                self._browser = webdriver.Remote('http://localhost:9515', {"nativeEvents": False,
                                                                           "javascriptEnabled": True})
            else:
                raise NotKnown("Unknown browser : " + self._browserName)
            self.set_implicit_wait_default()
            self._browser.maximize_window()
            self._currentFrame = "main"
            self.logger.info("Launching : " + str(self._browserName))
        except Exception as e:
            self.logger.error("Error launching browser : " + str(e))
            raise
        

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, value):
        self._environment = value

    @property
    def browser(self):
        return self._browser

    @browser.setter
    def browser(self, value):
        self._browser = value

    @property
    def browserName(self):
        return self._browserName

    @browserName.setter
    def browserName(self, value):
        self._browserName = value

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value

    @property
    def module(self):
        return self._module

    @module.setter
    def module(self, value):
        self._module = value
        self._logger.module = value

    @property
    def status_logger(self):
        return self._status_logger

    @property
    def configuration(self):
        return self._configuration

    @property
    def currentFrame(self):
        return self._currentFrame

    @currentFrame.setter
    def currentFrame(self, value):
        self._currentFrame = value


