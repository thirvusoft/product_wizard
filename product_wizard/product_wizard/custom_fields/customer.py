from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def create_customer_fields():
    custom_fields = {
		"Customer": [
			dict(fieldname='user_id', label='User ID',
				fieldtype='Link',options='User', insert_after='naming_series', allow_on_submit=1)
			]
    }
    create_custom_fields(custom_fields)