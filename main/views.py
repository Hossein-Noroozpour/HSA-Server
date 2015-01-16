from django.shortcuts import render
from main.models import Agent
from django.core.handlers.wsgi import WSGIRequest
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    pass


def register(request):
    """
    :type request: WSGIRequest
    """
    try:
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email_address = request.POST['email-address']
        birth_date = request.POST['birth-date']
        phone_number = request.POST['phone-number']
        home_address = request.POST['home-address']
        work_address = request.POST['work-address']
    except KeyError:
        return render(request, 'main/register.html')
    else:
        try:
            validate_email(email_address)
        except ValidationError:
            return render(request, 'main/register.html', {'error_message': "Please enter a valid email address."})
        try:
            birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        except ValueError:
            return render(request, 'main/register.html', {'error_message': "Please enter a valid birth date, "
                                                                           + "its format must be: YYYY-MM-DD"})
        try:
            Agent.objects.get(email_address=email_address)
        except ObjectDoesNotExist:
            agent = Agent(first_name=first_name,
                          last_name=last_name,
                          email_address=email_address,
                          birth_date=birth_date,
                          phone_number=phone_number,
                          home_address=home_address,
                          work_address=work_address,
                          key_iv_aes=get_random_string(length=128),
                          session_key_iv_aes=get_random_string(length=128),
                          logged_in=False,
                          login_tries=0,
                          last_login_try=timezone.now(),
                          confirmed=False,
                          registration_date=timezone.now())
            agent.save()
        else:
            return render(request, 'main/register.html', {'error_message': "Your email is registered before."})


def show(request):
    return render(request, 'main/show.html', {'agents_list': Agent.objects.order_by('last_name')})


def detail(request, agent_id):
    pass