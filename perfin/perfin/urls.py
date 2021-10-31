from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'perfin'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('budget/', views.BudgetView.as_view(), name='budget'),
    path('investments/', views.InvestmentsView.as_view(), name='investments'),
    path('networth/', views.NetWorthView.as_view(), name='networth'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
