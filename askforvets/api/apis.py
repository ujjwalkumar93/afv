import frappe


class Patient():
	def get_patient(self,patient=None):
		
		query = "select * from `tabPatient` "

		if patient:
			conditions  = f' where name = "{patient}" '

			query = query + conditions

		
		patients = frappe.db.sql(query,as_dict=True)
		return patients


class Practitioner():
	def get_practitioner(self,practitioner=None):

		query = "select * from `tabPractitioner`"

		if practitioner:
			conditions = f" where name = '{practitioner}' "

			query = query + conditions


		practitioners = frappe.db.sql(query,as_dict=True)
		return practitioners


class Appointment():
	def get_appointment(self,appointment=None):
		
		query = "select * from `tabAppointment`"

		if appointment:
			
			conditions = f" where name = '{appointment}' "
			
			query = query + conditions

		appointments = frappe.db.sql(query,as_dict=True)
		return appointments


class User():
	def get_user_detail(self,user=None):
		
		query = "select * from `tabUser`"

		if user:
			
			conditions = f" where name = '{user}' "
			
			query = query + conditions

		user = frappe.db.sql(query,as_dict=True)
		return user
