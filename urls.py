from django.urls import path
from . import views

app_name ='imsakapp'

urlpatterns = [
#fbvl
path('',views.readjadwalimsak),
path('alamat/<int:id>', views.detailjadwalimsak),
path('buat/', views.createjadwalimsak),
path('edit/<int:id>', views.updatejadwalimsak),
path('hapus/<int:id>', views.deletejadwalimsak),
]