from django.shortcuts import render
from .forms import SignupForm
from .models import Signup_Form


def home(request):
    context = {

        'name': 'Jeff Sevilla',
        'website': {
            'domain': 'test@gmail.com',
            'no_of_views': 0
         },
        'Address': 'San Diego'

    }
    return render(request, 'index.html', context)

def index(request):
    signup = SignupForm()
    return render(request, "form.html", {'form': signup})

def add(request):
    if request.method == 'POST':
        django_form = SignupForm(request.POST)
        if django_form.is_valid():
            new_member_firstname = django_form.data.get("firstname")
            new_member_lastname = django_form.data.get("lastname")
            new_member_age = django_form.data.get("age")

            #new_member_email = django_form.data.get("email")
            #new_member_username = django_form.data.get("username")
            #new_member_password = django_form.data.get("password")

            Signup_Form.objects.create(
                firstname = new_member_firstname,
                lastname = new_member_lastname,
                age=new_member_age

                #email = new_member_email,
                #username = new_member_username,
                #password = new_member_password
            )
    return render(request, 'add.html')

def show(request):
    users_list = Signup_Form.objects.all()
    return render(request, 'show.html', {'details': users_list})

def introduction(request):
    return render(request, 'introduction.html')

def about(request):
    return render(request, 'about.html')