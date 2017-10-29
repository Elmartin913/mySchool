"""mySch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app.views import (
    SchoolView,
    SchoolClassView,
    StudentView,
    Grades,
    StudentSearchView,
    AddStudentView,
    PizzaToppings,
    PresenceListView,
    UserDataView,
    SchoolSubjectCreateView,
    MessageFormView,
    UserListView,
    LoginView,
    LogoutView,
    ChangePassView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SchoolView.as_view(),
        name="index"),
    url(r'^class/(?P<school_class>(\d)+)', SchoolClassView.as_view(),
        name="school-class"),
    url(r'^student/(?P<student_id>(\d)+)', StudentView.as_view(),
        name="student_details"),
    url(r'^grades/(?P<student_id>(\d)+)/(?P<subject_id>(\d)+)', Grades.as_view(),
        name="student_grades"),
    url(r'^student_search', StudentSearchView.as_view(),
        name="student_search"),
    url(r'^add_student', AddStudentView.as_view(),
        name="add_student"),
    url(r'^pizza_toppings', PizzaToppings.as_view()),
    url(r'^class_presence/(?P<student_id>(\d)+)/(?P<date>\d{4}-\d{2}-\d{2})$', PresenceListView.as_view(),
        name="class_presence"),
    url(r'd2_p3_e1', UserDataView.as_view(),
        name="class_presence"),
    url(r'create_school_subject', SchoolSubjectCreateView.as_view(),
        name="create_school_subject"),
    url(r'compose_message', MessageFormView.as_view(),
        name="compose_message"),
    url(r'list_users', UserListView.as_view(),
        name="list_users"),
    url(r'login', LoginView.as_view(),
        name="login"),
    url(r'logout', LogoutView.as_view(),
        name="logout"),
    url(r'reset_password/(?P<user_id>(\d)+)$', ChangePassView.as_view(),
        name="reset_password"),

]
