#!/usr/bin/env python
# -*- coding: utf-8 -*-
from commons import ui
import time
from commons.Context import Context
from commons.Configuration import Configuration
from selenium.webdriver.common.keys import Keys
from commons.Test import Test


class catalogProductScreen():
    def __init__(self):
        if '1.6' in Configuration().version_presta:
            self._objects = {
                'product_image': ("css", "#link-Images"),
                'product_add_image': ("css", "#file-add-button"),
                'product_image_select': ("css", ".imgm.img-thumbnail"),
                'product_table': ("xpath", "//table[@id='table-product']//tbody"),
                'product_table_number': ("css", ".badge"),
                'product_table_check': ("xpath", "//*[@id='table-product']//tbody//tr[1]"),
                'product_table_id_desc': ("xpath", "//table[@id='table-product']//tr[1]/th/span/a[1]"),
                'line_product_table': ("xpath", "//table[@id=\"table-product\"]//tbody//tr[str(i)]"),
                'col_line_product_table': ("xpath", "//table[@id=\"table-product\"]//tbody//tr[str(i)]//td[str(j)]"),
                'btn_file_save': ("css", "#file-upload-button"),
                'btn_upload_file': ("css", "#file-add-button"),
                'file_list': ("css", "#file-files-list"),
                'product_add_product': ("css", "#page-header-desc-product-new_product"),
                'product_new_informations': ("css", "#link-Informations"),
                'product_new_info_type_simple': ("css", "#simple_product"),
                'product_new_info_type_pack': ("css", "#pack_product"),
                'product_new_info_type_virtual': ("css", "#virtual_product"),
                'product_new_info_name': ("css", "#name_1"),
                'product_new_info_ref': ("css", "#reference"),
                'product_new_info_ean13': ("css", "#ean13"),
                'product_new_info_upc': ("css", "#upc"),
                'product_new_info_on': ("xpath", "//label[@for='active_on']"),
                'product_new_info_off': ("xpath", "//label[@for='active_off']"),
                'product_new_info_available': ("css", "#available_for_order"),
                'product_new_info_show_price': ("css", "#show_price"),
                'product_new_info_online_only': ("css", "#online_only"),
                'product_new_info_resume': ("xpath", "//*[@id='mce_54']//iframe"),
                'product_new_info_desc': ("xpath", "//*[@id='mce_94']//iframe"),
                'product_new_info_tags': ("css", ".tagify-container input"),
                'product_new_visibility': ("xpath", "//*[@id=\"visibility\"]//option[@value='str(i)']"),
                'product_new_condition': ("xpath", "//*[@id=\"condition\"]//option[@value='str(i)']"),
                'product_new_save_stay': ("xpath", "(//*[@name='submitAddproductAndStay'])[1]"),
                'product_new_save_stay2': ("xpath", "(//*[@name='submitAddproductAndStay'])[2]"),
                'product_new_prices': ("css", "#link-Prices"),
                'product_new_wholesale': ("css", "#wholesale_price"),
                'product_new_price_TE': ("css", "#priceTE"),
                'product_new_price_TI': ("css", "#priceTI"),
                'product_new_price_unit': ("css", "#unit_price"),
                'product_new_price_unity': ("css", "#unity"),
                'product_new_price_on_sale': ("css", "#on_sale"),
                'product_new_Seo': ("css", "#link-Seo"),
                'product_new_Seo_meta_title': ("css", "#meta_title_1"),
                'product_new_Seo_meta_desc': ("css", "#meta_description_1"),
                'product_new_Seo_short_link': ("css", "#link_rewrite_1"),
            }

        if '1.7' in Configuration().version_presta or '17' in Configuration().version_presta:
            self._objects = {
                'product_table': ("xpath", "//form[@id='product_catalog_list']//div//table//tbody"),
                'product_table_number': ("xpath", "//*[@id=\"main-div\"]/div[3]/div/div/div[2]/div[2]/div[1]/div/h2"),
                'product_table_check': ("xpath", "//form[@id='product_catalog_list']//div//table//tbody//tr[1]"),
                'product_table_id_desc': (
                "xpath", "//form[@id='product_catalog_list']/div[2]/div/table/thead/tr[1]/th[1]/span[2]"),
                'line_product_table': ("xpath", "//form[@id=\"product_catalog_list\"]//div//table//tbody//tr[str(i)]"),
                'col_line_product_table_first_column': (
                "xpath", "//form[@id=\"product_catalog_list\"]//div//table//tbody//tr[str(i)]//td[str(j)]/div/label"),
                'col_line_product_table': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div/div/table/tbody/tr[str(i)]//td[str(j)]"),
                'product_add_product': ("css", "#page-header-desc-configuration-add"),

                'product_new_informations': ("xpath", "//a[@href='#step1']"),
                'product_new_info_type': (
                "xpath", "//select[@id=\"form_step1_type_product\"]//option[@value='str(i)']"),
                'product_new_info_name': ("css", "#form_step1_name_1"),
                'porduct_new_save_for_pictures': ("xpath", "//button[@class='btn btn-xs btn-primary']"),
                'product_new_info_ref': ("css", "#form_step6_reference"),
                'product_new_info_ean13': ("css", "#form_step6_ean13"),
                'product_new_info_isbn': ("css", "#form_step6_isbn"),
                'product_new_info_upc': ("css", "#form_step6_upc"),

                'product_new_info_features_add': ("css", "#add_feature_button"),
                'product_new_info_features_feature': (
                "xpath", "//select[@id=\"form_step1_features_str(i)_feature\"]//option[@value='str(j)']"),
                'product_new_info_features_custom_value': (
                "xpath", "//input[@id=\"form_step1_features_'str(i)'_custom_value_1\"]"),
                'product_new_info_features_value': (
                "xpath", "//select[@id=\"form_step1_features_'str(i)'_value\"]//option[@value=\"str(j)\"]"),

                'product_new_info_on': ("xpath", "//input[@id='form_step1_active_0']"),
                'product_new_info_off': ("xpath", "//input[@id='form_step1_active_1']"),
                'product_new_info_activate': ("css", ".switch-input"),
                'product_new_info_activate_check': ('css', '.switch-input.-checked'),
                'product_add_image': ("css", "#product-images-dropzone"),
                'product_new_info_available': ("css", "#available_for_order"),
                'product_new_info_show_price': ("css", "#show_price"),
                'product_new_info_online_only': ("css", "#online_only"),
                'product_new_info_desc_document': ("xpath", "//body[@id='tinymce']"),
                'product_new_info_resume_document': ("xpath", "//body[@id='tinymce']"),
                'product_new_info_resume': ("xpath", "//a[@href='#description_short']"),
                'product_new_info_desc': ("xpath", "//a[@href='#description']"),
                'product_new_info_tags': ("css", ".tagify-container input"),
                'product_new_visibility': ("xpath", "//*[@id=\"visibility\"]//option[@value='str(i)']"),
                'product_new_condition': ("xpath", "//*[@id=\"form_step6_condition\"]//option[@value='str(i)']"),
                'product_new_condition_check': ("xpath", "//select[@id='form_step6_condition']/option[@selected]"),
                'product_new_info_category_expand': ("css", "#form_step1_categories > ul > li > div"),
                'product_new_info_sub_category_expand': (
                'xpath', '//div[@id="form_step1_categories"]/ul/li/ul//li/div/label[text()="test_auto"]/..'),
                'product_new_info_category_checkbox': (
                'xpath', '//div[@id="form_step1_categories"]//label[text()="str(i)"]//input'),

                'product_new_info_default_category': (
                "xpath", "//select[@id=\"form_step1_id_category_default\"]/option[@value=str(i)]"),
                'product_new_info_default_category2': (
                "xpath", "//div[@id=\"form_step1_categories\"]//label[text()='str(i)']//../div/input"),
                'product_new_info_new_category_name': ('css', '#form_step1_new_category_name'),
                'product_new_info_new_category_parent_category': (
                "xpath", "//select[@id=\"form_step1_new_category_id_parent\"]/option[text()='str(i)']"),
                'product_new_info_new_category_save': ('css', '#form_step1_new_category_save'),
                'category_name_checkbox': (
                "xpath", "//input[@name=\"form[step1][categories][tree][]\" and ancestor::label[text()=\"str(i)\"]]"),
                'category_default_save': (
                "xpath", "//select[@id=\"form_step1_id_category_default\"]/option[@selected]"),

                'product_new_prices': ("xpath", "//a[@href='#step2']"),
                'product_new_sell_price_ht': ("css", "#form_step2_price"),
                'product_new_sell_price_ttc': ("css", "#form_step2_price_ttc"),
                'product_new_price_on_sale': ("css", "#form_step2_on_sale"),
                'product_new_price_ht': ("css", "#form_step2_wholesale_price"),
                'product_new_price_unit_ht': ("css", "#form_step2_unit_price"),
                'product_new_price_unity_ht': ("css", "#form_step2_unity"),
                'product_new_info_price_priority': (
                "xpath", "//*[@id=\"form_step2_specificPricePriority_str(i)\"]/option[@value=\"str(j)\"]"),
                'product_new_info_price_priority_apply_to_all': ('css', '#form_step2_specificPricePriorityToAll'),
                'product_new_pack_quantity': (
                "xpath", "//select[@id=\"form_step3_pack_stock_type\"]/option[@value=str(i)]"),
                'product_new_pack_quantity_check': (
                "xpath", "//select[@id='form_step3_pack_stock_type']/option[@selected]"),

                'product_new_quantity_variation': ("xpath", "//a[@href='#step3']"),
                'prodcut_new_quantity_advanced_stock': ("css", "#form_step3_advanced_stock_management"),
                'product_new_quantity_quantity': ("css", "#form_step3_qty_0"),
                'product_new_quantity_case_out_of_stock': ("xpath", "//input[@id=\"form_step3_out_of_stock_str(i)\"]"),
                'product_new_quantity_minimum': ("css", "input#form_step3_minimal_quantity"),
                'product_new_quantity_in_stock': ("css", "input#form_step3_available_now_1"),
                'product_new_quantity_out_stock': ("css", "input#form_step3_available_later_1"),
                'product_new_quantity_date_stock': ("css", "input#form_step3_available_date"),
                'product_new_variation_creation_value': (
                "xpath", "//div[@class=\"tt-suggestion tt-selectable\" and text()='str(i)']"),
                'product_new_variation_creation': ("css", "input#form_step3_attributes-tokenfield"),
                'product_new_variation_create': ("css", "#create-combinations"),
                'product_new_variation_open_close': ("xpath", "//button[@class='btn btn-tertiary-outline btn-back']"),
                'product_new_variation_open_close2': (
                "xpath", "(//button[@class=\"btn btn-tertiary-outline btn-back\"])[str(i)]"),
                'product_new_nb_variation': ("xpath", "//tbody[@id='accordion_combinations']/tr"),
                'product_new_list_variation': ("xpath", "//tbody[@id='accordion_combinations']"),
                'product_new_id_variation': ("xpath", "(//tbody[@id=\"accordion_combinations\"]/tr)[str(i)]"),
                'product_new_variation_open': ("xpath", "(//div[@class=\"btn-group btn-group-sm\"])[str(i)]/a[1]"),
                'product_new_variation_open_delete': (
                "xpath", "//tr[@data-index=str(i)]//td//a[@class=\"btn btn-default btn-sm delete\"]"),
                'product_new_variation_ref': ("xpath", "//input[@id=\"combination_str(i)_attribute_reference\"]"),
                'product_new_variation_ean13': ("xpath", "//input[@id=\"combination_str(i)_attribute_ean13\"]"),
                'product_new_variation_isbn': ("xpath", "//input[@id=\"combination_str(i)_attribute_isbn\"]"),
                'product_new_variation_upc': ("xpath", "//input[@id=\"combination_str(i)_attribute_upc\"]"),
                'product_new_variation_wholesale': (
                "xpath", "//input[@id=\"combination_str(i)_attribute_wholesale_price\"]"),
                'product_new_variation_price_impact': (
                "xpath", "//select[@id=\"combination_str(i)_attribute_price_impact\"]//option[@value=str(j)]"),
                'product_new_variation_price': ("xpath", "//input[@id=\"combination_str(i)_attribute_price\"]"),
                'product_new_variation_priceTI': ("xpath", "//input[@id=\"combination_str(i)_attribute_priceTI\"]"),
                'product_new_variation_weight_impact': (
                "xpath", "//select[@id=\"combination_str(i)_attribute_weight_impact\"]//option[@value=str(j)]"),
                'product_new_variation_weight': ("xpath", "//input[@id=\"combination_str(i)_attribute_weight\"]"),
                'product_new_variation_unit_impact': (
                "xpath", "//select[@id=\"combination_str(i)_attribute_unit_impact\"]//option[@value=str(j)]"),
                'product_new_variation_unity': ("xpath", "//input[@id=\"combination_str(i)_attribute_unity\"]"),
                'product_new_variation_minimal_quantity': (
                "xpath", "//input[@id=\"combination_str(i)_attribute_minimal_quantity\"]"),
                'product_new_variation_available_date': (
                "xpath", "//input[@id=\"combination_str(i)_available_date_attribute\"]"),
                'product_new_variation_default': ("xpath", "//input[@id=\"combination_str(i)_attribute_default\"]"),
                'product_new_variation_quantity': ("xpath", "//input[@id=\"combination_str(i)_attribute_quantity\"]"),
                'product_new_variation_img_liste': (
                "xpath", "//div[@id=\"combination_str(i)_id_image_attr\"]//div//input"),
                'product_new_variation_img_checkbox': (
                "xpath", "//div[@id=\"combination_str(i)_id_image_attr\"]//div[str(j)]//input"),

                'product_new_carrier_tab': ("xpath", "//a[@href='#step4']"),
                'product_new_carrier_width': ("css", "#form_step4_width"),
                'product_new_carrier_height': ("css", "#form_step4_height"),
                'product_new_carrier_depth': ("css", "#form_step4_depth"),
                'product_new_carrier_weight': ("css", "#form_step4_weight"),
                'product_new_carrier_add_ship_coast': ("css", "#form_step4_additional_shipping_cost"),
                'product_new_carrier': (
                "xpath", "//div[@id=\"form_step4_selectedCarriers\"]//div//label[contains(text(),'str(i)')]"),
                'product_new_carrier_check': ("xpath",
                                              "//div[@id=\"form_step4_selectedCarriers\"]//div//label[contains(text(),'str(i)')]/input[@checked]"),

                'product_new_ref': ("xpath", "//a[@href='#step5']"),
                'product_new_ref_title': ("css", "#form_step5_meta_title_1"),
                'product_new_ref_desc': ("css", "#form_step5_meta_description_1"),
                'product_new_ref_url': ("css", "#form_step5_link_rewrite_1"),

                'product_new_options': ("xpath", "//a[@href='#step6']"),
                'product_new_options_visibility': (
                "xpath", "//select[@id=\"form_step6_visibility\"]//option[@value='str(i)']"),
                'product_new_options_avalaible_orders': ("css", "input#form_step6_display_options_available_for_order"),
                'product_new_options_show_price': ("css", "input#form_step6_display_options_show_price"),
                'product_new_options_online_only': ("css", "input#form_step6_display_options_online_only"),
                'product_new_options_suppliers': ("css", "input#form_step6_suppliers_0"),
                'product_new_options_default_supplier': (
                "xpath", "//select[@id=\"form_step6_default_supplier\"]//option[str(i)]"),
                'product_new_options_supplier_reference': (
                "css", "#form_step6_supplier_combination_1_str(i)_supplier_reference"),
                'product_new_supplier_name_product': (
                "xpath", "//div[@id=\"supplier_combination_collection\"]/div[2]/div[2]/div/table//tr[str(i)]/td[1]"),
                'product_new_options_product_price': ("css", "#form_step6_supplier_combination_1_str(i)_product_price"),
                'product_new_options_price_currency': ("xpath",
                                                       "//select[@id=\"form_step6_supplier_combination_1_str(i)_product_price_currency\"]//option[str(j)]"),

                'product_new_save1': ("xpath", "//div[@id='step1']//div[@class='text-right']//input"),
                'product_new_save2': ("xpath", "//div[@id='step2']//div[@class='text-right']//input"),
                'product_new_save3': ("xpath", "//div[@id='step3']//div[@class='text-right']//input"),
                'product_new_save4': ("xpath", "//div[@id='step4']//div[@class='text-right']//input"),
                'product_new_save5': ("xpath", "//div[@id='step5']//div[@class='text-right']//input"),
                'product_new_save6': ("xpath", "//div[@id='step6']//div[@class='text-right']//input"),
                'product_new_next': ("xpath", "//*[@class='btn btn-primary btn-next']"),
                'product_new_next2': ("xpath", "(//*[@class='btn btn-primary btn-next'])[2]"),
                'product_new_next3': ("xpath", "(//*[@class='btn btn-primary btn-next'])[3]"),
                'product_new_next4': ("xpath", "(//*[@class='btn btn-primary btn-next'])[4]"),
                'product_new_next5': ("xpath", "(//*[@class='btn btn-primary btn-next'])[5]"),
                'product_new_previous': ("xpath", "//*[@class='btn btn-primary btn-prev']"),
                'product_new_save': ("css", "#submit"),

                'product_new_virtual_file_yes': ("css", "#form_step3_virtual_product_is_virtual_file_0"),
                'product_new_virtual_file_no': ("css", "#form_step3_virtual_product_is_virtual_file_1"),
                'product_new_virtual_file': ("css", "#form_step3_virtual_product_file"),
                'product_new_virtual_file_name': ("css", "#form_step3_virtual_product_name"),
                'product_new_virtual_file_nb_download': ("css", "#form_step3_virtual_product_nb_downloadable"),
                'product_new_virtual_file_exp_date': ("css", "#form_step3_virtual_product_expiration_date"),
                'product_new_virtual_file_nb_days': ("css", "#form_step3_virtual_product_nb_days"),
                'product_new_virtual_file_save': ("css", "#form_step3_virtual_product_save"),

                'product_new_pack_search': ("css", "#form_step1_inputPackItems"),
                'product_new_pack_quantity_product': ("css", "#form_step1_inputPackItems-curPackItemQty"),
                'product_new_pack_add': ("css", "#form_step1_inputPackItems-curPackItemAdd"),
                'pack_product_name': ("xpath", "//*[@id=\"form_step1_inputPackItems-data\"]/li[str(i)]/div/h4"),
                'pack_product_quantity': ("xpath",
                                          "//*[@id=\"form_step1_inputPackItems-data\"]/li[str(i)]/div/div[@class=\"quantity text-md-right\"]"),

                'product_new_specific_price_add': ("xpath", "//a[@href='#specific_price_form']"),
                'product_new_specific_price_shop': (
                "xpath", "//*[@id=\"form_step2_specific_price_sp_id_shop\"]//option[@value=str(i)]"),
                'product_new_specific_price_currency': (
                "xpath", "//*[@id=\"form_step2_specific_price_sp_id_currency\"]//option[@value=str(i)]"),
                'product_new_specific_price_country': (
                "xpath", "//*[@id=\"form_step2_specific_price_sp_id_country\"]//option[@value=str(i)]"),
                'product_new_specific_price_group': (
                "xpath", "//*[@id=\"form_step2_specific_price_sp_id_group\"]//option[@value=str(i)]"),
                'product_new_specific_price_variation': (
                "xpath", "//*[@id=\"form_step2_specific_price_sp_id_product_attribute\"]//option[@value=str(i)]"),
                'product_new_specific_price_start_date': ("css", "#form_step2_specific_price_sp_from"),
                'product_new_specific_price_end_date': ("css", "#form_step2_specific_price_sp_to"),
                'product_new_specific_price_quantity': ("css", "#form_step2_specific_price_sp_from_quantity"),
                'product_new_specific_price_price': ("css", "#form_step2_specific_price_sp_price"),
                'product_new_specific_price_show_price': ("css", "#form_step2_specific_price_leave_bprice"),
                'product_new_specific_price_reduction': ("css", "#form_step2_specific_price_sp_reduction"),
                'product_new_specific_price_reduction_type': (
                "xpath", "//*[@id=\"form_step2_specific_price_sp_reduction_type\"]//option[@value='str(i)']"),
                'product_new_specific_price_reduction_tax': (
                "xpath", "//*[@id=\"form_step2_specific_price_sp_reduction_tax\"]//option[@value=str(i)]"),
                'product_new_specific_price_save': ("css", "#form_step2_specific_price_save"),

                'product_new_document_attach_file': ("css", "#form_step6_attachment_product_file"),
                'product_new_document_attach_name': ("css", "#form_step6_attachment_product_name"),
                'product_new_document_attach_desc': ("css", "#form_step6_attachment_product_description"),
                'product_new_document_attach_add': ("css", "#form_step6_attachment_product_add"),

                'product_new_personalization_add': ("xpath", "//div[@id=\"custom_fields\"]/a"),
                'product_new_personalization_name': ("css", "#form_step6_custom_fields_str(i)_label_1"),
                'product_new_personalization_type': (
                "xpath", "//*[@id=\"form_step6_custom_fields_str(i)_type\"]//option[@value=str(j)]"),
                'product_new_personalization_mandatory': ("css", "#form_step6_custom_fields_str(i)_require"),

                'product_new_related_products_search': ("css", "#form_step1_related_products"),

                'product_open_manufacturer': ("css", "#add_brand_button"),
                'product_open_category': ("css", "#add-categories > a"),
                'product_open_features': ("css", "#add_feature_button"),
                'product_open_related_product': ("css", "#add-related-product-button"),

                'product_new_manufacturer': ("xpath", "//*[@id=\"form_step1_id_manufacturer\"]//option[@value=str(i)]"),
                'product_manufacturer_check': ("xpath", "//select[@id='form_step1_id_manufacturer']/option[@selected]"),

                'product_new_sell_price_ht_shortcut': ("css", "#form_step1_price_shortcut"),
                'product_new_sell_price_ttc_shortcut': ("css", "#form_step1_price_ttc_shortcut"),
                'product_new_quantity_quantity_shortcut': ("css", "#form_step1_qty_0_shortcut"),
                'product_new_activate_variation': ("xpath", "//input[@name=\"show_variations\" and @value=str(i)]"),

                'product_new_upload_img': ("xpath", "(//input[@type='file'])[3]"),
                'product_new_file_associate': ("xpath", "(//input[@type='file'])[2]"),
                'product_new_virtual_file': ("xpath", "(//input[@type='file'])[1]"),

                # Catalog page
                'catalog_select_all': ("css", "#bulk_action_select_all"),
                'catalog_table_id_asc': ("xpath", "//span[@psorderby='id_product' and @psorderway='asc']"),
                'catalog_table_name_asc': ("xpath", "//span[@psorderby='name' and @psorderway='asc']"),
                'catalog_table_name_desc': ("xpath", "//span[@psorderby='name' and @psorderway='desc']"),
                'catalog_table_ref_asc': ("xpath", "//span[@psorderby='reference' and @psorderway='asc']"),
                'catalog_table_ref_desc': ("xpath", "//span[@psorderby='reference' and @psorderway='desc']"),
                'catalog_table_cat_asc': ("xpath", "//span[@psorderby='name_category' and @psorderway='asc']"),
                'catalog_table_cat_desc': ("xpath", "//span[@psorderby='name_category' and @psorderway='desc']"),
                'catalog_table_price_asc': ("xpath", "//span[@psorderby='price' and @psorderway='asc']"),
                'catalog_table_price_desc': ("xpath", "//span[@psorderby='price' and @psorderway='desc']"),
                'catalog_table_quantity_asc': ("xpath", "//span[@psorderby='sav_quantity' and @psorderway='asc']"),
                'catalog_table_quantity_desc': ("xpath", "//span[@psorderby='sav_quantity' and @psorderway='desc']"),
                'catalog_table_state_asc': ("xpath", "//span[@psorderby='active' and @psorderway='asc']"),
                'catalog_table_state_desc': ("xpath", "//span[@psorderby='active' and @psorderway='desc']"),
                'catalog_search_id': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div[2]/div/table/thead/tr[2]/th[1]/input"),
                'catalog_search_name': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div[2]/div/table/thead/tr[2]/th[3]/input"),
                'catalog_search_ref': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div[2]/div/table/thead/tr[2]/th[4]/input"),
                'catalog_search_cat': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div[2]/div/table/thead/tr[2]/th[5]/input"),
                'catalog_search_price_min': ("xpath", "//form[@id='filter_column_price_min']"),
                'catalog_search_price_max': ("xpath", "//form[@id='filter_column_price_max']"),
                'catalog_search_qty_min': ("xpath", "//form[@id='filter_column_sav_quantity_min']"),
                'catalog_search_qty_max': ("xpath", "//form[@id='filter_column_sav_quantity_max']"),
                'catalog_search_state': ("xpath",
                                         "//form[@id=\"product_catalog_list\"]/div[2]/div/table/thead/tr[2]/th[9]/select/option[@value=str(i)]"),
                'catalog_filter_reset': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div[2]/div/table/thead/tr[2]/th[10]/input[2]"),
                'catalog_go_to_first_page': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div[2]/div[2]/div/ul[1]/li[1]/a"),
                'catalog_go_to_last_page': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div[2]/div[2]/div/ul[1]/li[5]/a"),
                'catalog_go_to_previous_page': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div[2]/div[2]/div/ul[1]/li[2]/a"),
                'catalog_go_to_next_page': ("xpath", "//a[@id='pagination_next_url']"),
                'catalog_go_to_page_number': (
                "xpath", "//form[@id=\"product_catalog_list\"]/div[2]/div[2]/div/ul[1]/li[3]/input"),
                'catalog_number_element_per_page': (
                "xpath", "//select[@name=\"paginator_select_page_limit\"]/option[@selected]"),
                'catalog_change_number_element_per_page': ("xpath",
                                                           "//form[@id=\"product_catalog_list\"]/div[2]/div[2]/div/ul[2]/li/select/option[@value=str(i)]"),
                'catalog_sort_col': ("xpath", "//span[@psorderby='str(i)' and @psorderway='str(j)']"),
                'catalog_footer_table_product': ("xpath", "//*[@id='product_catalog_list']/div[2]/div[2]/div/ul[2]/li"),
                'col_line_product_table_activate': (
                'xpath', '//form[@id=\"product_catalog_list\"]//div//table//tbody//tr[str(i)]//td[str(j)]/a'),
                'catalog_open_product': (
                'xpath', '//form[@id=\"product_catalog_list\"]//div//table//tbody//tr[str(i)]//td[str(j)]/a'),
                'product_img': ("xpath", "//*[@id=\"product-images-dropzone\"]/div[str(i)]"),

                'product_new_variation_line_quantity': (
                "xpath", "(//td[@class=\"attribute-quantity\"]/div/input)[str(i)]"),
                "related_product_info": ("xpath", "(//ul[@id=\"form_step1_related_products-data\"])/li[str(i)]/span"),
                'feature_selected': ("xpath", "//select[@id=\"form_step1_features_str(i)_feature\"]/option[@selected]"),
                'feature_value': ("xpath", "//select[@id=\"form_step1_features_str(i)_value\"]/option[@selected]"),
                'feature_custom_value': ("xpath", "//input[@id=\"form_step1_features_str(i)_custom_value_1\"]"),
                'new_product_visibility_check': ("xpath", "//select[@id=\"form_step6_visibility\"]//option[@selected]"),
                'new_product_default_supplier_check': (
                "xpath", "//select[@id=\"form_step6_default_supplier\"]//option[@selected]"),
                'product_new_options_price_currency_check': ("xpath",
                                                             "//select[@id=\"form_step6_supplier_combination_1_str(i)_product_price_currency\"]//option[@selected]"),
                'product_tax_rules_listbox_shortcut': ("css", "#select2-step2_id_tax_rules_group_rendered-container"),
                'product_tax_rules_listbox_view_shortcut': (
                "xpath", "//ul[@id=\"select2-step2_id_tax_rules_group_rendered-results\"]/li[str(i)]"),
                'product_tax_rules_listbox': ("css", "#select2-form_step2_id_tax_rules_group-container"),
                'product_tax_rules_listbox_view': (
                "xpath", "//ul[@id=\"select2-form_step2_id_tax_rules_group-results\"]/li[str(i)]"),
                "redirection_page_listbox": ("css", "#select2-form_step5_redirect_type-container"),
                "redirection_page_listbox_result": (
                "xpath", "//ul[@id=\"select2-form_step5_redirect_type-results\"]/li[str(i)]"),
                "redirection_page_target": ("xpath", "//input[@id=\"form_step5_id_product_redirected\"]"),
                "redirect_target_name": ("xpath", "//ul[@id=\"form_step5_id_product_redirected-data\"]/li/div"),
                "product_list_quicknav_id": ("xpath",
                                             "//table[@class=\"table table-condensed table-striped product quicknav-products\"]/tbody/tr[str(i)]/td/a"),
                "product_footer_delete": ("css", "#product_form_delete_btn"),
                "product_footer_view": ("css", "#product_form_preview_btn"),
                "product_footer_duplicate": ("css", "#product_form_save_duplicate_btn"),
                "product_footer_go_to_catalog": ("css", "#product_form_save_go_to_catalog_btn"),
                "product_footer_new": ("css", "#product_form_save_new_btn"),
                "select_all_lines": ("css", "#bulk_action_select_all"),
                "bulk_actions_button": ("css", "#product_bulk_menu"),
                "bulk_actions_list": ("xpath", "//div[@class=\"btn-group dropup open\"]/ul/li[str(i)]/a"),
            }

    def add_product(self, var_test):
        new_product = False
        if '1.6' in Configuration().version_presta:
            if ui.get_text(self._objects['product_table_number']) == "1":
                max_id = ui.get_text(self._objects['product_table_check']).split(" ")[0]
            else:
                ui.click(self._objects['product_table_id_desc'])
                max_id = ui.get_text(self._objects['product_table_check']).split(" ")[0]
            ui.click(self._objects['product_add_product'])

            # Fill the Informations part of the product
            if var_test.get("type") == "simple":
                ui.click(self._objects['product_new_info_type_simple'])
            if var_test.get("type") == "pack":
                ui.click(self._objects['product_new_info_type_pack'])
            if var_test.get("type") == "virtual":
                ui.click(self._objects['product_new_info_type_virtual'])
            ui.set_text(self._objects['product_new_info_name'], var_test.get("name"))
            ui.set_text(self._objects['product_new_info_ref'], var_test.get("ref"))
            ui.set_text(self._objects['product_new_info_ean13'], var_test.get("ean13"))
            ui.set_text(self._objects['product_new_info_upc'], var_test.get("upc"))

            if var_test.get("active") == "yes":
                ui.click(self._objects['product_new_info_on'])
            if var_test.get("active") == "no":
                ui.click(self._objects['product_new_info_off'])

            ui.set_text(self._objects['product_new_info_resume'], var_test.get("resume"))
            ui.set_text(self._objects['product_new_info_desc'], var_test.get("desc"))
            ui.set_text(self._objects['product_new_info_tags'], var_test.get("tags").replace('"', ''))
            visibility = ui.def_object(self._objects['product_new_visibility'], var_test.get("visibility"))
            ui.click(visibility)
            condition = ui.def_object(self._objects['product_new_condition'], var_test.get("condition"))
            ui.click(condition)

            ui.click(self._objects['product_new_save_stay'])

            # Fill the Prices part of the product
            ui.click(self._objects['product_new_prices'])
            ui.wait_until(self._objects['product_new_wholesale'][1], 60, 0.25,
                          self._objects['product_new_wholesale'][0])
            ui.set_text(self._objects['product_new_wholesale'], var_test.get("wholesale"), True)
            ui.set_text(self._objects['product_new_price_TE'], var_test.get("priceTE"), True)
            ui.set_text(self._objects['product_new_price_unit'], var_test.get("unit"), True)
            ui.set_text(self._objects['product_new_price_unity'], var_test.get("unity"))
            # ui.set_text(self._objects['product_new_price_on_sale'], var_test.get("onsale"))
            ui.click(self._objects['product_new_save_stay2'])

            # Fill the SEO part of the product
            ui.click(self._objects['product_new_Seo'])
            ui.wait_until(self._objects['product_new_Seo_meta_title'][1], 60, 0.25,
                          self._objects['product_new_Seo_meta_title'][0])
            ui.set_text(self._objects['product_new_Seo_meta_title'], var_test.get("metatitle"), True)
            ui.set_text(self._objects['product_new_Seo_meta_desc'], var_test.get("metadesc"), True)
            if var_test.get("shortlink") != "": ui.set_text(self._objects['product_new_Seo_short_link'],
                                                            var_test.get("shortlink"), True)

        if '1.7' in Configuration().version_presta or '17' in Configuration().version_presta:

            ui.click(self._objects['product_table_id_desc'])
            time.sleep(3)
            max_id = ui.get_text(self._objects['product_table_check']).split("\n")[0]
            ui.click(self._objects['product_add_product'])

            false_random = int(max_id) + 1
            product_name = (Context().browser.name + str(false_random) + var_test.get("name")).replace(" ", "")
            ui.set_text(self._objects['product_new_info_name'], product_name, True)
            var_test['product_name'] = product_name
            var_test['old_max_id'] = max_id

            if Context().environment.my_env == "ADMINDEV":
                try:
                    ui.click(("css", "a.hide-button"), test="yes")
                except:
                    None

            if var_test.get("active") == "yes":
                if Context().browserName == "IE":
                    ui.click(self._objects['product_new_info_activate'])
                    time.sleep(3)
                    ui.click(self._objects['product_new_info_activate'])
                else:
                    ui.click(self._objects['product_new_info_activate'])
                var_test["active_yes"] = "true"
            if var_test.get("active") == "no":
                var_test["active_yes"] = None

            product_type = ui.def_object(self._objects['product_new_info_type'], var_test.get("new_type"))
            ui.click(product_type)
            if var_test.get("new_type") == "1":
                if var_test.get('pack')[0]['search'] != "":
                    i = 1
                    for x_pack in var_test.get('pack'):
                        ui.set_text(self._objects['product_new_pack_search'], x_pack['search'], True)
                        time.sleep(3)
                        my_elem = ui.find_element(self._objects['product_new_pack_search'][0],
                                                  self._objects['product_new_pack_search'][1])
                        my_elem.send_keys(Keys.ARROW_DOWN)
                        my_elem.send_keys(Keys.ENTER)
                        ui.set_text(self._objects['product_new_pack_quantity_product'], x_pack['quantity'], True)
                        ui.click(self._objects['product_new_pack_add'])
                        my_elem.clear()
                        time.sleep(3)

                        pproduit_name = ui.def_object(self._objects['pack_product_name'], i)
                        pproduit_quantity = ui.def_object(self._objects['pack_product_quantity'], i)
                        var_test['pack_product_name_' + str(i)] = \
                        (ui.find_element(pproduit_name[0], pproduit_name[1]).text).split('Size')[0]
                        var_test['pack_product_quantity_' + str(i)] = \
                        (ui.find_element(pproduit_quantity[0], pproduit_quantity[1]).text).split('x')[1]
                        i = i + 1
                    var_test['pack_produit_nb'] = i
            if var_test.get("new_type") == "0" and var_test.get('variation') != "":
                activate_variation = ui.def_object(self._objects['product_new_activate_variation'], 1)
                ui.click(activate_variation)
            elif var_test.get("new_type") == "0" and var_test.get('variation') == "":
                activate_variation = ui.def_object(self._objects['product_new_activate_variation'], 0)
                ui.click(activate_variation)

            ui.click(self._objects['product_new_info_resume'])
            Context().browser.switch_to_frame("form_step1_description_short_1_ifr")
            ui.set_text(self._objects['product_new_info_resume_document'], var_test.get("resume"))
            Context().browser.switch_to_default_content()
            ui.click(self._objects['product_new_info_desc'])
            Context().browser.switch_to_frame("form_step1_description_1_ifr")
            ui.set_text(self._objects['product_new_info_desc_document'], var_test.get("desc"))
            Context().browser.switch_to_default_content()
            time.sleep(5)

            if "//" in var_test.get("picture"):
                img_data_id = []
                nb_img = 0
                for img in var_test.get("picture").split("//"):
                    ui.upload_file(self._objects['product_new_upload_img'], img)
                    nb_img = nb_img + 1

                    if nb_img == 1:
                        ui.wait_until("(//div[@class='dz-preview dz-image-preview ui-sortable-handle dz-complete'])",
                                      90, 1)
                        img_data_id.append(ui.get_attribute(
                            ("xpath", "(//div[@class='dz-preview dz-image-preview ui-sortable-handle dz-complete'])"),
                            "data-id"))
                        var_test['img_list'] = ui.get_attribute(
                            ("xpath", "(//div[@class='dz-preview dz-image-preview ui-sortable-handle dz-complete'])"),
                            "data-id")
                    else:
                        ui.wait_until(
                            "(//div[@class='dz-preview dz-image-preview ui-sortable-handle dz-complete'])[" + str(
                                nb_img) + "]", 90, 1)
                        img_data_id.append(ui.get_attribute(("xpath",
                                                             "(//div[@class='dz-preview dz-image-preview ui-sortable-handle dz-complete'])[" + str(
                                                                 nb_img) + "]"), "data-id"))
                        var_test['img_list'] = var_test['img_list'] + "//" + ui.get_attribute(("xpath",
                                                                                               "(//div[@class='dz-preview dz-image-preview ui-sortable-handle dz-complete'])[" + str(
                                                                                                   nb_img) + "]"),
                                                                                              "data-id")

                var_test['nb_img'] = nb_img
                source = ui.find_element("xpath", "//div[@data-id='" + img_data_id[nb_img - 1] + "']")
                x = ui.find_element("xpath", "//div[@data-id='" + img_data_id[0] + "']").location['x'] - \
                    ui.find_element("xpath", "//div[@data-id='" + img_data_id[nb_img - 1] + "']").location['x'] - 10
                y = ui.find_element("xpath", "//div[@data-id='" + img_data_id[0] + "']").location['y'] - \
                    ui.find_element("xpath", "//div[@data-id='" + img_data_id[nb_img - 1] + "']").location['y'] - 10
                ui.drag_and_drop(source, x, y)
            else:
                time.sleep(3)
                ui.upload_file(self._objects['product_new_upload_img'], var_test.get("picture"))
                ui.wait_until("(//div[@class='dz-preview dz-image-preview ui-sortable-handle dz-complete'])", 90, 1)
                var_test['img_list'] = ui.get_attribute(
                    ("xpath", "(//div[@class='dz-preview dz-image-preview ui-sortable-handle dz-complete'])"),
                    "data-id")
            #
            ui.click(self._objects['product_open_category'])
            if var_test.get('new_category_name') == "1":
                my_cat = (Context().browser.name + str(false_random)).replace(" ", "")
                ui.set_text(self._objects['product_new_info_new_category_name'], my_cat, True)
            else:
                ui.set_text(self._objects['product_new_info_new_category_name'], var_test.get('new_category_name'),
                            True)
            ui.click(self._objects['product_new_info_new_category_save'])
            ui.click(self._objects['product_new_info_category_expand'])
            time.sleep(2)
            if var_test.get('product_category') != "":
                my_category = ui.def_object(self._objects['product_new_info_category_checkbox'],
                                            var_test.get('product_category'))
                ui.click(my_category)
                default_category = ui.def_object(self._objects['product_new_info_default_category'],
                                                 var_test.get('product_category'))
                ui.click(default_category)
                var_test['category_name_save'] = var_test.get('product_category')
            else:
                if var_test.get('new_category_name') == "1":
                    my_category = ui.def_object(self._objects['product_new_info_category_checkbox'], my_cat)
                    ui.checkbox(my_category, "1")
                    default_category = ui.def_object(self._objects['product_new_info_default_category2'], my_cat)
                    ui.click(default_category)
                    var_test['category_name_save'] = my_cat

            ui.click(self._objects['product_open_manufacturer'])
            manufacturer = ui.def_object(self._objects['product_new_manufacturer'], var_test.get("manufacturer"))
            ui.click(manufacturer)
            var_test['manufacturer_check'] = ui.get_text(manufacturer)
            time.sleep(3)
            if var_test.get('search_related_products') != "":
                ui.click(self._objects['product_open_related_product'])
                time.sleep(3)
                if "//" in var_test.get("search_related_products"):
                    i = 1
                    for rel in var_test.get("search_related_products").split("//"):
                        ui.set_text(self._objects['product_new_related_products_search'], rel, True)
                        my_elem = ui.find_element(self._objects['product_new_related_products_search'][0],
                                                  self._objects['product_new_related_products_search'][1])
                        time.sleep(3)
                        my_elem.send_keys(Keys.ARROW_DOWN)
                        my_elem.send_keys(Keys.ENTER)
                        my_elem.clear()
                        related_product_name = ui.def_object(self._objects['related_product_info'], i)
                        var_test['related_product_name_' + str(i)] = \
                        ui.get_text((related_product_name[0], related_product_name[1])).split('\n')[0]
                        i = i + 1
                    var_test['related_product_number'] = i
                else:
                    ui.set_text(self._objects['product_new_related_products_search'],
                                var_test.get("search_related_products"), True)
                    my_elem = ui.find_element(self._objects['product_new_related_products_search'][0],
                                              self._objects['product_new_related_products_search'][1])
                    my_elem.send_keys(Keys.ARROW_DOWN)
                    my_elem.send_keys(Keys.ENTER)
                    my_elem.clear()
                    related_product_name = ui.def_object(self._objects['related_product_info'], 1)
                    var_test['related_product_name_1'] = \
                    ui.get_text((related_product_name[0], related_product_name[1])).split(" (")[0]
            if var_test.get('features') != "":
                ui.click(self._objects['product_open_features'])
                v = 0
                for x_feature in var_test.get('features'):
                    if v > 0:
                        ui.click(self._objects['product_new_info_features_add'])
                    feature_option = ui.def_object(self._objects['product_new_info_features_feature'], v,
                                                   x_feature['feature'])
                    ui.click(feature_option)
                    if x_feature['value'] != "":
                        feature_value = ui.def_object(self._objects['product_new_info_features_value'], v,
                                                      x_feature['value'])
                        ui.click(feature_value)
                    else:
                        feature_value = ui.def_object(self._objects['product_new_info_features_custom_value'], v)
                        ui.set_text(feature_value, x_feature['custom_value'])
                    v = v + 1

            if var_test.get("new_type") == "0" and var_test.get('variation') == "" or var_test.get("new_type") != "0":
                ui.set_text(self._objects['product_new_quantity_quantity_shortcut'], var_test.get("quantity"), True)
                var_test['quantity_totale'] = var_test.get('quantity')
            ui.set_text_script(self._objects['product_new_sell_price_ht_shortcut'], var_test.get("priceTE"))
            ui.set_text(self._objects['product_new_info_ref'], var_test.get("ref"))

            if var_test.get("tax_choosen_shortcut") == "1":
                ui.click(self._objects['product_tax_rules_listbox_shortcut'])
                tax_rule = ui.def_object(self._objects['product_tax_rules_listbox_view_shortcut'],
                                         var_test.get("tax_rule"))
                ui.click(tax_rule)

            ui.click(self._objects['product_new_save'])

            time.sleep(3)

            ui.click(self._objects['product_new_quantity_variation'])
            if var_test.get("new_type") == "1" and var_test.get('pack')[0]['search'] != "":
                quantity_pack = ui.def_object(self._objects['product_new_pack_quantity'], var_test.get('quantity_pack'))
                ui.click(quantity_pack)
            if var_test.get("new_type") == "2":
                if var_test.get("virtual_file") != "":
                    ui.click(self._objects['product_new_virtual_file_yes'])
                    time.sleep(3)
                    ui.upload_file(self._objects['product_new_virtual_file'],
                                   var_test.get("virtual_file")[0]['virtual_file'], True)
                    # ui.set_text(self._objects['product_new_virtual_file_name'],var_test.get("virtual_file")[0]['virtual_file_name'])
                    ui.set_text(self._objects['product_new_virtual_file_nb_download'],
                                var_test.get("virtual_file")[0]['virtual_file_nb_download'])
                    ui.set_text(self._objects['product_new_virtual_file_exp_date'],
                                var_test.get("virtual_file")[0]['virtual_file_exp_date'])
                    ui.set_text(self._objects['product_new_virtual_file_nb_days'],
                                var_test.get("virtual_file")[0]['file_nb_days'], True)
                    ui.click(self._objects['product_new_virtual_file_save'])
                    time.sleep(2)
                else:
                    ui.click(self._objects['product_new_virtual_file_no'])
                    ui.click(self._objects['form_step3_depends_on_stock_1'])
                    ui.set_text(self._objects['product_new_quantity_quantity'], var_test.get("quantity"), True)

                    # product_new_variation_creation
            if var_test.get('variation') != "":
                for x_variation in var_test.get('variation'):
                    for var_x in x_variation['compose'].split('//'):
                        ui.set_text(self._objects['product_new_variation_creation'], var_x, True)
                        my_elem = ui.find_element(self._objects['product_new_variation_creation'][0],
                                                  self._objects['product_new_variation_creation'][1])
                        my_elem.send_keys(Keys.ARROW_DOWN)
                        my_elem.send_keys(Keys.ENTER)
                        my_elem.clear()

                    ui.click(self._objects['product_new_variation_create'])
                    time.sleep(3)

            if var_test.get('variation') != "":
                w = 1

                nb_var = len(ui.find_elements(self._objects['product_new_nb_variation'][0],
                                              self._objects['product_new_nb_variation'][1]))
                for x_variation in var_test.get('variation'):
                    v = ui.get_attribute(ui.def_object(self._objects['product_new_id_variation'], w), "data-index")
                    open_var = ui.def_object(self._objects['product_new_variation_open'], nb_var - 1)
                    ui.click(open_var)
                    ref = ui.def_object(self._objects['product_new_variation_ref'], v)
                    ui.set_text(ref, x_variation['ref'], True)
                    ean13 = ui.def_object(self._objects['product_new_variation_ean13'], v)
                    ui.set_text(ean13, x_variation['ean13'], True)
                    isbn = ui.def_object(self._objects['product_new_variation_isbn'], v)
                    ui.set_text(isbn, x_variation['isbn'], True)
                    upc = ui.def_object(self._objects['product_new_variation_upc'], v)
                    ui.set_text(upc, x_variation['upc'], True)
                    wholesale = ui.def_object(self._objects['product_new_variation_wholesale'], v)
                    ui.set_text(wholesale, x_variation['wholesale'], True)
                    price = ui.def_object(self._objects['product_new_variation_price'], v)
                    ui.set_text(price, x_variation['price'], True)
                    priceTI = ui.def_object(self._objects['product_new_variation_priceTI'], v)
                    ui.set_text(priceTI, x_variation['priceTI'], True)
                    weight = ui.def_object(self._objects['product_new_variation_weight'], v)
                    ui.set_text(weight, x_variation['weight'], True)
                    unity = ui.def_object(self._objects['product_new_variation_unity'], v)
                    ui.set_text(unity, x_variation['unity'], True)
                    minimal_quantity = ui.def_object(self._objects['product_new_variation_minimal_quantity'], v)
                    ui.set_text(minimal_quantity, x_variation['minimal_quantity'], True)
                    available_date = ui.def_object(self._objects['product_new_variation_available_date'], v)
                    ui.set_text(available_date, x_variation['available_date'], True)
                    default = ui.def_object(self._objects['product_new_variation_default'], v)
                    ui.checkbox(default, var_test.get('ad_quantity'))
                    quantity = ui.def_object(self._objects['product_new_variation_quantity'], v)
                    ui.set_text(quantity, x_variation['quantity'], True)

                    if w == 1:
                        var_test['quantity_totale'] = x_variation['quantity']
                        ui.click(self._objects['product_new_variation_open_close'])
                    else:
                        var_test['quantity_totale'] = int(var_test.get('quantity_totale')) + int(
                            x_variation['quantity'])
                        close_var = ui.def_object(self._objects['product_new_variation_open_close2'], w)
                        ui.click(close_var)
                    w = w + 1
                    nb_var = nb_var + 1

            product_out_stock = ui.def_object(self._objects['product_new_quantity_case_out_of_stock'],
                                              var_test.get("out_stock"))
            ui.click(product_out_stock)
            if var_test.get("new_type") == "0" and var_test.get('variation') == "" or var_test.get("new_type") != "0":
                ui.set_text(self._objects['product_new_quantity_minimum'], var_test.get("qty_min"), True)
            ui.set_text(self._objects['product_new_quantity_in_stock'], var_test.get("qty_msg_stock"), True)
            ui.set_text(self._objects['product_new_quantity_out_stock'], var_test.get("qty_msg_unstock"), True)
            if var_test.get('variation') == "":
                ui.set_text(self._objects['product_new_quantity_date_stock'], var_test.get("qty_date"), True)
            var_test['qty_date_for_check'] = ui.get_attribute(self._objects["product_new_quantity_date_stock"], "value")

            ui.click(self._objects['product_new_save'])

            time.sleep(3)

            if var_test.get("new_type") != "2":
                ui.click(self._objects['product_new_carrier_tab'])
                ui.set_text(self._objects['product_new_carrier_width'], var_test.get("cwidth"), True)
                ui.set_text(self._objects['product_new_carrier_height'], var_test.get("cheight"), True)
                ui.set_text(self._objects['product_new_carrier_depth'], var_test.get("cdepth"), True)
                ui.set_text(self._objects['product_new_carrier_weight'], var_test.get("cweight"), True)
                ui.set_text_script(self._objects['product_new_carrier_add_ship_coast'], var_test.get("cadd_ship_coast"))
                carrier = ui.def_object(self._objects['product_new_carrier'], var_test.get("carrier"))
                ui.click(carrier)

                ui.click(self._objects['product_new_save'])

                time.sleep(3)

            ui.click(self._objects['product_new_prices'])
            ui.set_text_script(self._objects['product_new_sell_price_ht'], var_test.get("priceTE"))
            ui.checkbox(self._objects['product_new_price_on_sale'], var_test.get('on_sale'))
            ui.set_text_script(self._objects['product_new_price_ht'], var_test.get("wholesale"))
            ui.set_text_script(self._objects['product_new_price_unit_ht'], var_test.get("unit"))
            ui.set_text_script(self._objects['product_new_price_unity_ht'], var_test.get("unity"))
            if var_test.get("tax_choosen_shortcut") == "0":
                ui.click(self._objects['product_tax_rules_listbox'])
                tax_rule = ui.def_object(self._objects['product_tax_rules_listbox_view'], var_test.get("tax_rule"))
                ui.click(tax_rule)
            """
            if var_test.get('specific_price')!="":
                for x_price in var_test.get('specific_price'):
                    ui.click(self._objects['product_new_specific_price_add'])
                    time.sleep(3)
                    currency=ui.def_object(self._objects['product_new_specific_price_currency'],x_price['currency'])
                    ui.click(currency)
                    country=ui.def_object(self._objects['product_new_specific_price_country'],x_price['country'])
                    ui.click(country)
                    group=ui.def_object(self._objects['product_new_specific_price_group'],x_price['group'])
                    ui.click(group)
                    if var_test.get('variation')!="" and x_price['variation'] == 1:
                        variation=ui.def_object(self._objects['product_new_specific_price_variation'],"1")
                        ui.click(variation)
                    ui.set_text(self._objects['product_new_specific_price_start_date'], x_price['start_date'])
                    ui.set_text(self._objects['product_new_specific_price_end_date'], x_price['end_date'])
                    ui.set_text(self._objects['product_new_specific_price_quantity'], x_price['quantity'],True)
                    ui.set_text_script(self._objects['product_new_specific_price_reduction'], x_price['price'])
                    ui.checkbox(self._objects['product_new_specific_price_show_price'], x_price['show_price'])
                    ui.set_text_script(self._objects['product_new_specific_price_reduction'], x_price['reduction'])
                    reduction_type = ui.def_object(self._objects['product_new_specific_price_reduction_type'],x_price['reduction_type'])
                    ui.click(reduction_type)
                    reduction_tax = ui.def_object(self._objects['product_new_specific_price_reduction_tax'],x_price['reduction_tax'])
                    ui.click(reduction_tax)
                    ui.click(self._objects['product_new_specific_price_save'])
                    time.sleep(3)
            """
            if var_test.get('price_priority') != "":
                v = 0
                for priority in var_test.get('price_priority').split('//'):
                    option = ui.def_object(self._objects['product_new_info_price_priority'], v, priority)
                    ui.click(option)
                    v = v + 1
                ui.checkbox(self._objects['product_new_info_price_priority_apply_to_all'],
                            var_test.get('price_priority_to_all'))
            ui.click(self._objects['product_new_save'])

            time.sleep(3)

            ui.click(self._objects['product_new_ref'])
            ui.set_text(self._objects['product_new_ref_title'], var_test.get("metatitle"))
            ui.set_text(self._objects['product_new_ref_desc'], var_test.get("metadesc"))
            ui.set_text(self._objects['product_new_ref_url'], var_test.get("shortlink"), True)
            ui.click(self._objects['redirection_page_listbox'])
            redirection = ui.def_object(self._objects['redirection_page_listbox_result'],
                                        var_test.get("redirection_page"))
            ui.click(redirection)
            if var_test.get("redirection_page") > str(1):
                ui.set_text(self._objects['redirection_page_target'], var_test.get("redirect_target"), True)
                time.sleep(2)
                my_elem = ui.find_element(self._objects['redirection_page_target'][0],
                                          self._objects['redirection_page_target'][1])
                my_elem.send_keys(Keys.ARROW_DOWN)
                my_elem.send_keys(Keys.ENTER)
                my_elem.clear()
                var_test['redirect_target_name'] = ui.get_text(self._objects['redirect_target_name'])

            ui.click(self._objects['product_new_save'])

            time.sleep(3)

            ui.click(self._objects['product_new_options'])
            visibility = ui.def_object(self._objects['product_new_options_visibility'], var_test.get('visibility'))
            ui.click(visibility)
            ui.checkbox(self._objects['product_new_options_avalaible_orders'], var_test.get('avalaible_orders'))
            ui.checkbox(self._objects['product_new_options_show_price'], var_test.get('show_price'))
            ui.checkbox(self._objects['product_new_options_online_only'], var_test.get('online_only'))
            supplier = ui.def_object(self._objects['product_new_options_suppliers'], var_test.get('options_suppliers'))
            ui.click(supplier)
            default_supplier = ui.def_object(self._objects['product_new_options_default_supplier'],
                                             var_test.get('default_supplier'))
            ui.click(default_supplier)

            ui.set_text(self._objects['product_new_info_upc'], var_test.get("upc"))
            ui.set_text(self._objects['product_new_info_ean13'], var_test.get("ean13"))
            ui.set_text(self._objects['product_new_info_isbn'], var_test.get("isbn"))
            # ui.set_text(self._objects['product_new_info_ref'], var_test.get("ref"))
            condition = ui.def_object(self._objects['product_new_condition'], var_test.get("condition"))
            ui.click(condition)

            if var_test.get('variation') != "":
                v = 0
                for x_variation in var_test.get('variation'):
                    if x_variation['supplier_reference'] != "":
                        supp_ref = ui.def_object(self._objects['product_new_options_supplier_reference'], v)
                        ui.set_text(supp_ref, x_variation['supplier_reference'])
                    else:
                        product = ui.def_object(self._objects['product_new_supplier_name_product'], v + 1)
                        name_product = ui.get_text(product)
                        supp_ref = ui.def_object(self._objects['product_new_options_supplier_reference'], v)
                        ui.set_text(supp_ref, name_product)
                    supp_price = ui.def_object(self._objects['product_new_options_product_price'], v)
                    ui.set_text(supp_price, x_variation['supplier_product_price'], True)
                    currency = ui.def_object(self._objects['product_new_options_price_currency'], v,
                                             x_variation['supplier_product_price_currency'])
                    ui.click(currency)
                    v = v + 1
            else:
                if var_test.get('supplier_reference') != "":
                    supp_ref = ui.def_object(self._objects['product_new_options_supplier_reference'], 0)
                    ui.set_text(supp_ref, product_name)
                else:
                    product = ui.def_object(self._objects['product_new_supplier_name_product'], 0)
                    name_product = ui.get_text(product)
                    supp_ref = ui.def_object(self._objects['product_new_options_supplier_reference'], 0)
                    ui.set_text(supp_ref, name_product)
                supp_price = ui.def_object(self._objects['product_new_options_product_price'], 0)
                ui.set_text(supp_price, var_test.get('product_price'), True)
                currency = ui.def_object(self._objects['product_new_options_price_currency'], 0,
                                         var_test.get('price_currency'))
                ui.click(currency)
            if var_test.get('personalization') != "":
                v = 0
                for x_perso in var_test.get('personalization'):
                    ui.click(self._objects['product_new_personalization_add'])
                    name = ui.def_object(self._objects['product_new_personalization_name'], v)
                    ui.set_text(name, x_perso['name'])
                    my_type = ui.def_object(self._objects['product_new_personalization_type'], v, x_perso['type'])
                    ui.click(my_type)
                    mandatory = ui.def_object(self._objects['product_new_personalization_mandatory'], v)
                    ui.checkbox(mandatory, x_perso['mandatory'])
                    v = v + 1
            if var_test.get('document_attach') != "":
                for x_document in var_test.get('document_attach'):
                    time.sleep(3)
                    ui.upload_file(self._objects['product_new_file_associate'], x_document['file'], True)
                    if x_document['name'] != "":
                        ui.set_text(self._objects['product_new_document_attach_name'], x_document['name'], True)
                    else:
                        ui.set_text(self._objects['product_new_document_attach_name'], x_document['file'], True)
                    ui.set_text(self._objects['product_new_document_attach_desc'], x_document['desc'], True)
                    ui.click(self._objects['product_new_document_attach_add'])
                    time.sleep(3)
            ui.click(self._objects['product_new_save'])

            time.sleep(5)
            try:
                ui.click(self._objects['product_footer_go_to_catalog'])
                time.sleep(5)
                new_product = self.check_product(var_test)
            except:
                None

        return new_product

    def modify_product(self, var_test):

        img_prod1 = ui.def_object(self._objects['col_line_product_table'], 1, 3)
        ui.click(img_prod1)
        time.sleep(3)
        ui.click(self._objects['product_image'])
        time.sleep(3)
        ui.click(self._objects['btn_upload_file'])
        time.sleep(3)
        ui.upload_file(var_test.get("picture"))
        time.sleep(3)
        ui.click(self._objects['file_list'])
        time.sleep(3)
        ui.click(self._objects['btn_file_save'])
        time.sleep(5)
        return True

    def check_product(self, var_test):
        for i in range(1, 10):
            row_product = ui.def_object(self._objects['line_product_table'], i)
            my_product = ui.get_text(row_product)
            if var_test.get('product_name') == str(my_product.split(" ")[0].split("\n")[1]):
                Test.assert_more_or_equal(var_test.get('old_max_id'), ui.find_element(
                    ui.def_object(self._objects['col_line_product_table_first_column'], i, 1)[0],
                    ui.def_object(self._objects['col_line_product_table_first_column'], i, 1)[1]).text,
                                          "'id product' is not bigger than the previous one",
                                          "'id product' is bigger than the previous one")
                Test.assert_equals(str(var_test.get('ref')),
                                   ui.find_element(ui.def_object(self._objects['col_line_product_table'], i, 4)[0],
                                                   ui.def_object(self._objects['col_line_product_table'], i, 4)[
                                                       1]).text, "'reference' hasn't the right value",
                                   "'reference' is ok")
                check_price = var_test.get("priceTE")
                if "." not in check_price:
                    check_price = check_price + ".00"
                check_price = "€" + check_price
                Test.assert_equals(str(check_price),
                                   ui.find_element(ui.def_object(self._objects['col_line_product_table'], i, 6)[0],
                                                   ui.def_object(self._objects['col_line_product_table'], i, 6)[
                                                       1]).text.split(" ")[0], "'price' hasn't the right value",
                                   "'price' is ok")
                Test.assert_equals(int(var_test.get('quantity_totale')), int(
                    ui.find_element(ui.def_object(self._objects['col_line_product_table'], i, 7)[0],
                                    ui.def_object(self._objects['col_line_product_table'], i, 7)[1]).text),
                                   "'quantity' hasn't the right value", "'quantity' is ok")

                col_selected = ui.def_object(self._objects['catalog_open_product'], i, 2)
                ui.click(col_selected)
                try:
                    Test.assert_equals(var_test.get('product_name'),
                                       ui.get_attribute(self._objects["product_new_info_name"], "value"),
                                       "'name' not matching", "'name' is ok")
                    if var_test.get("active") == "yes":
                        try:
                            ui.find_element(self._objects['product_new_info_activate_check'][0],
                                            self._objects['product_new_info_activate_check'][1])
                        except:
                            raise
                    else:
                        try:
                            ui.find_element(self._objects['product_new_info_activate'])
                        except:
                            raise
                    Test.assert_equals(var_test.get('new_type'), ui.find_element('xpath',
                                                                                 '//select[@id="form_step1_type_product"]//option[@selected="selected"]/..').get_attribute(
                        'value'), "'new_type' not matching", "'new_type' is ok")

                    if var_test.get("new_type") == "1" and var_test.get('pack')[0]['search'] != "":
                        my_product = []
                        for i in range(1, var_test.get('pack_produit_nb')):
                            my_product.append((ui.find_element(ui.def_object(self._objects['pack_product_name'], i)[0],
                                                               ui.def_object(self._objects['pack_product_name'], i)[
                                                                   1]).text).split('Size')[0] + "||" + (ui.find_element(
                                ui.def_object(self._objects['pack_product_quantity'], i)[0],
                                ui.def_object(self._objects['pack_product_quantity'], i)[1]).text).split('x')[1])
                        for j in range(1, var_test.get('pack_produit_nb')):
                            Test.assert_equals(var_test.get('pack_product_name_' + str(j)).strip().encode('utf8'),
                                               my_product[j - 1].split('||')[0].strip().encode('utf8'),
                                               "'pack_product_name_" + str(j) + " not matching",
                                               "'pack_product_name_" + str(j) + " is ok")
                            Test.assert_equals(var_test.get('pack_product_quantity_' + str(j)),
                                               my_product[j - 1].split('||')[1],
                                               "'pack_product_quantity_" + str(j) + " not matching",
                                               "'pack_product_quantity_" + str(j) + " is ok")

                    ui.click(self._objects['product_new_info_resume'])
                    Context().browser.switch_to_frame("form_step1_description_short_1_ifr")
                    Test.assert_equals(var_test.get('resume'),
                                       ui.find_element(self._objects['product_new_info_resume_document'][0],
                                                       self._objects['product_new_info_resume_document'][1]).text,
                                       "'resume' not matching", "resume is ok")
                    Context().browser.switch_to_default_content()
                    ui.click(self._objects['product_new_info_desc'])
                    Context().browser.switch_to_frame("form_step1_description_1_ifr")
                    Test.assert_equals(var_test.get('desc'),
                                       ui.find_element(self._objects['product_new_info_desc_document'][0],
                                                       self._objects['product_new_info_desc_document'][1]).text,
                                       "'desc' not matching", "resume is ok")
                    Context().browser.switch_to_default_content()

                    if "//" in var_test.get("picture"):
                        img_data_id = []
                        i = 1
                        while i <= var_test.get('nb_img'):
                            current_picture = ui.def_object(self._objects['product_img'], i + 3)
                            img_data_id.append(ui.get_attribute((current_picture[0], current_picture[1]), "data-id"))
                            i = i + 1
                        j = 0
                        img_data_id.sort()
                        save_data_id = var_test.get('img_list')
                        check_data_id = []
                        for data_id in save_data_id.split("//"):
                            check_data_id.append(data_id)
                        check_data_id.sort()
                        while j < var_test.get('nb_img'):
                            Test.assert_equals(img_data_id[j], check_data_id[j],
                                               "data_id of the picture are not the same, please check the picture saved")
                            j = j + 1
                    if var_test.get("new_type") == "0" and var_test.get('variation') == "" or var_test.get(
                            "new_type") != "0":
                        Test.assert_equals(var_test.get("quantity"),
                                           ui.get_attribute(self._objects["product_new_quantity_quantity_shortcut"],
                                                            "value"), "'quantity' not matching", "'quantity' is ok")
                    check_price = var_test.get("priceTE")
                    if "." not in check_price:
                        check_price = check_price + ".000000"
                    Test.assert_equals(check_price,
                                       ui.get_attribute(self._objects["product_new_sell_price_ht_shortcut"], "value"),
                                       "'priceTE' not matching", "'priceTE' is ok")

                    if var_test.get("new_type") == "0" and var_test.get('variation') != "":
                        Test.assert_equals("true", ui.get_attribute(
                            ui.def_object(self._objects['product_new_activate_variation'], 1), "checked"),
                                           "'priceTE' not matching", "'priceTE' is ok")

                    Test.assert_equals(var_test.get('manufacturer_check'),
                                       ui.find_element(self._objects['product_manufacturer_check'][0],
                                                       self._objects['product_manufacturer_check'][1]).text,
                                       "'product_manufacturer' not matching", "'product_manufacturer' is ok")

                    if var_test.get('search_related_products') != "":
                        if "//" in var_test.get("search_related_products"):
                            i = 1
                            while i < var_test.get('related_product_number'):
                                related_product = ui.def_object(self._objects['related_product_info'], i)
                                Test.assert_equals(
                                    str(var_test.get('related_product_name_' + str(i)).encode('utf8')).split(" (")[0],
                                    str(ui.get_text((related_product[0], related_product[1])).encode('utf8')).split(
                                        " (")[0], "'related_product' not matching", "'related_product' is ok")
                                i = i + 1
                        else:
                            related_product = ui.def_object(self._objects['related_product_info'], 1)
                            Test.assert_equals(var_test.get('related_product_name_1'),
                                               ui.get_attribute((related_product[0], related_product[1]), "value"),
                                               "'related_product' not matching", "'related_product' is ok")

                    if var_test.get('features') != "":
                        v = 0
                        for x_feature in var_test.get('features'):
                            feature_selected = ui.def_object(self._objects['feature_selected'], v)
                            Test.assert_equals(x_feature['feature'],
                                               ui.get_attribute((feature_selected[0], feature_selected[1]), "value"),
                                               "'feature_selected' not matching", "'feature_selected' is ok")

                            if x_feature['value'] != "":
                                feature_value = ui.def_object(self._objects['feature_value'], v)
                                Test.assert_equals(x_feature['value'],
                                                   ui.get_attribute((feature_value[0], feature_value[1]), "value"),
                                                   "'feature_value' not matching", "'feature_value' is ok")
                            else:
                                feature_value = ui.def_object(self._objects['feature_custom_value'], v)
                                Test.assert_equals(x_feature['custom_value'],
                                                   ui.get_attribute((feature_value[0], feature_value[1]), "value"),
                                                   "'feature_value' not matching", "'feature_value' is ok")
                            v = v + 1

                    ui.click(self._objects['product_new_quantity_variation'])

                    if var_test.get("new_type") == "2":
                        if var_test.get("virtual_file") != "":
                            Test.assert_equals("true", ui.get_attribute(self._objects["product_new_virtual_file_yes"],
                                                                        "checked"),
                                               "'virtual file attached' not matching", "'virtual file attached' is ok")
                            Test.assert_equals(var_test.get("virtual_file")[0]['virtual_file'],
                                               ui.get_attribute(self._objects["product_new_virtual_file_name"],
                                                                "value"), "'virtual_file_name' not matching",
                                               "'virtual_file_name' is ok")
                            Test.assert_equals(var_test.get("virtual_file")[0]['virtual_file_nb_download'],
                                               ui.get_attribute(self._objects["product_new_virtual_file_nb_download"],
                                                                "value"), "'virtual_file_nb_download' not matching",
                                               "'virtual_file_nb_download' is ok")
                            Test.assert_equals(var_test.get("virtual_file")[0]['file_nb_days'],
                                               ui.get_attribute(self._objects["product_new_virtual_file_nb_days"],
                                                                "value"), "'file_nb_days' not matching",
                                               "'file_nb_days' is ok")
                        else:
                            Test.assert_equals("true", ui.get_attribute(self._objects["product_new_virtual_file_no"],
                                                                        "checked"),
                                               "'virtual file attached' not matching", "'virtual file attached' is ok")

                    if var_test.get('variation') != "":
                        v = 1
                        for x_variation in var_test.get('variation'):
                            quantity_var = ui.def_object(self._objects['product_new_variation_line_quantity'], v)
                            Test.assert_equals(x_variation['quantity'],
                                               ui.get_attribute((quantity_var[0], quantity_var[1]), "value"),
                                               "'quantity variation' not matching", "'quantity variation' is ok")
                            v = v + 1
                    else:
                        Test.assert_equals(var_test.get("quantity"),
                                           ui.get_attribute(self._objects['product_new_quantity_quantity'], "value"),
                                           "'quantity' not matching", "'quantity' is ok")

                    if var_test.get("new_type") == "1" and var_test.get('pack')[0]['search'] != "":
                        Test.assert_equals(var_test.get("quantity_pack"), ui.get_attribute((self._objects[
                                                                                                'product_new_pack_quantity_check'][
                                                                                                0], self._objects[
                                                                                                'product_new_pack_quantity_check'][
                                                                                                1]), 'value'),
                                           "'quantity_pack' not matching", "'quantity_pack' is ok")
                    if var_test.get("new_type") != "0" or var_test.get("new_type") == "" and var_test.get(
                            'variation') == "":
                        Test.assert_equals(var_test.get('qty_min'),
                                           ui.get_attribute(self._objects["product_new_quantity_minimum"], "value"),
                                           "'qty_min' not matching", "'qty_min' is ok")

                    Test.assert_equals(var_test.get("out_stock"), ui.get_attribute(
                        ("xpath", "//div[@id=\"form_step3_out_of_stock\"]/div/label/input[@checked]"), "value"),
                                       "'out_stock variation' not matching", "'out_stock variation' is ok")
                    Test.assert_equals(var_test.get('qty_msg_stock'),
                                       ui.get_attribute(self._objects["product_new_quantity_in_stock"], "value"),
                                       "'qty_msg_stock' not matching", "'qty_msg_stock' is ok")
                    Test.assert_equals(var_test.get('qty_msg_unstock'),
                                       ui.get_attribute(self._objects["product_new_quantity_out_stock"], "value"),
                                       "'qty_msg_unstock' not matching", "'qty_msg_unstock' is ok")

                    if var_test.get('variation') == "":
                        Test.assert_equals(var_test.get('qty_date_for_check'),
                                           ui.get_attribute(self._objects["product_new_quantity_date_stock"], "value"),
                                           "'qty_date' not matching", "'qty_date' is ok")

                    if var_test.get("new_type") != "2":
                        ui.click(self._objects['product_new_carrier_tab'])
                        Test.assert_equals(var_test.get('cwidth'),
                                           ui.get_attribute(self._objects["product_new_carrier_width"], "value"),
                                           "'cwidth' not matching", "'cwidth' is ok")
                        Test.assert_equals(var_test.get('cheight'),
                                           ui.get_attribute(self._objects["product_new_carrier_height"], "value"),
                                           "'cheight' not matching", "'cheight' is ok")
                        Test.assert_equals(var_test.get('cdepth'),
                                           ui.get_attribute(self._objects["product_new_carrier_depth"], "value"),
                                           "'new_type' not matching", "'cdepth' is ok")
                        Test.assert_equals(var_test.get('cweight'),
                                           ui.get_attribute(self._objects["product_new_carrier_weight"], "value"),
                                           "'cweight' not matching", "'cweight' is ok")
                        if "." not in var_test.get('cadd_ship_coast'):
                            cadd_ship_coast_check = var_test.get('cadd_ship_coast') + ".000000"
                        else:
                            cadd_ship_coast_check = var_test.get('cadd_ship_coast')
                        Test.assert_equals(str(cadd_ship_coast_check), str(
                            ui.get_attribute(self._objects["product_new_carrier_add_ship_coast"], "value")),
                                           "'cadd_ship_coast' not matching", "'cadd_ship_coast' is ok")
                        carrier_check = ui.def_object(self._objects['product_new_carrier_check'],
                                                      var_test.get("carrier"))
                        Test.assert_equals("true", ui.get_attribute((carrier_check[0], carrier_check[1]), "checked"),
                                           "'product_new_carrier' not matching", "'product_new_carrier' is ok")

                    ui.click(self._objects['product_new_prices'])
                    check_price = var_test.get("priceTE")
                    if "." not in check_price:
                        check_price = check_price + ".000000"
                    Test.assert_equals(check_price,
                                       ui.get_attribute(self._objects["product_new_sell_price_ht"], "value"),
                                       "'priceTE' not matching", "'priceTE' is ok")
                    if var_test.get('on_sale') == "0":
                        Test.assert_equals("None",
                                           str(ui.get_attribute(self._objects['product_new_price_on_sale'], "checked")),
                                           "'product_new_carrier' not matching", "'product_new_carrier' is ok")
                    else:
                        Test.assert_equals("true",
                                           ui.get_attribute(self._objects['product_new_price_on_sale'], "checked"),
                                           "'product_new_carrier' not matching", "'product_new_carrier' is ok")

                    wholesale = var_test.get('wholesale')
                    if "." not in wholesale:
                        wholesale = wholesale + ".000000"
                    Test.assert_equals(wholesale, ui.get_attribute(self._objects["product_new_price_ht"], "value"),
                                       "'wholesale' not matching", "'wholesale' is ok")
                    Test.assert_equals(var_test.get('unity'),
                                       ui.get_attribute(self._objects["product_new_price_unity_ht"], "value"),
                                       "'unity' not matching", "'unity' is ok")

                    ui.click(self._objects['product_new_ref'])
                    Test.assert_equals(var_test.get('metatitle'), ui.get_attribute(
                        (self._objects['product_new_ref_title'][0], self._objects['product_new_ref_title'][1]),
                        'value'), "'metatitle' not matching", "'metatitle' is ok")
                    Test.assert_equals(var_test.get('metadesc'), ui.get_attribute(
                        (self._objects['product_new_ref_desc'][0], self._objects['product_new_ref_desc'][1]), 'value'),
                                       "'metadesc' not matching", "'metadesc' is ok")
                    Test.assert_equals(var_test.get('shortlink'), ui.get_attribute(
                        (self._objects['product_new_ref_url'][0], self._objects['product_new_ref_url'][1]), 'value'),
                                       "'shortlink' not matching", "'shortlink' is ok")

                    ui.click(self._objects['product_new_options'])
                    Test.assert_equals(var_test.get('upc'),
                                       ui.get_attribute(self._objects["product_new_info_upc"], "value"),
                                       "'upc' not matching", "'upc' is ok")
                    Test.assert_equals(var_test.get('ean13'),
                                       ui.get_attribute(self._objects["product_new_info_ean13"], "value"),
                                       "'ean13' not matching", "'ean13' is ok")
                    Test.assert_equals(var_test.get('isbn'),
                                       ui.get_attribute(self._objects["product_new_info_isbn"], "value"),
                                       "'isbn' not matching", "'isbn' is ok")
                    Test.assert_equals(var_test.get('ref'),
                                       ui.get_attribute(self._objects["product_new_info_ref"], "value"),
                                       "'ref' not matching", "'ref' is ok")
                    if var_test.get("new_type") != "2":
                        Test.assert_equals(var_test.get("condition"), ui.get_attribute((self._objects[
                                                                                            'product_new_condition_check'][
                                                                                            0], self._objects[
                                                                                            'product_new_condition_check'][
                                                                                            1]), 'value'),
                                           "'condition' not matching", "'condition' is ok")
                    else:
                        Test.assert_equals("new", ui.get_attribute((self._objects['product_new_condition_check'][0],
                                                                    self._objects['product_new_condition_check'][1]),
                                                                   'value'), "'condition' not matching",
                                           "'condition' is ok")

                    Test.assert_equals(var_test.get('visibility'),
                                       ui.get_attribute(self._objects["new_product_visibility_check"], "value"),
                                       "'visibility' not matching", "'visibility' is ok")
                    Test.assert_equals("true", ui.get_attribute(self._objects["product_new_options_avalaible_orders"],
                                                                "checked"), "'avalaible_orders' not matching",
                                       "'avalaible_orders' is ok")
                    Test.assert_equals("true",
                                       ui.get_attribute(self._objects["product_new_options_show_price"], "checked"),
                                       "'show_price' not matching", "'show_price' is ok")
                    Test.assert_equals("true",
                                       ui.get_attribute(self._objects["product_new_options_online_only"], "checked"),
                                       "'online_only' not matching", "'online_only' is ok")
                    Test.assert_equals("true",
                                       ui.get_attribute(self._objects["product_new_options_suppliers"], "checked"),
                                       "'options_suppliers' not matching", "'options_suppliers' is ok")
                    Test.assert_equals(var_test.get('default_supplier'),
                                       ui.get_attribute(self._objects["new_product_default_supplier_check"], "value"),
                                       "'default_supplier' not matching", "'default_supplier' is ok")

                    if var_test.get('variation') != "":
                        v = 0
                        for x_variation in var_test.get('variation'):
                            if x_variation['supplier_reference'] != "":
                                supp_ref = ui.def_object(self._objects['product_new_options_supplier_reference'], v)
                                Test.assert_equals(x_variation['supplier_reference'],
                                                   ui.get_attribute((supp_ref[0], supp_ref[1]), "value"),
                                                   "'supplier_reference' not matching", "'supplier_reference' is ok")
                            else:
                                product = ui.def_object(self._objects['product_new_supplier_name_product'], v + 1)
                                name_product = ui.get_text(product)
                                supp_ref = ui.def_object(self._objects['product_new_options_supplier_reference'], v)
                                Test.assert_equals(name_product, ui.get_attribute((supp_ref[0], supp_ref[1]), "value"),
                                                   "'supplier_reference' not matching", "'supplier_reference' is ok")
                            supp_price = ui.def_object(self._objects['product_new_options_product_price'], v)
                            supplier_product_price = x_variation['supplier_product_price']
                            if "." not in supplier_product_price:
                                supplier_product_price = supplier_product_price + ".000000"
                            Test.assert_equals(supplier_product_price,
                                               ui.get_attribute((supp_price[0], supp_price[1]), "value"),
                                               "'supplier_product_price' not matching",
                                               "'supplier_product_price' is ok")
                            currency = ui.def_object(self._objects['product_new_options_price_currency_check'], v,
                                                     x_variation['supplier_product_price_currency'])
                            Test.assert_equals(x_variation['supplier_product_price_currency'],
                                               ui.get_attribute((currency[0], currency[1]), "value"),
                                               "'default_supplier' not matching", "'default_supplier' is ok")
                            v = v + 1
                    else:
                        if var_test.get('supplier_reference') != "":
                            supp_ref = ui.def_object(self._objects['product_new_options_supplier_reference'], 0)
                            Test.assert_equals(var_test.get('product_name'),
                                               ui.get_attribute((supp_ref[0], supp_ref[1]), "value"),
                                               "'supplier_reference' not matching", "'supplier_reference' is ok")
                        else:
                            product = ui.def_object(self._objects['product_new_supplier_name_product'])
                            name_product = ui.get_text(product)
                            supp_ref = ui.def_object(self._objects['product_new_options_supplier_reference'], 0)
                            Test.assert_equals(name_product, ui.get_attribute((supp_ref[0], supp_ref[1]), "value"),
                                               "'supplier_reference' not matching", "'supplier_reference' is ok")
                        supp_price = ui.def_object(self._objects['product_new_options_product_price'], 0)
                        supplier_product_price = var_test.get('product_price')
                        if "." not in supplier_product_price:
                            supplier_product_price = supplier_product_price + ".000000"
                        Test.assert_equals(supplier_product_price,
                                           ui.get_attribute((supp_price[0], supp_price[1]), "value"),
                                           "'supplier_product_price' not matching", "'supplier_product_price' is ok")
                        currency = ui.def_object(self._objects['product_new_options_price_currency_check'], 0)
                        Test.assert_equals(var_test.get('price_currency'),
                                           ui.get_attribute((currency[0], currency[1]), "value"),
                                           "'default_supplier' not matching", "'default_supplier' is ok")

                    if var_test.get('personalization') != "":
                        v = 0
                        for x_perso in var_test.get('personalization'):
                            name = ui.def_object(self._objects['product_new_personalization_name'], v)
                            Test.assert_equals(x_perso['name'], ui.get_attribute((name[0], name[1]), "value"),
                                               "'product_new_personalization_name' not matching",
                                               "'product_new_personalization_name' is ok")
                            my_type = ui.def_object(self._objects['product_new_personalization_type'], v,
                                                    x_perso['type'])
                            Test.assert_equals(x_perso['type'], ui.get_attribute((my_type[0], my_type[1]), "value"),
                                               "'default_supplier' not matching", "'default_supplier' is ok")
                            mandatory = ui.def_object(self._objects['product_new_personalization_mandatory'], v)
                            if x_perso['mandatory'] == str(1):
                                Test.assert_equals("true", ui.get_attribute((mandatory[0], mandatory[1]), "checked"),
                                                   "'mandatory' not matching", "'mandatory' is ok")
                            else:
                                Test.assert_equals("None",
                                                   str(ui.get_attribute((mandatory[0], mandatory[1]), "checked")),
                                                   "'mandatory' not matching", "'mandatory' is ok")
                            v = v + 1

                    return True
                except:
                    return False

    def product_catalog_sort(self, var_test):
        sort_product = False
        try:
            elem_per_page = ui.find_element(self._objects['catalog_number_element_per_page'], no_log=True)
            nb_elem_per_page = elem_per_page.text
        except:
            nb_elem_per_page = "20"
        if nb_elem_per_page != "20":
            def_nb_page = ui.def_object(self._objects['catalog_change_number_element_per_page'], "20")
            ui.click(def_nb_page)

        i = 1
        while i != -1:
            try:
                ligne_table = ui.def_object(self._objects['line_product_table'], i)
                ui.find_element(ligne_table[0], ligne_table[1], not_log=True)
                i = i + 1
            except:
                nb_element = i - 1
                i = -1
        # asc
        for col in var_test.get("col_search").split("//"):
            try:
                current_element_number = 1
                col_sort = ui.def_object(self._objects['catalog_sort_col'], col.split('||')[0], "asc")
                ui.click(col_sort)
                product_list = []
                product_list2 = []
                while int(current_element_number) <= int(nb_element):
                    if col.split('||')[1] == "1":
                        product_list.append(int(ui.find_element(
                            ui.def_object(self._objects['col_line_product_table_first_column'], current_element_number,
                                          1)[0],
                            ui.def_object(self._objects['col_line_product_table_first_column'], current_element_number,
                                          1)[1]).text))
                    elif col.split('||')[1] == "6":
                        element_value = ui.get_text(
                            ui.def_object(self._objects['col_line_product_table'], current_element_number,
                                          col.split('||')[1])).split(' ')[0].replace(',', '.')
                        product_list.append(float(element_value))
                    elif col.split('||')[1] == "8":
                        product_list.append(int(ui.get_text(
                            ui.def_object(self._objects['col_line_product_table'], current_element_number,
                                          col.split('||')[1]))))
                    elif col.split('||')[1] == "9":
                        product_list.append(ui.get_attribute(
                            ui.def_object(self._objects['col_line_product_table_activate'], current_element_number,
                                          col.split('||')[1]), "onClick"))
                    else:
                        product_list.append(ui.get_text(
                            ui.def_object(self._objects['col_line_product_table'], current_element_number,
                                          col.split('||')[1])))
                    current_element_number = current_element_number + 1
                product_list2 = product_list
                product_list2.sort()
                i = 0
                while int(i) < int(nb_element):
                    Test.assert_equals(product_list[i], product_list2[i], "value isn't ok")
                    i = i + 1
            except:
                raise
        # desc
        for col in var_test.get("col_search").split("//"):
            current_element_number = 1
            col_sort = ui.def_object(self._objects['catalog_sort_col'], col.split('||')[0], "desc")
            ui.click(col_sort)
            product_list = []
            product_list2 = []
            while int(current_element_number) <= int(nb_element):
                if col.split('||')[1] == "1":
                    product_list.append(int(ui.find_element(
                        ui.def_object(self._objects['col_line_product_table_first_column'], current_element_number, 1)[
                            0],
                        ui.def_object(self._objects['col_line_product_table_first_column'], current_element_number, 1)[
                            1]).text))
                elif col.split('||')[1] == "6":
                    element_value = ui.get_text(
                        ui.def_object(self._objects['col_line_product_table'], current_element_number,
                                      col.split('||')[1])).split(' ')[0].replace(',', '.')
                    product_list.append(float(element_value))
                elif col.split('||')[1] == "8":
                    product_list.append(int(ui.get_text(
                        ui.def_object(self._objects['col_line_product_table'], current_element_number,
                                      col.split('||')[1]))))
                elif col.split('||')[1] == "9":
                    product_list.append(ui.get_attribute(
                        ui.def_object(self._objects['col_line_product_table_activate'], current_element_number,
                                      col.split('||')[1]), "onClick"))
                else:
                    product_list.append(ui.get_text(
                        ui.def_object(self._objects['col_line_product_table'], current_element_number,
                                      col.split('||')[1])))
                current_element_number = current_element_number + 1
            product_list2 = product_list
            product_list2.sort(reverse=True)
            i = 0
            while int(i) < int(nb_element):
                Test.assert_equals(product_list[i], product_list2[i], "value isn't ok")
                i = i + 1
        sort_product = True
        return sort_product


