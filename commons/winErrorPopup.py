def close_driver_popups():
    import win32gui
    import pymouse
    import time

    def _MyCallback(hwnd, extra):
        extra.append(hwnd)

    windows = []
    win32gui.EnumWindows(_MyCallback, windows)
    popups_ie = [window for window in windows if win32gui.GetWindowText(window) == "Command line server for the IE driver"]
    popups_python = [window for window in windows if win32gui.GetWindowText(window) == "python.exe"]
    popups_chrome = [window for window in windows if win32gui.GetWindowText(window) == "chromedriver.exe"]
    popups_ie_2 = [window for window in windows if win32gui.GetWindowText(window) == "Internet Explorer"]
    popups_ff_plugin = [window for window in windows if win32gui.GetWindowText(window) == "Plugin Container for " \
                                                                                          "Firefox"]

    def close_popups(popups):
        for popup in popups:
            elem_popup = []
            win32gui.EnumChildWindows(popup, _MyCallback, elem_popup)
            close = [window for window in elem_popup if win32gui.GetWindowText(window) == "Close the program"]
            try:
                rect = win32gui.GetWindowRect(close[0])
                pymouse.PyMouse().click(rect[0] + 10, rect[1] + 10)
            except:
                win32gui.CloseWindow(popup)
            time.sleep(2)

    close_popups(popups_ie)
    close_popups(popups_ie_2)
    close_popups(popups_chrome)
    close_popups(popups_python)
    close_popups(popups_ff_plugin)