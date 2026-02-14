from django.views.generic import CreateView
from .models import Interview
from .forms import InterviewCreateForm

class InterviewCreateView(CreateView):
    model = Interview
    template_name = 'booking/create_booking.html'
    form = InterviewCreateForm
    fields = '__all__'