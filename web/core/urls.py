from django.urls import path

from web.core.views import product_list_and_create_view, product_category_list_and_create_view, single_product_view, \
    event_list_and_create_view, single_event_view, single_product_category_view

urlpatterns = (
    path('product-create/', product_list_and_create_view, name='product list and create'),
    path('single-product/<int:pk>/', single_product_view, name='single product'),
    path('category-create/', product_category_list_and_create_view, name='category list and create'),
    path('single-category/<int:pk>/', single_product_category_view, name='single category'),
    path('event-create/', event_list_and_create_view, name='event list and create'),
    path('single-event/<int:pk>/', single_event_view, name='single event'),

)
