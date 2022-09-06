from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view send a contact form to cul sports """
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send Email
        send_mail(
            'Cúl Contact Form - ' + message_name,  # Subject line
            message,  # Message
            None,  # From
            ['sean_tangney@hotmail.com'],  # To Email
        )

        messages.success(request, 'Thank you. '
                                  ' Message Succesfully Sent!')
        return render(request, 'home/contact.html', {
                        'message_name': message_name
                        })
    else:
        return render(request, 'home/contact.html', {})
