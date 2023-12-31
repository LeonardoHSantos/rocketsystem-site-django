from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.home, name="login"),
    path("register/", views.home, name="register"),
    path("sobre/", views.about, name="about"),
    path("info-servicos/<str:service_name>", views.infoServices, name="info_services"),
    path("detalhes-servicos/", views.detailsServices, name="details_services"),
    path("pipedrive/v1/person/", views.PipedrivePerson, name="person"),
    path("pipedrive/v1/info/person/<str:id_person>", views.infoPerson, name="info_person"),
    path("pipedrive/v1/info/person/detele/<str:id_person>", views.deletePerson, name="detele_person"),

    path("pipedrive/v1/deals/", views.PipedriveDeals, name="deals"),
]
