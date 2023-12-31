from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import PictureForm, LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BookingImageModel


class AddBookingView(LoginRequiredMixin, views.View):
    login_url = 'Login'
    redirect_field_name = 'AddBooking'

    def get(self, request):
        form = PictureForm()
        images = BookingImageModel.objects.all()
        return render(request, 'AddBooking.html', {'form': form})

    def post(self, request):
        form = PictureForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')

        for image in images:
            BookingImageModel.objects.create(booking = BookingImageModel, images=image)

        if form.is_valid():
            picture_form = form.save(commit=False)
            picture_form.user = request.user
            picture_form.save()
            return redirect('profile_details', pk=request.user.pk)
        return render(request, 'AddBooking.html', {'form': form, 'images': images})

class LoginView(views.View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'registratiton/Login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
                return render(request, 'registratiton/Login.html', {'form': form})

        return render(request, 'registratiton/Login.html', {'form': form})


class RegistrationView(views.CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('Login')

class MyLogoutoView(views.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        redirect_url = reverse_lazy('home')
        return redirect(redirect_url)


class AboutUsView(views.View):
    def get(self, request):
        return render(request, 'AboutUs.html')