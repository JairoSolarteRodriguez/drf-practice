from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views
from ingredients import views as ingredientsView


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('ingredients', ingredientsView.IngredientsViewSet)

urlpatterns = [
    path('hello-view', view=views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
