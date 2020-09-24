from django.urls import path, include
from .views import TodoList, TodoDetail

urlpatterns = [
    #TodoListは、クラス名にas_view()
    path('list/', TodoList.as_view()),
    path('detail/<int:pk>', TodoDetail.as_view()),
]
