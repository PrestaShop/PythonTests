from commons import ui


class adminPageScreen():    
    
    def __init__(self):
        self._objects = {
                        'dashboard': ("css","li#maintab-AdminDashboard"),
                        
                        'catalog': ("css","li#maintab-AdminCatalog"),
                        'catalog-products' : ("css","li#subtab-AdminProducts"),
                        'catalog-categories' : ("css","li#subtab-AdminCategories"),
                        'catalog-tracking' : ("css","li#subtab-AdminTracking"),
                        'catalog-attributes_groups' : ("css","li#subtab-AdminAttributesGroups"),
                        'catalog-features' : ("css","li#subtab-AdminFeatures"),
                        'catalog-manufacturers' : ("css","li#subtab-AdminManufacturers"),
                        'catalog-suppliers' : ("css","li#subtab-AdminSuppliers"),
                        'catalog-tags' : ("css","li#subtab-AdminTags"),
                        'catalog-admin_attachments' : ("css","li#subtab-AdminAttachments"),
                        
                        'orders': ("css","li#maintab-AdminParentOrders"),
                        'orders-orders' : ("css","li#subtab-AdminOrders"),
                        'orders-invoces' : ("css","li#subtab-AdminInvoices"),
                        'orders-return' : ("css","li#subtab-AdminReturn"),
                        'orders-delivery_slip' : ("css","li#subtab-AdminDeliverySlip"),
                        'orders-slip' : ("css","li#subtab-AdminSlip"),
                        'orders-statuses' : ("css","li#subtab-AdminStatuses"),
                        'orders-order_message' : ("css","li#subtab-AdminOrderMessage"),

                        'customer': ("css","li#maintab-AdminParentCustomer"),
                        'customer-customers' : ("css","li#subtab-AdminCustomers"),
                        'customer-addresses' : ("css","li#subtab-AdminAddresses"),
                        'customer-groups' : ("css","li#subtab-AdminGroups"),
                        'customer-carts' : ("css","li#subtab-AdminCarts"),
                        'customer-customer_threads' : ("css","li#subtab-AdminCustomerThreads"),
                        'customer-contacts' : ("css","li#subtab-AdminContacts"),
                        'customer-genders' : ("css","li#subtab-AdminGenders"),

                        
                        'price_rule': ("css","li#maintab-AdminPriceRule"),
                        'price_rule-cart_rules' : ("css","li#subtab-AdminCartRules"),
                        'price_rule-specific_price_rule' : ("css","li#subtab-AdminSpecificPriceRule"),
                        'price_rule-marketing' : ("css","li#subtab-AdminMarketing"),
                        
                        'modules': ("css","li#maintab-AdminParentModules"),
                        'modules-modules' : ("css","li#subtab-AdminModules"),
                        'modules-addons_catalog' : ("css","li#subtab-AdminAddonsCatalog"),
                        'modules-modules_positions' : ("css","li#subtab-AdminModulesPositions"),
                        'modules-payment' : ("css","li#subtab-AdminPayment"),
                        
                        'shipping': ("css","li#maintab-AdminParentShipping"),
                        'shipping-carriers' : ("css","li#subtab-AdminCarriers"),
                        'shipping-shipping' : ("css","li#subtab-AdminShipping"),
                        
                        'localization': ("css","li#maintab-AdminParentLocalization"),
                        'localization-localization' : ("css","li#subtab-AdminLocalization"),
                        'localization-languages' : ("css","li#subtab-AdminLanguages"),
                        'localization-zones' : ("css","li#subtab-AdminZones"),
                        'localization-countries' : ("css","li#subtab-AdminCountries"),
                        'localization-states' : ("css","li#subtab-AdminStates"),
                        'localization-currencies' : ("css","li#subtab-AdminCurrencies"),
                        'localization-taxes' : ("css","li#subtab-AdminTaxes"),
                        'localization-rules_group' : ("css","li#subtab-AdminTaxRulesGroup"),
                        'localization-translations' : ("css","li#subtab-AdminTranslations"),
                        
                        'preferences': ("css","li#maintab-AdminParentPreferences"),
                        'preferences-preferences' : ("css","li#subtab-AdminPreferences"),
                        'preferences-order_preferences' : ("css","li#subtab-AdminOrderPreferences"),
                        'preferences-p_preferences' : ("css","li#subtab-AdminPPreferences"),
                        'preferences-customer_preferences' : ("css","li#subtab-AdminCustomerPreferences"),
                        'preferences-themes' : ("css","li#subtab-AdminThemes"),
                        'preferences-meta' : ("css","li#subtab-AdminMeta"),
                        'preferences-cms_content' : ("css","li#subtab-AdminCmsContent"),
                        'preferences-images' : ("css","li#subtab-AdminImages"),
                        'preferences-stores' : ("css","li#subtab-AdminStores"),
                        'preferences-conf' : ("css","li#subtab-AdminSearchConf"),
                        'preferences-maintenance' : ("css","li#subtab-AdminMaintenance"),
                        'preferences-geolocation' : ("css","li#subtab-AdminGeolocation"),
                        
                        'tools': ("css","li#maintab-AdminTools"),
                        'tools-information' : ("css","li#subtab-AdminInformation"),
                        'tools-performance' : ("css","li#subtab-AdminPerformance"),
                        'tools-emails' : ("css","li#subtab-AdminEmails"),
                        'tools-import' : ("css","li#subtab-AdminImport"),
                        'tools-backup' : ("css","li#subtab-AdminBackup"),
                        'tools-request_sql' : ("css","li#subtab-AdminRequestSql"),
                        'tools-logs' : ("css","li#subtab-AdminLogs"),
                        'tools-webservice' : ("css","li#subtab-AdminWebservice"),
                        
                        'admin': ("css","li#maintab-AdminAdmin"),
                        'admin-admin_preferences' : ("css","li#subtab-AdminAdminPreferences"),
                        'admin-quick_accesses' : ("css","li#subtab-AdminQuickAccesses"),
                        'admin-employees' : ("css","li#subtab-AdminEmployees"),
                        'admin-profiles' : ("css","li#subtab-AdminProfiles"),
                        'admin-access' : ("css","li#subtab-AdminAccess"),
                        'admin-tabs' : ("css","li#subtab-AdminTabs"),
                        'admin-gamification' : ("css","li#subtab-AdminGamification"),
                        
                        'stats': ("css","li#maintab-AdminParentStats"),
                        'stats-stats' : ("css","li#subtab-AdminStats"),
                        'stats-search_engines' : ("css","li#subtab-AdminSearchEngines"),
                        'stats-referrers' : ("css","li#subtab-AdminReferrers"),
                        
                         }

    def go_to_admin_menu(self,entry,subEntry=False):
        if subEntry == False:
            ui.click(self._objects[entry])
        else:
            ui.click_submenu(self._objects[entry],self._objects[subEntry])