from django.shortcuts import render


## RENDERING HOME PAGE ##
def index(request):
	return render(request,"index.html")

## RENDERING ABOUT US PAGE ##
def about_us(request):
	return render(request,"about_us.html")


## RENDERING CONTACT US PAGE ##
def contact_us(request):
	return render(request,"contact_us.html")

## RENDERING GALLERY PAGE ##
def gallery(request):
	return render(request,"gallery.html")

## RENDERING SERVICE PAGE ##
def service(request):
	return render(request,"services.html")

## RENDERING BLOG PAGE ##
def blog(request):
	return render(request,"blog.html")

## RENDERING BOOKING APPOINTMENT/SESSION PAGE ##
def appointment(request):
	return render(request,"appointment.html")

## RENDERING LOGIN PAGE FOR USER LOGIN ##
def login(request):
	return render(request,"login.html")

## RENDERING PAYMENT PLANS PAGE  ##
def plans(request):
	return render(request,"plans.html")

## RENDERING PAYMENT FROM USER PAGE  ##
def payment(request):
	return render(request,"payment.html")	

## RENDERING PAYMENT DONE AND ZOOM LINK SENT PAGE  ##
def zoom(request):
	return render(request,"zoom.html")

## RENDERING REGISTRATION PAGE ##
def registration(request):
	return render(request,"registration.html")

## RENDERING REGISTRATION PAGE ##
def login1(request):
	return render(request,"login1.html")		

## RENDERING REGISTRATION PAGE ##
def gender(request):
	return render(request,"male_female.html")	

## RENDERING DOCTOR HOME PAGE ##
def doc_index(request):
	return render(request,"doctor/doc-index.html")	

## RENDERING DOCTOR APPOINTMENT PAGE FOR CHECKING UPCOMING APPOINTMENTS FROM PATIENTS ##
def doc_appointment(request):
	return render(request,"doctor/doc-appointments.html")	

def doc_edit_appointment(request):
	return render(request,"doctor/doc-edit-appointment.html")	

## RENDERING DOCTOR PATIENTS ##
def doc_patients(request):
	return render(request,"doctor/patients.html")	

def doctor_payment(request):
	return render(request,"doctor/invoices.html")	

def doctor_login(request):
	return render(request,"doctor/login.html")