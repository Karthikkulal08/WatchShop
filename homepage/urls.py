from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.Home,name='home'),
    path('About',views.About),
    path('upload', views.upload,name="upload_images"),
    path('login', views.login_page,name="login"),
    path('signup', views.signup_user,name="signup"),
    path('logout', views.logout_user,name="logout"),
    path('product/<int:id>/', views.show_product, name='product'),
    path('addtowish/<int:id>', views.show_product, name='addtowish'),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
