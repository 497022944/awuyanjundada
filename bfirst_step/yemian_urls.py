from django.urls import path
from . import views
urlpatterns =[
    path('',views.batch),
    path('batch/', views.batch),
    path('batchmanyan/', views.batchmanyan),
    #path('index_id/<index_id>/<index_name>', views.index_id),
]