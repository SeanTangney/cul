from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact, QueryType


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view send a contact form to cul sports """

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_body = request.POST['message']

        Contact.objects.create(
            message_name=message_name,
            message_email=message_email,
            message_body=message_body
        )

        send_mail(
            message_name + message_email,  # Subject line
            ' Cul Contact Form' + message_body,  # Message
            None,  # From
            ['sean_tangney@hotmail.com'],  # To Email
        )

        messages.success(request, 'Thank you. '
                         ' Message Succesfully Sent!')
        return render(request, 'home/contact.html', {
                        'message_name': message_name
                        })
    else:
        query_types = QueryType.objects.all()
        return render(request, 'home/contact.html', {'types': query_types})
