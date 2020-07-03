from django.urls import path
from bank.api.views import BankListView

app_name = 'bank'

urlpatterns = [
    path('list',BankListView.as_view(),name='list')
]