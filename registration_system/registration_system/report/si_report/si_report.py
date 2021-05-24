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
			"label": _("Item  code"),
			"fieldtype": "Link",
			"fieldname": "item_code",
			"options": "Item",
			"width":100
		},
		{
			"label": _("Item Name"),
			"fieldtype": "Data",
			"fieldname": "item_name",
			"width":100
		},
		{
			"label": _("Quantity"),
			"fieldtype": "Float",
			"fieldname": "qty",
		},
		{
			"label": _("Rate"),
			"fieldtype": "Currency",
			"fieldname": "rate",
			"options": "currency",

		},
		{
			"label": _("Total Amount"),
			"fieldtype": "Currency",
			"fieldname": "amount",
			"options": "currency",

		},
		{
			"label": _("Grand Total"),
			"fieldname": "total",
			"fieldtype": "Currency",
			"options": "Currency",
			"width":100
		},
	]

	return columns

def get_data(filters):

	data = frappe.db.sql("""select A.customer,A.company,A.posting_date,
							B.item_code,B.item_name,B.qty,B.rate,B.amount,A.total 
							from `tabSales Invoice` AS A 
							INNER JOIN `tabSales Invoice Item` AS B 
							ON A.name=B.parent 
							where total>10000 
							and posting_date BETWEEN '{0}' and '{1}'
							""".format(filters.get("start_date"),filters.get("end_date")))
	
	return data
