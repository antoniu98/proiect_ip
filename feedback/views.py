from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.
def feedback_page(response):
    if response.method == 'POST':
        form = FeedbackForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(response, 'feedback.html', {
        'feedback_form': FeedbackForm(),
        'feedbacks' :  Feedback.objects.all(),
        'message' : 'Maybe bad rating :)'
        })
    return render(response, 'feedback.html', {
        'feedback_form': FeedbackForm(),
        'feedbacks' :  Feedback.objects.all(),
        'message' : 'Please : rate from 1-5 and specify your accomodation'
    })