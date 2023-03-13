from django.conf.urls import url
from django.urls import path

from . import views
app_name='todoapp'

urlpatterns=[

    path('',views.homepage,name='homepage'),
    path('homelistview/', views.TodoListView.as_view(), name='homelistview'),
    path('homedetailview/<int:pk>/', views.TodoDetailView.as_view(), name='homedetailview'),
    path('homeupdateview/<int:pk>/', views.TodoUpdateView.as_view(),name='homeupdateview'),
    path('homedeleteview/<int:pk>/', views.TodoDeleteView.as_view(),name='homedeleteview'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),


    # path('detail/',views.detail,name='detail'),

]