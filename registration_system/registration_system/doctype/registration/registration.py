# Copyright (c) 2021, Monika and contributors
# For license information, please see license.txt
import re
import frappe
from frappe.model.document import Document
from frappe import _


class Registration(Document):

	def before_save(self):

		#to check the validation of first name
		if not (self.first_name).isalpha():
			frappe.throw("Enter Alphabets only without any space")

		#to check the validation of password
		if len(self.password)<8:
			frappe.throw("Length of password should be greater than 8")

		elif not re.search("[a-z]",self.password):
			frappe.throw("In password Alphabets must be between [a-z]")

		elif not re.search("[A-Z]",self.password):
			frappe.throw("In password Atleast one alphabet should be uppercase")

		elif not re.search("[0-9]",self.password):
			frappe.throw("In password Atleast 1 number is between[0-9]")

		elif not re.search("[_@$]",self.password):
			frappe.throw("In password Alleast one character from [_ @ $]")

		elif re.search("[\s]",self.password):
			frappe.throw("In password no whitespace allowed")
		

	def on_submit(self):
		user = frappe.get_doc(doctype='User', first_name=self.first_name,email=self.email,new_password=self.password)
		user.send_welcome_email=0
		user.insert()

		context={"email":self.email,"password":self.password} 
		msg=frappe.render_template("registration_system/public/email_template/welcome.html",context)

		
		frappe.sendmail(
			recipients=self.email,
			sender="patilmoni2012@gmail.com",
			subject="Successfully Register",
			message=msg,
			reference_doctype=self.doctype,
			reference_name=self.name,

			)
		frappe.msgprint(_("Email Sent Successfully"))

		




