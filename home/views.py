from django.shortcuts import render
from django.contrib import messages


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view send a contact form to cul sports """
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        messages.success(request, 'Thank you. '
                                  ' Message Succesfully Sent!')
        return render(request, 'home/contact.html')

    else:
        messages.error(request, 'Failed To Send Message. '
                                ' Please Ensure The Form Is Valid.')
        return render(request, 'home/contact.html')
