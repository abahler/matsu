from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect
from forms import MatsuContactForm
# Importing get_connection necessary if you have send_mail or EmailMessage?
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.forms.util import ErrorList
from django.conf import settings
import smtplib

def home(request):
	return render_to_response("index.html")
	
# Show web applications page
def webapps(request):
	return render_to_response("webapplications.html")

# Build message that goes to the Matsu admin
def build_message(form):
    msg_list = []
    msg_list.append('Summary of submitted information:\n\n')
    msg_list.append('From: ')
    msg_list.append(form.cleaned_data['name'])
    msg_list.append('\nOrganization/University: ')
    msg_list.append(form.cleaned_data['organization'])
    msg_list.append('\nEmail: ')
    msg_list.append(form.cleaned_data['sender'])
    msg_list.append('\nMessage: ')
    msg_list.append(form.cleaned_data['message'])
    msg_list.append('\n')
    return ''.join(msg_list)

# Show form or submit it
def contact(request):
	# If form has been submitted...
	if request.method == "POST":
		# Use form bound to the POST data
		form = MatsuContactForm(request.POST)
		
		# If all validation rules pass...
		if form.is_valid():
			subject = "New feedback from Matsu user"
			sender = form.cleaned_data['sender']
			message = build_message(form)
			recipients = [settings.CONTACT_EMAIL]
			
			# Trying below instead of "send_mail(subject, message, sender, recipients)"
			emailMatsu = EmailMessage(subject, message, sender, recipients)
		
			try:
				emailMatsu.send()
				return HttpResponseRedirect("/contact/thankyou/")
			except smtplib.SMTPRecipientsRefused as e:
				form._errors["sender"] = ErrorList(["Domain of address %s does not exist" % sender])
				
	# Otherwise, if no form submitted
	else:
		form = MatsuContactForm()
		
	# Including third argument for csrf verification, Without it, you get "CSRF aborted" 403 error.
	return render_to_response("contact.html", {'form' : form}, context_instance=RequestContext(request))

# Show demos page
def matsu_demos(request):
	return render_to_response("matsu-demonstrations.html")

def thankyou(request):
	return render_to_response("thankyou.html")

def file_not_found(request):
        return render_to_response("404.html")

def server_error(request):
        return render_to_response("500.html")
