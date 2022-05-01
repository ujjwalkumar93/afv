import frappe
from askforvets.api.apis import Patient,Practitioner,Appointment

@frappe.whitelist()
def get_patient(patient=None):
	 return Patient().get_patient(patient)
	 


@frappe.whitelist()
def get_practitioner(practitioner=None):
	return Practitioner().get_practitioner(practitioner)
	

@frappe.whitelist()
def get_appointment(appointment=None):
	return Appointment().get_appointment(appointment)
	