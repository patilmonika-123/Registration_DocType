# Copyright (c) 2013, Monika and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)

	data = get_data(filters)
	return columns, data

def get_columns(filters):
	columns = [
		{
			"label": _("Customer"),
			"fieldtype": "Link",
			"fieldname": "customer",
			"options": "Customer",
			"width":150


		},
		{
			"label": _("Company"),
			"fieldtype": "Link",
			"fieldname": "company",
			"options": "Company"
		},
		{
			"label": _("Posting Date"),
			"fieldtype": "Date",
			"fieldname": "posting_date"
		},
		{
			"label": _("Total"),
			"fieldname": "total",
			"options": "Currency",
			"width":100
		},
	]

	return columns

def get_data(filters):
	print(filters.get("start_date"),filters.get("end_date"))

	data = frappe.db.sql("""select customer,company,posting_date,total from `tabSales Invoice` where total>'{2}' and posting_date BETWEEN '{0}' and '{1}' """.format(filters.get("start_date"),filters.get("end_date"),filters.get("total")))
	
	return data
