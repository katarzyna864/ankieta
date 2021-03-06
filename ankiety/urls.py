from django.urls import path

from . import views

app_name = 'ankiety'
urlpatterns = [
    path('', views.index, name='index'),
    path('useranswers/', views.useranswers, name='useranswers'),
    path('whetheranswered/', views.whetheranswered, name='whetheranswered'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
]