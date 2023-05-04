from django.shortcuts import render
from .models import *

## RENDERING HOME PAGE ##
def index(request):
	Banner   = Slider_banner.objects.all()        # Fetching banner image from database
	services = Services.objects.all()			  # Fetching banner image from database
	service  = Service.objects.all()              # Fetching banner image from database
	session  = Session_types.objects.all()        # Fetching session types  image and name from database
	
	mission_vision_whychooseus = mission_vision.objects.all()  # Fetching mission & vision image and content from database


	context = {

	'Banner'  :Banner,
	'service' :service,
	'services':services,
	'mvw'     : mission_vision_whychooseus,
	'session' : session,
	}

	return render(request,"index.html",context)

## RENDERING ABOUT US PAGE ##
def about_us(request):

	about = About_us.objects.all()
	print(about)
	mission_vision_whychooseus = mission_vision.objects.all()

	context = {
	'About' : about,
	'mvw'   : mission_vision_whychooseus,
	}

	return render(request,"about_us.html",context)


## RENDERING CONTACT US PAGE ##
def contact_us(request):
	if request.method=='POST':
		name=request.POST["name"]
		email = request.POST["email"]
		mobile_no = request.POST['mobile']
		message = request.POST['message']
		p = ContactForm.objects.create(name=name,address=email,mobile_number=mobile_no,Message=message)
		p.save()
		context = {
		'name':name,
		}
		return render(request,"contact_us.html",context)
	else:
		return render(request,"contact_us.html")


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
	# if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']

    #     if password == password2:
    #         if User.objects.filter(email=email).exists():
    #             messages.info(request, 'Email Taken')
    #             return redirect('registration')
    #         elif User.objects.filter(username=username).exists():
    #             messages.info(request, 'Username Taken')
    #             return redirect('registration')
    #         else:
    #             user = User.objects.create_user(username=username, email=email, password=password)
    #             user.save()

    #             # log user in and redirect to settings page
    #             user_login = auth.authenticate(username=username, password=password)
    #             auth.login(request, user_login)

    #             # create a Profile object for the new user
    #             user_model = User.objects.get(username=username)
    #             new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
    #             new_profile.save()
    #             return redirect('login')
    #     else:
    #         messages.info(request, 'Password Not Matching')
    #         return redirect('registration')

    # else:return render(request, 'registration.html')
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