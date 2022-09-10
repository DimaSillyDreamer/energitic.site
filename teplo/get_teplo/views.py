import email
from django.shortcuts import redirect, render

from .models import Articles

from . forms import HeatCalculationForm, PumpForm, Registration, Login, FuelAmount, FuelTank
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator


def heat_calc(request):
    if request.method == 'POST':
        form = HeatCalculationForm(request.POST)
        t_outdoor = int(request.POST['t_outdoor'])
        t_indoor = int(request.POST['t_indoor'])
        volume = int(request.POST['volume'])
        house = request.POST['house']
        if form.is_valid():
            if house == 'жилое' and volume < 3000:
                q0 = 0.49
                qv = None
            elif house == 'жилое' and 5000 > volume >= 3000:
                q0 = 0.44
                qv = None
            elif house == 'жилое' and volume < 3000:
                q0 = 0.49
                qv = None
            elif house == 'жилое' and 5000 > volume >= 3000:
                q0 = 0.44
                qv = None
            elif house == 'жилое' and 10000 > volume >= 5000:
                q0 = 0.4
                qv = None
            elif house == 'жилое' and 15000 > volume >= 10000:
                q0 = 0.36
                qv = None
            elif house == 'жилое' and 20000 > volume >= 15000:
                q0 = 0.33
                qv = None
            elif house == 'жилое' and 25000 > volume >= 20000:
                q0 = 0.32
                qv = None
            elif house == 'жилое' and 30000 > volume >= 25000:
                q0 = 0.31
                qv = None
            elif house == 'жилое' and volume >= 30000:
                q0 = 0.3
                qv = None
            elif house == 'административное' and volume < 5000:
                q0 = 0.5
                qv = 1.02
            elif house == 'административное' and 10000 > volume >= 5000:
                q0 = 0.44
                qv = 0.09
            elif house == 'административное' and 15000 > volume >= 10000:
                q0 = 0.40
                qv = 0.08
            elif house == 'административное' and volume >= 15000:
                q0 = 0.37
                qv = None
            elif house == 'производственное' and 10000 > volume >= 5000:
                q0 = 0.6
                qv = 0.35
            elif house == 'производственное' and 15000 > volume >= 10000:
                q0 = 0.5
                qv = 0.25
            elif house == 'производственное' and 100000 > volume >= 15000:
                q0 = 0.47
                qv = 0.17
            elif house == 'производственное' and volume >= 100000:
                q0 = 0.43
                qv = 0.11
            elif house == 'ясли, сад' and volume < 5000:
                q0 = 0.44
                qv = 0.13
            elif house == 'ясли, сад' and volume > 5000:
                q0 = 0.40
                qv = 0.12
            elif house == 'больница' and volume < 5000:
                q0 = 0.47
                qv = 0.34
            elif house == 'больница' and 10000 > volume >= 5000:
                q0 = 0.42
                qv = 0.33
            elif house == 'больница' and 15000 > volume >= 10000:
                q0 = 0.37
                qv = 0.3
            elif house == 'больница' and volume >= 15000:
                q0 = 0.35
                qv = 0.29
            res1 = int(round((volume * q0 * 1.06 * (t_indoor - t_outdoor)) / 1000, 0))
                
            if qv is not None:
                res2 = int(round((volume * qv * (t_indoor - t_outdoor)) / 1000, 0))
                    
                total = res1 + res2
            else:
                res2 = 0
            total = int(round((res1 + res2), 0))
            data = {'form': form, 'total': total, 'res1': res1, 'res2': res2,
                    't_outdoor': t_outdoor, 't_indoor': t_indoor, 'volume': volume}
            return render(request, 'heat_calc.html', data)
    else:
        form = HeatCalculationForm()
    return render(request, 'heat_calc.html', {'form': form})


def home(request):
    articles_1 = Articles.objects.order_by('-id')[:2]
    return render(request, 'home.html', {'articles_1':articles_1})

def pump_calc(request):
    if request.method == 'POST':
        form = PumpForm(request.POST)
        n_boiler = request.POST['n_boiler']
        t_from_boiler = request.POST['t_from_boiler']
        t_into_boiler = request.POST['t_into_boiler']
        #email = request.POST['email']
        
        if form.is_valid():
            q_pump = round(int(n_boiler) * 0.86 / (int(t_from_boiler) - int(t_into_boiler)), 1)
            data = {
            'form': form,
            'n_boiler': n_boiler,
            't_from_boiler': t_from_boiler,
            't_into_boiler': t_into_boiler,
            #'email': email,
            'q_pump': q_pump
            }
            return render(request, 'pump_calc.html', data)
        else:
            return redirect('pump-calc')
    else:
        form = PumpForm()
    return render(request, 'pump_calc.html', {'form': form})  

def registration(request):
    if request.method == "POST":
        form = Registration(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Такой email уже используется.')
                return redirect('registration')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Такоe имя уже используется.')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'пароли не совпадают')
            return redirect('registration', {'form': form})
    else:
        form = Registration()
        return render(request, 'registration.html', {'form': form})
       

def login(request):
    form = Login()
    if request.method == "POST":
        form = Login(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')

def tools_page(request):
    return render(request, 'tools_page.html')


def instruments(request):

    return render(request, 'instruments.html')


def fuel_calc(request):
    if request.method == 'POST':
        form = FuelAmount(request.POST)
        efficiency = request.POST['efficiency']
        fuel = request.POST['fuel']
        boiler_power = request.POST['boiler_power']
        if form.is_valid():
            if fuel == 'природный газ':
                consumption = round((float(boiler_power)* 1000000 * 0.859845) / (((float(efficiency)) / 100) * 8000), 1)
                print(consumption)              
            elif fuel == 'дизельное топливо':
                consumption = round(((float(boiler_power) * 1000000 * 0.859845) / ((float(efficiency) / 100) * 10180)) / 835, 1)

            data = {
                'form': form,
                'efficiency': efficiency,
                'fuel': fuel,
                'boiler_power': boiler_power,
                'consumption': consumption
                }
            return render(request, 'fuel_calc.html', data)
        else:
            redirect('fuel-calc')
    else:
        form = FuelAmount()
        return render(request, 'fuel_calc.html', {'form': form})

def articles(request):
    articles = Articles.objects.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {'page_obj': page_obj}
    return render(request, 'articles.html', data)

def fuel_tank(request):
    if request.method == 'POST':
        form = FuelTank(request.POST)
        boiler_power = request.POST['boiler_power']
        number_of_days = request.POST['number_of_days']
        efficiency = request.POST['efficiency']
        if form.is_valid():
            tank_volume = round(((float(boiler_power) * 1000000 * 0.859845) / (((float(efficiency) / 100) * 10180)) / 835) * 24 * int(number_of_days), 2)
            data = {
                'form': form,
                'boiler_power': boiler_power,
                'number_of_days': number_of_days,
                'efficiency': efficiency,
                'tank_volume': tank_volume
                }
            return render(request, 'fuel_tank.html', data)
        else:
            redirect('fuel-tank')
    else:
        form = FuelTank()
        return render(request, 'fuel_tank.html', {'form': form})

def contacts(request):
    return render(request, 'contacts.html')

def questionnaires(request):
    return render(request, 'questionnaires.html')

def news(request):
    return render(request, 'news.html')