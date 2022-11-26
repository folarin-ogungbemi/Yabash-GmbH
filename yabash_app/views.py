from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic.list import ListView
from .models import Testimonial, Booking
from django.views.generic.edit import FormView
from .forms import BookingForm
from django.http import HttpResponseRedirect


class Testimonials(ListView):
    model = Testimonial
    queryset = Testimonial.objects.filter(status=1)
    template_name = 'index.html'
    context_object_name = 'testimonials'


class BookingRecords(ListView):
    model = Booking
    form_class = BookingForm
    template_name = 'records.html'
    context_object_name = 'records'
    paginate_by = 3

    def get_queryset(self):
        return Booking.objects.filter(client=self.request.user.id)


class BookingCreateView(FormView):
    template_name = 'booking.html'
    form_class = BookingForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.instance.client = request.user
            form.save()
            return HttpResponseRedirect(reverse('homePage'))
        else:
            return self.form_invalid(form)


# Function creates user ability to edit
# and update form and redirects to records
def BookingUpdateView(request, record_id):
    record = get_object_or_404(Booking, id=record_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('bookingRecord')
    form = BookingForm(instance=record)
    context = {
        'form': form
    }
    return render(request, 'update.html', context)


# Function creates user ability to delete form and redirects to records
def BookingDeleteView(request, record_id):
    record = get_object_or_404(Booking, id=record_id)
    record.delete()
    return redirect('bookingRecord')
