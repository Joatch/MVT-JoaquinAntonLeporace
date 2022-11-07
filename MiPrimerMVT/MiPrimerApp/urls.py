from django.urls import path

from MiPrimerApp.views import mostrar_familia

urlpatterns = [
    path('', mostrar_familia)
]

#familia/

