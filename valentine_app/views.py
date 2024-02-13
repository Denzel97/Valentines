from django.shortcuts import render, redirect
from .forms import SenderForm, ReceiverForm
from .models import Sender
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def thank_you(request):
    # Get the response from the request's GET parameters
    response = request.GET.get('response')

    # Ensure the response is set and convert it to lowercase
    response_lower = response.lower() if response else None

    # Debug print statement
    print(f"Debug: {response_lower}")

    # Pass the response to the template
    return render(request, 'valentine_app/thank_you.html', {'response': response_lower})




def sender(request):
    if request.method == 'POST':
        sender_form = SenderForm(request.POST)
        if sender_form.is_valid():
            sender = sender_form.save()
            sender_link = sender.generate_unique_link()
            return render(request, 'valentine_app/sender_confirmation.html', {'sender_link': sender_link})
    else:
        sender_form = SenderForm()

    return render(request, 'valentine_app/sender.html', {'sender_form': sender_form})



from django.urls import reverse

# ...

def receiver(request, sender_id):
    sender = Sender.objects.get(pk=sender_id)

    if request.method == 'POST':
        receiver_form = ReceiverForm(request.POST)
        if receiver_form.is_valid():
            receiver = receiver_form.save(commit=False)
            receiver.sender = sender
            receiver.save()

            # Send email to the sender
            subject = "Thank You for Your Valentine's Response"
            sender_email = sender.sender_email
            receiver_name = receiver.receiver_name
            response = receiver.response

            # Render email content using a template
            email_html = render_to_string('valentine_app/email_template.html', {'receiver_name': receiver_name, 'response': response})
            email_plain = strip_tags(email_html)  # Strip HTML tags for the plain text version

            # Send the email
            send_mail(
                subject,
                email_plain,
                'denzelwassh97@gmail.com',  # Replace with your sender email
                [sender_email],
                html_message=email_html,
            )

            # Redirect to the thank_you view without any parameters
            return redirect(reverse('thank_you') + f'?response={receiver_form.cleaned_data["response"]}')

    else:
        receiver_form = ReceiverForm()

    return render(request, 'valentine_app/receiver.html', {'receiver_form': receiver_form})