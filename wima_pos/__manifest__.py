{
    'name' : 'Wima POS',
    'version' : '2.0',
    'summary' : 'BU for POS Modul',
    'author': "Catur Kurniawan",
    'description' : """
All in One Wima Pos Module
    """,
    'category' : 'WIma',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'depends': [
        'web',
        'sms',
        'base_setup',
        # 'point_of_sale',
        # 'stock',
        # 'product_margin',
        # 'sale_management',
        # 'contacts',
        # 'purchase',
        # 'hr_expense',
        'l10n_id_mceasy',
        # 'purchase_stock',
        'mass_mailing',
    ],
    'data': [
        # rules
        # 'partner/security/rule.xml',
        # 'sales/security/rule.xml',
        # 'after_sales/security/rule.xml',
        # 'service/security/rule.xml',
        # 'subscription/security/rule.xml',
        # 'approval/security/rule.xml',
        # common
        'common/security/ir.model.access.csv',
        'common/views/mceasy_default_layout.xml',
        'common/views/res_users_views.xml',
        'common/views/external_template.xml',
        'common/views/city.xml',
        'common/wizard/wizard_external_template.xml',
        'common/data/report_layout.xml',
        'common/data/data_provinsi.xml',
        'common/data/data_city.xml',
        # 'common/data/template_contract.xml',
        # 'common/data/template_quotation.xml',
        # 'common/data/template_sale_order.xml',
        # 'common/data/template_invoice.xml',
        # 'common/data/template_promotion.xml',
        # menu
        'menu/views/webclient_templates.xml',
        # efaktur
        'efaktur/security/ir.model.access.csv',
        'efaktur/views/account_move_views.xml',
        'efaktur/views/efaktur_views.xml',
        'efaktur/views/res_config_settings_views.xml',
        'efaktur/views/res_partner_views.xml',
        # accounting
        'accounting/data/account_accountant_data.xml',
        'accounting/data/ir_cron.xml',
        'accounting/data/digest_data.xml',
        'accounting/data/pdf_export_templates.xml',
        'accounting/data/balance_sheet.xml',
        'accounting/data/cash_flow_report.xml',
        'accounting/data/executive_summary.xml',
        'accounting/data/profit_and_loss.xml',
        'accounting/data/aged_partner_balance.xml',
        'accounting/data/general_ledger.xml',
        'accounting/data/trial_balance.xml',
        'accounting/data/sales_report.xml',
        'accounting/data/partner_ledger.xml',
        'accounting/data/multicurrency_revaluation_report.xml',
        'accounting/data/deferred_reports.xml',
        'accounting/data/journal_report.xml',
        'accounting/data/generic_tax_report.xml',
        'accounting/data/mail_activity_type_data.xml',
        'accounting/security/ir.model.access.csv',
        'accounting/security/account_accountant_security.xml',
        'accounting/views/account_account_views.xml',
        'accounting/views/account_fiscal_year_view.xml',
        'accounting/views/account_journal_dashboard_views.xml',
        'accounting/views/account_move_views.xml',
        'accounting/views/account_payment_views.xml',
        'accounting/views/account_reconcile_views.xml',
        'accounting/views/account_reconcile_model_views.xml',
        'accounting/views/account_accountant_menuitems.xml',
        'accounting/views/digest_views.xml',
        'accounting/views/account_budget_views.xml',
        'accounting/views/account_analytic_account_views.xml',
        'accounting/views/res_config_settings_views.xml',
        'accounting/views/product_views.xml',
        'accounting/views/bank_rec_widget_views.xml',
        'accounting/views/account_report_view.xml',
        'accounting/data/assets_report.xml',
        'accounting/data/account_report_actions.xml',
        'accounting/views/account_tax_views.xml',
        'accounting/views/mail_activity_views.xml',
        'accounting/views/partner_view.xml',
        'accounting/views/report_template.xml',
        'accounting/views/res_company_views.xml',
        'accounting/data/account_followup_data.xml',
        'accounting/wizard/followup_manual_reminder_views.xml',
        'accounting/wizard/followup_missing_information.xml',
        'accounting/views/account_followup_views.xml',
        'accounting/views/account_journal_dashboard_view.xml',
        'accounting/wizard/account_change_lock_date.xml',
        'accounting/wizard/account_auto_reconcile_wizard.xml',
        'accounting/wizard/account_reconcile_wizard.xml',
        'accounting/wizard/reconcile_model_wizard.xml',
        'accounting/wizard/account_report_file_download_error_wizard.xml',
        'accounting/wizard/fiscal_year.xml',
        'accounting/wizard/mail_activity_schedule_views.xml',
        'accounting/wizard/multicurrency_revaluation.xml',
        'accounting/wizard/report_export_wizard.xml',
        'accounting/views/account_activity.xml',
        'accounting/security/account_asset_security.xml',
        'accounting/views/account_asset_views.xml',
        'accounting/views/account_journal.xml',
        'accounting/data/menuitems.xml',
        'accounting/views/report_followup.xml',
        'accounting/security/account_budget_security.xml',
        'accounting/security/account_auto_transfer_security.xml',
        'accounting/views/transfer_model_views.xml',
        'accounting/views/account_followup_line_views.xml',
        'accounting/security/account_followup_security.xml',
        'accounting/security/sms_security.xml',
        'accounting/data/account_data.xml',
        # POS
        # 'pos/views/pos_receipt_template.xml'
        # partner
        # 'partner/data/data.xml',
        # 'partner/views/res_partner.xml',
        # 'partner/security/ir.model.access.csv',
        # 'partner/views/menus.xml',
        # 'partner/views/res_partner_size.xml',
        # inventory
        # 'inventory/security/ir.model.access.csv',
        # 'inventory/views/product_component.xml',
        # 'inventory/views/product_operation_views.xml',
        # 'inventory/views/inventory_menus.xml',
        # 'inventory/views/product_template_inherit_form.xml',
        # 'inventory/views/stock_picking_inherit_form.xml',
        # 'inventory/views/stock_move_line_inherit_tree.xml',
        # 'inventory/views/stock_route_inherit_form.xml',
        # 'inventory/views/stock_picking_type_inherit_form.xml',
        # 'inventory/views/stock_quant_inherit_views.xml',
        # 'inventory/data/uom_data.xml',
        # 'inventory/data/component_type.xml',
        # 'inventory/data/warehouse.xml',
        # 'inventory/data/product_operation_template.xml',
        # sales
        # 'sales/report/quotation.xml',
        # 'sales/report/contract.xml',
        # 'sales/views/promotion.xml',
        # 'sales/views/quotation.xml',
        # 'sales/views/contract.xml',
        # 'sales/views/contract_period.xml',
        # 'sales/views/pricelist.xml',
        # 'sales/views/sale_order.xml',
        # 'sales/views/crm_category.xml',
        # 'sales/views/crm_team.xml',
        # 'sales/report/proforma.xml',
        # 'sales/views/menus.xml',
        # 'sales/security/ir.model.access.csv',
        # 'sales/data/sequence.xml',
        # 'sales/data/crm_category.xml',
        # 'sales/data/contract_period.xml',
        # after sales
        # 'after_sales/data/sequence.xml',
        # 'after_sales/views/after_sale_views.xml',
        # 'after_sales/views/menus.xml',
        # 'after_sales/security/ir.model.access.csv',
        # sevice
        # 'service/report/implementation_bast.xml',
        # 'service/views/work_order.xml',
        # 'service/views/outstanding_work_order.xml',
        # 'service/views/entity_asset.xml',
        # 'service/views/entity_asset_specification.xml',
        # 'service/views/partner_domain.xml',
        # 'service/views/toplevel_domain.xml',
        # 'service/views/menus.xml',
        # 'service/security/ir.model.access.csv',
        # 'service/data/sequence.xml',
        # subscription
        # 'subscription/data/sequence.xml',
        # 'subscription/data/recurring_plan.xml',
        # 'subscription/security/ir.model.access.csv',
        # 'subscription/views/subscription.xml',
        # 'subscription/views/subscription_line.xml',
        # 'subscription/views/subscription_plan_views.xml',
        # 'subscription/views/account_move_inherit_form.xml',
        # 'subscription/views/account_move_inherit_tree.xml',
        # 'subscription/views/account_move_inherit_search.xml',
        # 'subscription/views/menus.xml',
        # 'subscription/report/invoice.xml',

        # "purchasing/security/purchase_request.xml",
        # "purchasing/security/ir.model.access.csv",
        # "purchasing/data/purchase_request_sequence.xml",
        # "purchasing/data/purchase_request_data.xml",
        # "purchasing/reports/report_purchase_request.xml",
        # "purchasing/wizard/purchase_request_line_make_purchase_order_view.xml",
        # "purchasing/views/purchase_request_view.xml",
        # "purchasing/views/purchase_request_line_view.xml",
        # "purchasing/views/purchase_request_report.xml",
        # "purchasing/views/product_template.xml",
        # "purchasing/views/purchase_order_view.xml",
        # "purchasing/views/stock_move_views.xml",

        # Approval Managament
        # 'approval/security/ir.model.access.csv',
        # 'approval/views/approval_views.xml',
        # 'approval/views/dashboard_approval_views.xml',
        # 'approval/views/approval_line_views.xml',
        # 'approval/wizard/approval_reject_wizard_views.xml',
        # 'approval/data/user.xml',
        # 'approval/data/configuration.xml',

        # Mailing
        'mailing/views/menus.xml',
        'mailing/views/mailing_contact_views.xml',
        'mailing/views/mailing_views.xml'
    ],
    'assets': {
        # 'point_of_sale.asset': ['wima_pos/pos/static/src/js/pos_custom.js'],
        'wima_pos.assets_pdf_export': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap_backend'),
            'web/static/fonts/fonts.scss',
            'wima_pos/static/src/scss/**/*',
        ],
        'wima_pos.assets_followup_report': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap_backend'),
            'web/static/fonts/fonts.scss',
        ],
        'web.report_assets_common': [
            'wima_pos/static/src/scss/account_pdf_export_template.scss',
            'wima_pos/static/src/scss/report_mceasy.scss',
        ],
        'web._assets_primary_variables': [
            ('after', 'web/static/src/scss/primary_variables.scss', 'wima_pos/static/src/**/*.variables.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'wima_pos/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'wima_pos/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_backend_helpers': [
            ('before', 'web/static/src/scss/bootstrap_overridden.scss', 'wima_pos/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            'wima_pos/static/src/webclient/home_menu/home_menu_background.scss',
            'wima_pos/static/src/webclient/navbar/navbar.scss',
        ],
        'web.assets_backend': [
            'wima_pos/static/src/webclient/**/*.scss',
            'wima_pos/static/src/views/**/*.scss',
            'wima_pos/static/src/components/**/*',
            'wima_pos/static/src/js/**/*',
            'wima_pos/static/src/fields/*',
            'wima_pos/static/src/widgets/**/*',
            'wima_pos/static/src/core/**/*',
            'wima_pos/static/src/webclient/**/*.js',
            'wima_pos/static/src/webclient/**/*.xml',
            'wima_pos/static/src/views/**/*.js',
            'wima_pos/static/src/views/**/*.xml',

            ('remove', 'wima_pos/static/src/**/*.dark.scss'),
        ],
        'web.assets_web': [
            ('replace', 'web/static/src/main.js', 'wima_pos/static/src/main.js'),
        ],
        # ========= Dark Mode =========
        "web.dark_mode_variables": [
            # web._assets_primary_variables
            ('before', 'wima_pos/static/src/scss/primary_variables.scss', 'wima_pos/static/src/scss/primary_variables.dark.scss'),
            ('before', 'wima_pos/static/src/**/*.variables.scss', 'wima_pos/static/src/**/*.variables.dark.scss'),
            # web._assets_secondary_variables
            ('before', 'wima_pos/static/src/scss/secondary_variables.scss', 'wima_pos/static/src/scss/secondary_variables.dark.scss'),
        ],
        "web.assets_web_dark": [
            ('include', 'web.dark_mode_variables'),
            # web._assets_backend_helpers
            ('before', 'wima_pos/static/src/scss/bootstrap_overridden.scss', 'wima_pos/static/src/scss/bootstrap_overridden.dark.scss'),
            ('after', 'web/static/lib/bootstrap/scss/_functions.scss', 'wima_pos/static/src/scss/bs_functions_overridden.dark.scss'),
            # assets_backend
            'wima_pos/static/src/**/*.dark.scss',
            'wima_pos/static/src/scss/*.dark.scss',
        ],
    },
    'pre_init_hook': '_pre_init_hook',
    'post_init_hook': '_post_init_hook',
    'uninstall_hook': "uninstall_hook",
}