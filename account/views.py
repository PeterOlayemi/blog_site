from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, FormView
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetConfirmView, LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from .token import account_activation_token

from .forms import RegisterForm
from .models import User

# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        if not 'agree' in self.request.POST:
            messages.error(self.request, 'You Must Agree To Our Terms And Conditions Before You Register')
            return redirect('register')
        user.is_active = False
        user.profile_picture = self.request.FILES.get('profile_picture')
        user.save()
        self.send_verification_email(user)
        messages.success(self.request, 'Registration Successful! Please Check Your Email To Verify Your Account.')
        return super().form_valid(form)

    def send_verification_email(self, user):
        current_site = get_current_site(self.request)
        subject = "Affyn's Blog: Verify Your Account"
        message = render_to_string('account/mail/account_verify_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(get_user_model(), pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None 
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your Account Has Been Verified. You Can Log In Now.')
            return redirect('login')
        else:
            messages.error(request, 'Activation Link Is Invalid!.')
            return redirect('login')

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        if not self.request.POST.get('remember'):
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(1209600)
        return response
    
def LogOutView(request):
    logout(request)
    return redirect('home')

class TermView(TemplateView):
    template_name = 'account/term.html'
    
class PrivacyView(TemplateView):
    template_name = 'account/privacy.html'
    
class ForgotPasswordView(FormView):
    form_class = PasswordResetForm
    template_name = 'account/forgot_password.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = self.request.POST.get('email')
        try:
            user = get_object_or_404(User, email=email)
            self.send_verification_email(user)
            messages.success(self.request, 'Check Your Email Inbox Or Spam For Instructions On How To Reset Your Password')
            return super().form_valid(form)
        except:
            messages.error(self.request, 'Email Not Found')
            return redirect('forgot_password')
    
    def send_verification_email(self, user):
        current_site = get_current_site(self.request)
        subject = "Affyn's Blog: Forgot Password Request"
        message = render_to_string('account/mail/forgot_password_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
            'date': timezone.now().date(),
        })
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

class ForgotPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'account/forgot_password_confirm.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your Password Has Been Reset Successfully. You Can Log In Now.')
        return redirect(reverse_lazy('login'))
