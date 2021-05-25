// Copyright (c) 2021, Monika and contributors
// For license information, please see license.txt

frappe.ui.form.on('Registration', {
	validate(frm) {
		//to check the validation of telephone
		var phone_regex = /^[0]?[7-9][0-9]{9}$/;
		var emailregex= /^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\D{2,3}$/;
		if (phone_regex.test(frm.doc.telephone)==false){
			frappe.msgprint(__("Enter Valid telephone number"));
			frappe.validated=false;
		}
		else if (emailregex.test(frm.doc.email)==false){
			frappe.msgprint(__("Invalid Eamil"));
			frappe.validated=false;
		}
		
	}

	 				
})

