# -*- coding: utf-8 -*-
import time
import os
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command
from commons.winKeyPress import keyboard_stream, SendInput
from commons.Context import Context
from commons.Configuration import Configuration


def click(element, test=None):
    """
    @summary: click on the element specified
    @param: element: format of element: ('method','identification'), e.g.: ("xpath","//[@id='login']") or ("css","#login") 
    """
    try:
        elem = find_element(element[0], element[1])
        Context().browser.execute_script("window.scrollTo(0, " + str(elem.location['y'] - 150) + ")")
        elem.click()
        Context().logger.debug("Clicking on ({0})".format(element[1]))
    except:
        if test == None:
            Context().logger.error("Cannot click on the element ({0})".format(element[1]))
            take_screenshot("Exception.png")
        else:
            Context().logger.debug("Cannot click on the element ({0})".format(element[1]))
        raise


def click_with_offset(browser, element, xoff=0, yoff=0):
    chains = ActionChains(browser)
    chains.move_to_element_with_offset(element, xoff, yoff).click().perform()


def click_submenu(parent, element):
    """
    @summary: click on the sub-element specified of the parent specified
    @param: parent: format of parent: ('method','identification'), e.g.: ("xpath","//[@id='login']") or ("css","#login")
    @param: element: format of element: ('method','identification'), e.g.: ("xpath","//[@id='login']") or ("css","#login")
    """
    try:
        """
        parent_elem = find_element(parent[0], parent[1])
        mov = ActionChains(Context().browser).move_to_element(parent_elem)
        mov.perform()
        wait_until(element[1],120,1,element[0])
        elem = find_element(element[0], element[1])
        elem.click()
        Context().logger.debug("Clicking on ({0})".format(element[1]))
        """
        parent_elem = find_element(parent[0], parent[1])
        parent_elem.click()
        wait_until(element[1], 120, 1, element[0])
        elem = find_element(element[0], element[1])
        elem.click()
        Context().logger.debug("Clicking on ({0})".format(element[1]))
    except:
        Context().logger.error("Cannot click on the element ({0})".format(element[1]))
        take_screenshot("Exception.png")
        raise

def click_submenu_by_move(parent, element):
    """
    @summary: click on the sub-element specified of the parent specified
    @param: parent: format of parent: ('method','identification'), e.g.: ("xpath","//[@id='login']") or ("css","#login")
    @param: element: format of element: ('method','identification'), e.g.: ("xpath","//[@id='login']") or ("css","#login")
    """
    try:
        parent_elem = find_element(parent[0], parent[1])
        mov = ActionChains(Context().browser).move_to_element(parent_elem)
        mov.perform()
        time.sleep(3)
        wait_until(element[1],120,1,element[0])
        elem = find_element(element[0], element[1])
        elem.click()
        Context().logger.debug("Clicking on ({0})".format(element[1]))

    except:
        Context().logger.error("Cannot click on the element ({0})".format(element[1]))
        take_screenshot("Exception.png")
        raise


def set_text(element, value, clear=None):
    """
    @summary: fill the specified element with the value in parameter
    @param: element: format of element: ('method','identification'), e.g.: ("xpath","//[@id='login']") or ("css","#login")
    @param: value: value that you want to put in the element
    """
    if value != "":
        try:
            elem = find_element(element[0], element[1])
            if clear == True:
                elem.clear()
            if type(value) != int:
                if value.startswith('#') and value.endswith('#'):
                    from commons.Dataset import Dataset
                    value = Dataset().helper_eval(value)
            elem.send_keys(value)
            Context().logger.debug("Filled the element ({0}) with ({1})".format(element[1], value))
        except:
            Context().logger.error("Cannot fill the element ({0}) with ({1})".format(element[1], value))
            take_screenshot("Exception.png")
            raise


def set_text_script(element, value):
    """
    @summary: fill the specified element with the value in parameter by a script
    @param: element: format of element: ('method','identification'), e.g.: ("xpath","//[@id='login']") or ("css","#login")
    @param: value: value that you want to put in the element
    """
    if value != "":
        try:
            elem = find_element(element[0], element[1])
            Context().browser.execute_script("arguments[0].value = '" + value + "';", elem)
            Context().logger.debug("Filled the element ({0}) with ({1})".format(element[1], value))
        except:
            Context().logger.error("Cannot fill the element ({0}) with ({1})".format(element[1], value))
            take_screenshot("Exception.png")
            raise


def native_set_text(element, text):
    """
    @summary: type a string using the OS native events
    @param: element: format of element: ('method','identification'), e.g.: ("xpath","//[@id='login']") or ("css","#login")
    @param: text: str, the text to type
    """
    if text != "":
        try:
            elem = find_element(element[0], element[1])
            elem.click()
        except:
            Context().logger.error("Cannot click on the element ({0})".format(element[1]))
            take_screenshot("Exception.png")
            raise
        stream = keyboard_stream(text)
        try:
            for val in stream:
                SendInput(val)
            Context().logger.debug("Filled the element ({0}) with ({1})".format(element[1], text))
        except:
            Context().logger.error("Cannot fill the element ({0}) with ({1})".format(element[1], text))
            take_screenshot("Exception.png")


def find_element(method, element, not_log=False):
    """
    @summary: find an element with the method and element's information given in the parameter of the function
    @param: method: xpath or css
    @param: element: format of element, e.g.: "//[@id='login']" or "#login"
    """
    try:
        elet = ""
        if method == "xpath":
            elet = Context().browser.find_element_by_xpath(element)
        elif method == "css":
            elet = Context().browser.find_element_by_css_selector(element)
        return elet
    except:
        if not_log == False:
            Context().logger.error("Cannot find the element ({0})".format(element))
            take_screenshot("Exception.png")
        raise


def is_existant(element):
    try:
        elet = ""
        if element[0] == "xpath":
            elet = Context().browser.find_element_by_xpath(element[1])
        elif element[0] == "css":
            elet = Context().browser.find_element_by_css_selector(element[1])
        return True
    except:
        return False


def is_visible(element):
    try:
        elet = ""
        if element[0] == "xpath":
            elet = Context().browser.find_element_by_xpath(element[1])
        elif element[0] == "css":
            elet = Context().browser.find_element_by_css_selector(element[1])

        if elet.is_displayed():
            return True
        else:
            return False
    except:
        return False


def find_elements(method, element, not_log=False):
    """
    @summary: find an element with the method and element's information given in the parameter of the function
    @param: method: xpath or css
    @param: element: format of element, e.g.: "//[@id='login']" or "#login"
    """
    try:
        elet = ""
        if method == "xpath":
            elet = Context().browser.find_elements_by_xpath(element)
        elif method == "css":
            elet = Context().browser.find_elements_by_css_selector(element)
        return elet
    except:
        if not_log == False:
            Context().logger.error("Cannot find the element ({0})".format(element))
            take_screenshot("Exception.png")
        raise


def get_text(element):
    """
    @summary: find the text of an element
    @param: element: format of element, e.g.: "//[@id='login']" or "#login"
    @return: text of the element
    """
    try:
        elem = find_element(element[0], element[1])
        return elem.text
    except:
        Context().logger.error("cannot find the text element ({0})".format(element[1]))
        take_screenshot("Exception.png")
        raise


def get_class(element):
    """
    @summary: find the class of an element
    @param: element: format of element, e.g.: "//[@id='login']" or "#login"
    @return: class of the element
    """
    try:
        elem = find_element(element[0], element[1])
        return elem.get_attribute("class")
    except:
        Context().logger.error("cannot find the text element ({0})".format(element[1]))
        take_screenshot("Exception.png")
        raise


def get_attribute(element, attribute):
    """
    @summary: find the class of an element
    @param: element: format of element, e.g.: "//[@id='login']" or "#login"
    @return: class of the element
    """
    try:
        elem = find_element(element[0], element[1])
        return elem.get_attribute(attribute)
    except:
        Context().logger.error("cannot find the text element ({0})".format(element[1]))
        take_screenshot("Exception.png")
        raise


def option_selector(element, value):
    """
    @summary: Selects a specific option in a dropdown list
    @param object_list: List of webelements in a dropdown
    @param value: Value to be compared and selected
    """

    dd = find_element(element[0], element[1])

    for i in dd:
        if get_text(i) == str(value):
            return i


def choose_a_dd_value(element, desired_value):
    """
    @summary: Method used to check for occurence of a value in the DD, if not selects a random value.
    @param element: DD items in a list format
    @param desired_value: Value to be searched
    @return: A True flag indicating a successful click
    """
    if desired_value != "":
        found = option_selector(element, desired_value)
        if found is not None:
            try:
                new_element = ("css", found)
                click(new_element)
                Context().logger.debug("Clicking on ({0})".format(new_element))
                return True
            except:
                Context().logger.error("Cannot click on the element ({0})".format(element[1]))
                take_screenshot("Exception.png")
                raise


def def_object(my_object, value, value2=None):
    """
    @summary: replace a variable by the right value (given in the parameters of the function) and create a tuple with of the element
    @param: my_object: the element that needs to be update and transform in a tuple
    @param: value: value you want to insert in the element 'my_object'
    @return: the tuple of the element
    """
    if value2 == None:
        element = (my_object[0] + ":|:" + str(my_object[1]).replace("str(i)", str(value)))
        if type(value) == int:
            element = element.replace("'", "")
        element = tuple(item for item in element.split(':|:') if item.strip())
    else:
        element = (
        my_object[0] + ":|:" + str(my_object[1]).replace("str(i)", str(value)).replace("str(j)", str(value2)))
        if type(value) == int or type(value2) == int:
            element = element.replace("'", "")
        element = tuple(item for item in element.split(':|:') if item.strip())
    return element


def take_screenshot(filename='screenshot.png'):
    """
    @summary: Take a screenshot of the page displayed in the active webdriver instance
    @param filename: str, optional. The name of the file.
    """
    context = Context()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    config = Configuration()
    if config.function_test != None:
        filename = str(config.browser) + "-" + str(config.datasets_file_name).replace("'", "").replace("[", "").replace(
            "]", "") + '-' + str(config.function_test) + '_' + timestamp + '_' + filename
    else:
        filename = str(config.browser) + '-' + str(config.datasets_file_name).replace("'", "").replace("[", "").replace(
            "]", "") + '-' + str(config._fct_test) + '_' + timestamp + '_' + filename
    if Configuration().job_jenkins == None:
        context.browser.save_screenshot(os.path.join('test_results', 'screenshots', filename))
        context.logger.info("Screenshot taken as " + filename)
    else:
        finale_path = "C:\jenkins\workspace\\" + Configuration().job_jenkins + "\Browser\\" + Context().browserName + "\Function\\" + Configuration().function_test + "\\" + Configuration().build_jenkins
        os.makedirs(finale_path, exist_ok=True)
        Context().browser.save_screenshot(os.path.join(finale_path, filename))
        context.logger.info("Screenshot taken as " + finale_path + "\\" + filename)


def upload_file(element, fileUpload, is_submit=False):
    """
    """
    img_selected = os.path.abspath(os.curdir) + "/datasets/" + fileUpload
    elem = find_element(element[0], element[1])
    Context().browser.execute_script('arguments[0].setAttribute("style", "")', elem)
    elem.send_keys(img_selected)
    if is_submit != False:
        elem.submit()


def wait_loader(predicate, timeout_seconds, period=0.25):
    """
    @summary Call repeatedly the predicate until it returns true or timeout_seconds passed.
    @param predicate: a condition, modelized as a callable,  that will valued either as True or False
    @param timeout_seconds: the timeout in second
    @param period: the time to sleep between 2 calls to predicate. Defaults to 0.25s.
    @return True if a call to predicate returned True before timeout_seconds passed, else False
    """
    Context().logger.info("waiting until predicate is true for {end} seconds".format(end=timeout_seconds))
    ultimatum = time.time() + timeout_seconds
    while time.time() < ultimatum:
        Context().logger.debug("checking predicate for wait until : {spent} / {end}".format(
            spent=str(time.time() - (ultimatum - timeout_seconds)), end=timeout_seconds))
        try:
            Context().browser.find_element_by_xpath(predicate).is_displayed()
            Context().logger.info("Loader is display")
        except:
            return True
        time.sleep(period)
    return False


def wait_until(predicate, timeout_seconds, period=0.25, method="xpath"):
    """
    @summary Call repeatedly the predicate until it returns true or timeout_seconds passed.
    @param predicate: a condition, modelized as a callable,  that will valued either as True or False
    @param timeout_seconds: the timeout in second
    @param period: the time to sleep between 2 calls to predicate. Defaults to 0.25s.
    @return True if a call to predicate returned True before timeout_seconds passed, else False
    """
    Context().logger.info("waiting until predicate is true for {end} seconds".format(end=timeout_seconds))
    ultimatum = time.time() + timeout_seconds
    if method == "xpath":
        while time.time() < ultimatum:
            Context().logger.debug("checking predicate for wait until : {spent} / {end}".format(
                spent=str(time.time() - (ultimatum - timeout_seconds)), end=timeout_seconds))
            try:
                Context().browser.find_element_by_xpath(predicate).is_displayed()
                return True
            except:
                None
            time.sleep(period)
    else:
        while time.time() < ultimatum:
            Context().logger.debug("checking predicate for wait until : {spent} / {end}".format(
                spent=str(time.time() - (ultimatum - timeout_seconds)), end=timeout_seconds))
            try:
                Context().browser.find_element_by_css_selector(predicate).is_displayed()
                return True
            except:
                None
            time.sleep(period)
    Context().logger.error("The element {0} is not displayed".format(predicate))
    return False


def scroll(elem, direction):
    """
    Scroll the page
    @param elem: Scrollbar
    @param direction: Directional input
    """
    _dir = {'up': Keys.ARROW_UP,
            'down': Keys.ARROW_DOWN,
            'right': Keys.ARROW_RIGHT,
            'left': Keys.ARROW_LEFT,
            'pagedown': Keys.PAGE_DOWN,
            'pageup': Keys.PAGE_UP,
            'home': Keys.HOME,
            'end': Keys.END,
            'top': Keys.PAGE_UP,
            'home': Keys.HOME,
            'top_page': Keys.BACK_SPACE,
            'enter': Keys.ENTER}
    elem.send_keys(_dir[direction.lower()])


def drag_and_drop(source, xoffset, yoffset):
    actions = []
    if source: actions.append(lambda: Context().browser.execute(Command.MOVE_TO, {'element': source.id}))
    actions.append(lambda: Context().browser.execute(Command.MOUSE_DOWN, {}))
    actions.append(
        lambda: Context().browser.execute(Command.MOVE_TO, {'xoffset': int(xoffset), 'yoffset': int(yoffset)}))
    actions.append(lambda: Context().browser.execute(Command.MOUSE_UP, {}))
    for action in actions:
        action()
    return actions


def checkbox(element, status_wanted):
    """
    @summary: click on the element specified
    @param: element: format of element: ('method','identification'), e.g.: ("xpath","//[@id='login']") or ("css","#login") 
    """
    try:
        if status_wanted == "1":
            status_wanted = "true"
            status_log = "Check"
        else:
            status_wanted = "None"
            status_log = "Uncheck"
        elem = find_element(element[0], element[1])
        status = get_attribute(element, "checked")
        if str(status) != status_wanted:
            Context().browser.execute_script("window.scrollTo(0, " + str(elem.location['y'] - 150) + ")")
            elem.click()
            Context().logger.debug(status_log + "({0})".format(element[1]))
    except:
        Context().logger.error("Cannot check/uncheck the element ({0})".format(element[1]))
        take_screenshot("Exception.png")
        raise