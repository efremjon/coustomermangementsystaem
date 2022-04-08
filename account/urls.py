from django.urls import path,include
from .import views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views

urlpatterns = [

# this is authentication apart.
    path('a/',include('django.contrib.auth.urls')),
    path('register/', views.registerPage, name="re"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

# this part is

    path('',views.home,name='home'),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),
    path('product/',views.product,name='product'),
    path('customer/<str:pk_cust>/',views.customer,name='customer'),
    
    path('create_order/<int:pk>',views.Customer_Order,name='cust_order'),
    path('Update_order/<int:pk>/',views.Update_Order,name='update_order'),
    path('delete_order/<int:pk>/',views.Delete_Order,name='delete_order'),


    #################################################

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"), 
        name="password_reset_complete"),

 #################################################

]
