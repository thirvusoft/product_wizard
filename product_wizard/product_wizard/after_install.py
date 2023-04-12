import frappe
from product_wizard.product_wizard.custom_fields.customer import create_customer_fields

def after_install():
    create_customer_fields()