from.import views
from django.urls import path
urlpatterns = [
    path('',views.demo,name='demo'),


    path('operation/',views.Arithmetic_operation,name='Arithmetic_operation')


    # path('',views.home,name='home'),
    #
    # path('about/',views.about,name='about'),
    #
    # path('contact/',views.contact,name='contact'),
    #
    # path('detail/',views.detail,name='detail'),
    #
    # path('thank/',views.thank,name='thank')
]