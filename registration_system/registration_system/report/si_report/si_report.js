// Copyright (c) 2016, Monika and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["SI report"] = {
	"filters": [
		{
            "fieldname":"start_date",
            "label": __("Start Date"),
            "fieldtype": "Date",
            "reqd":1
        },
        {
            "fieldname":"end_date",
            "label": __("End Date"),
            "fieldtype": "Date",
        },
        {
            "fieldname":"total",
            "label": __("Total"),
            "fieldtype": "Currency",
        },


	]
};
