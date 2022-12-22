
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('category/<slug:val>', views.CategoryView.as_view(),name="category"),
    path('categor-title/val>', views.CategoryTitle.as_view(),name="category-title"),
    path('product_detail/<int:pk>', views.ProductDetail.as_view(),name="product_detail"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
