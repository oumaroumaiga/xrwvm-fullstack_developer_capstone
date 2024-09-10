from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from djangoapp import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),  # Include the app's URLs

    # Dynamic URLs
    path('login/', views.login_user, name='login'),
    path('register/', views.registration, name='register'),
    path('dealers/', views.get_dealerships, name='dealers'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('get_dealer/', views.get_dealerships, name='get_dealer'),

    # Static pages
    path('', TemplateView.as_view(template_name="Home.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
