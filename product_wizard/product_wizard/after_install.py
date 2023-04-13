import frappe
from product_wizard.product_wizard.custom_fields.customer import create_customer_fields
from product_wizard.product_wizard.custom_fields.activity_log import create_activity_log_fields

def after_install():
    create_customer_fields()
    create_activity_log_fields()