from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('product/',views.product,name='product'),
    path('customer/<str:pk_cust>/',views.customer,name='customer'),
    path('create_order/',views.Customer_Order,name='cust_order'),
    path('Update_order/<int:pk>/',views.Update_Order,name='update_order'),
    path('delete_order/<int:pk>/',views.Delete_Order,name='delete_order'),

]
