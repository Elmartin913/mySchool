from django import forms
from .models import (SCHOOL_CLASS, Student, SchoolSubject, Message)
from django.core.validators import EmailValidator, URLValidator
from .validators import range_validator


class StudentSearchForm(forms.Form):

    name = forms.CharField(label='Nazwisko ucznia')


class AddStudentForm(forms.Form):

    first_name = forms.CharField(label='Imie', max_length=64)
    last_name = forms.CharField(label='Nazwisko', max_length=64)
    school_class = forms.ChoiceField(label='Klasa', choices=SCHOOL_CLASS)
    year_of_birth = forms.IntegerField(label="Data urodzenia", validators=[range_validator])


class PizzaConfigurator(forms.Form):

    TOPPINGS = (
        (1, 'oliwki'),
        (2, 'pomidory'),
        (3, 'dodatkowy ser'),
        (4, 'anchovies'),
        (5, 'cebula'),
    )

    toppins = forms.MultipleChoiceField(
        label='Dodatki',
        choices=TOPPINGS,
        widget=forms.CheckboxSelectMultiple,
    )


class PresenceListForm(forms.Form):

    student = forms.ModelChoiceField(label='Student', queryset=Student.objects.all())
    day = forms.DateField(label='Data', widget=forms.HiddenInput())
    present = forms.NullBooleanField(label='Obecnosc')


class UserData(forms.Form):

    name = forms.CharField(label='Imie')
    surname = forms.CharField(label='Nazwisko')
    email = forms.CharField(label='E-mail', validators=[EmailValidator()])
    favourite_www = forms.CharField(label='Ulubiona strona www', validators=[URLValidator()])


class SchoolSubjectForm(forms.ModelForm):
    class Meta:
        model = SchoolSubject
        # fields = '__all__'
        fields = ['name', 'teacher_name']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['date_sent']


class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Haslo', widget=forms.PasswordInput)


class ChangePassForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput())
    new_pass = forms.CharField(widget=forms.PasswordInput())
    old_pass_2 = forms.CharField(widget=forms.PasswordInput())





