from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic.list import ListView
from .models import Testimonial, Booking, Subscription
from django.views.generic.edit import FormView
from .forms import BookingForm, SubscriptionForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# class Testimonials(ListView):
#     model = Testimonial
#     queryset = Testimonial.objects.filter(status=1)
#     template_name = 'index.html'
#     context_object_name = 'testimonials'

def testimonial_and_subscription(request):
    testimonials = Testimonial.objects.filter(status=1)
    subscription_form = SubscriptionForm()
    context = {
        'testimonials': testimonials,
        'form': subscription_form
    }
    if request.method == "POST":
        subscription_form = SubscriptionForm(request.POST)
        if subscription_form.is_valid():
            subscription_form.save()
            return redirect('homePage')
        else:
            return subscription_form.form_invalid()
    return render(request, 'index.html', context)


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
            if self.request.user.is_authenticated:
                form.instance.client = request.user
                form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Your Booking has been successfully created.')
                return HttpResponseRedirect(reverse('homePage'))
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    'Sorry!, but you need to Sign in first.')
                return HttpResponseRedirect(reverse('account_login'))
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
            messages.add_message(
                request,
                messages.SUCCESS,
                'Booking has been successfully updated.')
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
    messages.add_message(
        request,
        messages.SUCCESS,
        'Booking has been successfully deleted.')
    return redirect('bookingRecord')
