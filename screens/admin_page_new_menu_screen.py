import time

from commons import ui
from commons.Context import Context
from commons.Configuration import Configuration


class adminPageScreen():
    def __init__(self):
        self._objects = {
            'Dashboard': ("css", "li#tab-AdminDashboard"),

            'Orders': ("css", "li#subtab-AdminParentOrders"),
            'Orders_orders': ("css", "li#subtab-AdminOrders"),
            'Orders_invoices': ("css", "li#subtab-AdminInvoices"),
            'Orders_slip': ("css", "li#subtab-AdminSlip"),
            'Orders_deliverySlip': ("css", "li#subtab-AdminDeliverySlip"),
            'Orders_carts': ("css", "li#subtab-AdminCarts"),

            'Catalog': ("css", "li#subtab-AdminCatalog"),
            'Catalog_products': ("xpath", "//li[contains(@class,\"link-leveltwo\")]/a[contains(text(),\"Products\")]"),
            'Catalog_categories': ("css", "li#subtab-AdminCategories"),
            'Catalog_tracking': ("css", "li#subtab-AdminTracking"),
            'Catalog_attributesGroups': ("css", "li#subtab-AdminParentAttributesGroups"),
            'Catalog_manufacturers': ("css", "li#subtab-AdminParentManufacturers"),
            'Catalog_attachments': ("css", "li#subtab-AdminAttachments"),
            'Catalog_cartRules': ("css", "li#subtab-AdminParentCartRules"),

            'Customer': ("css", "li#AdminParentCustomer"),
            'Customer_customers': ("css", "li#subtab-AdminCustomers"),
            'Customer_addresses': ("css", "li#subtab-AdminAddresses"),

            'CustomerThreads': ("css", "li#subtab-AdminParentCustomerThreads"),
            'CustomerThreads_customerThreads': ("css", "li#subtab-AdminCustomerThreads"),
            'CustomerThreads_return': ("css", "li#subtab-AdminReturn"),
            'CustomerThreads_orderMessage': ("css", "li#subtab-AdminOrderMessage"),

            'Shipping': ("css", "li#subtab-AdminParentShipping"),
            'Shipping_carriers': ("css", "li#subtab-AdminCarriers"),
            'Shipping_shipping': ("css", "li#subtab-AdminShipping"),

            'Payment': ("css", "li#subtab-AdminPayment"),
            'Payment_payment': ("css", "li#subtab-AdminPayment"),
            'Payment_paymentPreferences': ("css", "li#subtab-AdminPaymentPreferences"),

            'Stats': ("css", "li#subtab-AdminStats"),

            'Modules': ("xpath", "//li[@id='subtab-AdminParentModulesSf']"),
            'Modules_modules': ("xpath", "//li[@id='subtab-AdminModulesSf']"),
            'Modules_marketing': ("xpath", "//li[@id='subtab-AdminMarketing']"),

            'Themes': ("css", "li#subtab-AdminThemes"),
            'Themes_themes': ("css", "li#subtab-AdminThemes"),
            'Themes_addonsCatalog': ("css", "li#subtab-AdminAddonsCatalog"),
            'Themes_cmsContent': ("css", "li#subtab-AdminCmsContent"),
            'Themes_modulesPositions': ("css", "li#subtab-AdminModulesPositions"),
            'Themes_images': ("css", "li#subtab-AdminImages"),

            'Localization': ("css", "li#subtab-AdminParentLocalization"),
            'Localization_localization': ("css", "li#subtab-AdminLocalization"),
            'Localization_countries': ("css", "li#subtab-AdminCountries"),
            'Localization_taxes': ("css", "li#subtab-AdminTaxes"),
            'Localization_translations': ("css", "li#subtab-AdminTranslations"),

            'Preferences': ("css", "li#subtab-AdminAdvancedParameters"),
            'Preferences_preferences': ("css", "li#subtab-AdminPreferences"),
            'Preferences_orderPreferences': ("css", "li#subtab-AdminParentOrderPreferences"),
            'Preferences_products': ("css", "li#subtab-AdminPPreferences"),
            'Preferences_customerPreferences': ("css", "li#subtab-AdminCustomerPreferences"),
            'Preferences_stores': ("css", "li#subtab-AdminParentStores"),
            'Preferences_meta': ("css", "li#subtab-AdminMeta"),
            'Preferences_searchConf': ("css", "li#subtab-AdminSearchConf"),
            'Preferences_employees': ("css", "li#subtab-AdminParentEmployees"),

            'AdvancedParameters': ("css", "li#subtab-AdminAdvancedParameters"),
            'AdvancedParameters_information': ("css", "li#subtab-AdminInformation"),
            'AdvancedParameters_performance': ("css", "li#subtab-AdminPerformance"),
            'AdvancedParameters_admin': ("css", "li#subtab-AdminAdmin"),
            'AdvancedParameters_emails': ("css", "li#subtab-AdminEmails"),
            'AdvancedParameters_import': ("css", "li#subtab-AdminImport"),
            'AdvancedParameters_requestSql': ("css", "li#subtab-AdminRequestSql"),
            'AdvancedParameters_logs': ("css", "li#subtab-AdminLogs"),
            'AdvancedParameters_webservice': ("css", "li#subtab-AdminWebservice"),

            'Error_alert': ("xpath", "//div[@class='alert alert-danger']"),
            'Error_message': ("xpath", "//div[@id='content']/h1"),

            'General_loginHeader': ("xpath", "//div[@id='login-header']"),
            'General_logoPrestaShop': ("xpath", "//a[@id='header_logo']"),
            'General_logoPrestaShopModules': ("xpath", "//a[@class='logo pull-left']"),
        }

    def go_to_admin_menu(self, entry, subEntry=False):
        if subEntry == False:
            ui.click(self._objects[entry])
        else:
            ui.click_submenu_by_move(self._objects[entry], self._objects[subEntry])

    def open_all_contoller(self):
        f = open("datasets/controllers.txt", "r")
        storename = ""
        if Configuration().storename != None:
            storename = Configuration().storename

        for l in f:

            if Configuration().vm == None:
                url = Context().environment.url.replace('str(i)', storename).replace('str(j)',
                                                                                     'localhost/') + "?controller=" + l
            else:
                url = Context().environment.url.replace('str(i)', storename).replace('str(j)',
                                                                                     Configuration().vm + '/') + "?controller=" + l
            Context().goto_url(url)

            time.sleep(3)
            if (ui.is_visible(self._objects["Error_alert"])):
                if (ui.is_existant(self._objects["Error_message"])):
                    if (ui.get_text(self._objects["Error_message"]) == "The controller %s is missing or invalid." % (
                    l.strip())):
                        Context().logger.info("%s controller is OK" % (l.strip()))
                    else:
                        Context().logger.error("%s controller is broken" % (l.strip()))
                else:
                    Context().logger.error("%s controller is broken" % (l.strip()))
            else:
                if (not ui.is_visible(self._objects["General_loginHeader"]) and not ui.is_visible(
                        self._objects["General_logoPrestaShop"]) and not ui.is_visible(
                        self._objects["General_logoPrestaShopModules"])):
                    Context().logger.error("%s controller is broken" % (l.strip()))
                else:
                    Context().logger.info("%s controller is OK" % (l.strip()))