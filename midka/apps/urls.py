from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps import views

router = DefaultRouter()
router.register(r'books', viewset=views.BookViewSet)
router.register(r'journals', viewset=views.JournalViewSet)
router.register(r'bookandjuornals', views=views.)

urlpatterns = [
    path('', include(router.urls))
]