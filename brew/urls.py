from django.urls import path
from .views import get_or_create_coffee
from .views import get_or_create_snack
from .views import get_coffee_by_id
from .views import get_snack_by_id

urlpatterns = [
    path('api/coffees/', get_or_create_coffee, name='create_coffee'),
    path('api/snacks/', get_or_create_snack, name='get_post_snack'),
    path('api/coffees/<int:pk>/', get_coffee_by_id, name='get_coffee_by_id'),
    path('api/snacks/<int:pk>/', get_snack_by_id, name='get_snack_by_id')
]