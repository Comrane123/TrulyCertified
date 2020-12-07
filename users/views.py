from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import SignUpForm


# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    # success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
