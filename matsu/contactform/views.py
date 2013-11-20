from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect
# Import contact form you created in forms.py
from forms import MatsuContactForm
from django.core.context_processors import csrf
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.forms.util import ErrorList
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
    msg_list.append('From:\n')
    msg_list.append(form.cleaned_data['name'])
    msg_list.append('\nOrganization/University\n')
    msg_list.append(form.cleaned_data['organization'])
    msg_list.append('\nEmail\n')
    msg_list.append(form.cleaned_data['sender'])
    msg_list.append('\nMessage:\n')
    msg_list.append(form.cleaned_data['message'])
    return ''.join(msg_list)

# Show form or submit it
def contact(request):
	
	# If form has been submitted...
    if request.method == 'POST':
    	
    	# Use form bound to the POST data
        form = OSDCSupportForm(request.POST)
        
        # If all validation rules pass...
        if form.is_valid():
            subject = "New feedback from Matsu user"
            message = build_message(form)
            sender = form.cleaned_data['sender']
            recipients = [settings.CONTACT_EMAIL]

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect("thankyou.html") # Redirect after POST
	
	# Otherwise, if no form submitted
    else:
        form = MatsuContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })

# Show demos page
def matsu_demos(request):
	return render_to_response("matsu-demonstrations.html")

# Necessary to specify view to redirect after thank you? That may be specified above.
# def matsu_contact_thanks(request):
# 	return render_to_response(request, "thankyou.html")