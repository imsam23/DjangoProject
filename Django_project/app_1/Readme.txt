
Whatever the data submitted with a form, once it has been successfully validated by
calling is_valid() (and is_valid() has returned True),
the validated form data will be in the form.cleaned_data dictionary.
This data will have been nicely converted into Python types for you.

For example:

if form.is_valid():
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/thanks/')


Rendering fields manually:

