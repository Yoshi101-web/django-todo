from django.urls import path, include
from .views import TodoList

urlpatterns = [
    #TodoListは、クラス名にas_view()
    path('list/', TodoList.as_view()),
]
