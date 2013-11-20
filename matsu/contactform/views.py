from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect
# from forms import MatsuContactForm
from django.core.context_processors import csrf
# from django.core.mail import sendmail

def home(request):
	return render_to_response("index.html")
	
# Show web applications page
def webapps(request):
	return render_to_response("webapplications.html")

# Show contact form
def contact(request, user=None):
	return render_to_response("contact.html")
	
def matsu_demos(request):
	return render_to_response("matsu-demonstrations.html")
