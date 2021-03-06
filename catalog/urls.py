from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from catalog import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('hola/hola', views.homePageView, name='home'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
