import email
from tkinter import Widget
from django import forms

purpose_of_premises = [
    'жилое',
    'административное',
    'производственное',
    'ясли, сад',
    'больница']

fuel_type = [
    'природный газ',
    'дизельное топливо'
]

class HeatCalculationForm(forms.Form):

    t_outdoor = forms.DecimalField(
        label="Температура наружного воздуха, гр.С",
        max_digits=3,

    )
    t_indoor = forms.DecimalField(
        label='Температура внутреннего воздуха, гр.С',
        max_digits=3
    )
    volume = forms.DecimalField(
        label='Отапливаемый объем здания, куб.м.',
        max_digits=15
    )
    house = forms.ChoiceField(
        label="Назначние помещения:",
        choices=[
            (x, x) for x in purpose_of_premises
        ])
    #email = forms.EmailField(
        #label="Введите ваш email:"
    #)

class PumpForm(forms.Form):
    n_boiler = forms.DecimalField(
        label="Введите мощность котла, кВт:",
        max_digits=15
    )
    t_from_boiler = forms.DecimalField(
        label='Введите температуру подачи, гр. С:',
        max_digits=3
    )
    t_into_boiler = forms.DecimalField(
        label='Введите температуру обратного потока, гр. С:',
        max_digits=3
    )
    #email = forms.EmailField(
        #label="Введите ваш email:"
    #)

class Registration(forms.Form):
    username = forms.CharField(
        label='Введите имя пользователя:',
        max_length=30
    )
    email = forms.EmailField(
        label='Введите ваш email:'
    )
    password = forms.CharField(
        label='Введите пароль:',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Введите пароль:',
        widget=forms.PasswordInput()
    )

class Login(forms.Form):
    username = forms.CharField(
        label='Введите имя пользователя:',
        max_length=30
    )
    password = forms.CharField(
        label='Введите пароль:',
        widget=forms.PasswordInput()
    )
    

class FuelAmount(forms.Form):
    efficiency = forms.DecimalField(
        label='Введите КПД котла, %:',
        max_digits=4
    )
    boiler_power = forms.DecimalField(
        label='Введите мощность котла, МВт:'
    )
    fuel = forms.ChoiceField(
        label="Выберите вид топлива:",
        choices=[
            (x, x) for x in fuel_type
        ])

class FuelTank(forms.Form):
    boiler_power = forms.DecimalField(
        label = 'Введите расчетную тепловую мощность котельной, МВт:',
        max_digits=6        
    )

    number_of_days = forms.DecimalField(
        label='Введите количество суток работы котельной от склада дизельного топлива:',    
        max_digits=4
    )

    efficiency = forms.DecimalField(
        label='Введите КПД котла, %:',
        max_digits=4       
    )