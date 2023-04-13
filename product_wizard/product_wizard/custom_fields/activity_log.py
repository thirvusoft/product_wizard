from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def create_activity_log_fields():
    custom_fields = {
		"Customer": [
			dict(fieldname='location', label='Location',
				fieldtype='Small Text', insert_after='user')
			]
    }
    create_custom_fields(custom_fields)