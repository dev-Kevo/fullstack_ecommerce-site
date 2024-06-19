from django.urls import path, include
from  .views import ProductList, OrderList, CustomerList, UserList
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()

router.register(r'products', ProductList, basename='product')
router.register(r'orders', OrderList, basename='order')
router.register(r'customers', CustomerList, basename='customer')
router.register(r'users', UserList, basename='user')



urlpatterns = [
    path('', include(router.urls)),
]
