import frappe
from askforvets.api.apis import Patient, Practitioner, Appointment ,User

@frappe.whitelist()
def get_patient(patient=None):
	 return Patient().get_patient(patient)
	 


@frappe.whitelist()
def get_practitioner(practitioner=None):
	return Practitioner().get_practitioner(practitioner)
	

@frappe.whitelist()
def get_appointment(appointment=None):
	return Appointment().get_appointment(appointment)



@frappe.whitelist()
def get_appointment(appointment=None):
	return Appointment().get_appointment(appointment)



@frappe.whitelist()
def get_user_detail(user=None):
	return User().get_user_detail(user)

