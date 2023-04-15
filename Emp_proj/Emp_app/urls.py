from django.urls import path
from Emp_app.views import Employeelist, EmployeeDetail

app_name = 'Emp_app'

urlpatterns = [
     path('api/emp', Employeelist.as_view()),
     path('api/emp/<int:pk>', EmployeeDetail.as_view()),
]

