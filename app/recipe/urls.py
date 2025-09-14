"""URL mapping for recipe app."""

from django.urls import (  # noqa
    path,
    include,
)

from rest_framework.routers import DefaultRouter  # noqa

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
