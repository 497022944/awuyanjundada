from django.urls import path
from . import views
urlpatterns =[
    path('',views.batch),
    path('batch/', views.batch),
    #path('index_id/<index_id>/<index_name>', views.index_id),
]