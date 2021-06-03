// Copyright (c) 2016, Monika and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["QR-assign2"] = {
	"filters": [
		{
            "fieldname":"from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "reqd":1
        },
        {
            "fieldname":"to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
        },
        {
            "fieldname":"qty",
            "label": __("Quantity"),
            "fieldtype": "Float",
        },           

	]
};
