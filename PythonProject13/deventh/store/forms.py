from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        field = ['first_name','last_name','username','email','password1','password2']
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        field = ['username' , 'password']
