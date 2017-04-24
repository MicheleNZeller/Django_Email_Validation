from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email, EmailManager

# Create your views here.
def index(request):
	return render(request, "first_app/index.html")

def process(request):
	if request.method == "POST":
		response = Email.emailmanager.validate(request.POST)
		if response[0] == True:
			Email.emailmanager.create(emails=request.POST['email_post'])
			return redirect("/success")
		else:
			messages.error(request, response[1])
			return redirect("/")

	else:
		return redirect("/")


def success(request):
	emails = Email.emailmanager.all()
	context = {
		"all_emails": emails
	}
	return render(request, "first_app/success.html", context)
