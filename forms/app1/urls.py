from django.urls import path

from .import views
urlpatterns=[path('insert/',views.insert_view),
             path('display/',views.display),
             path('update/<int:id>',views.update_view),
             path('delete/<int:id>',views.delete_view),
             ]
