from django.shortcuts import render
from rest_framework import generics as api_views

from web.core.models import Event, Product, ProductCategory
from web.core.serializers import EventSerializer, ProductSerializer, CategorySerializer


class EventListCreateView(api_views.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


event_list_and_create_view = EventListCreateView.as_view()


class SingleEventView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


single_event_view = SingleEventView.as_view()


class ProductListCreateView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_and_create_view = ProductListCreateView.as_view()


class SingleProductView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


single_product_view = SingleProductView.as_view()


class ProductCategoryListCreateView(api_views.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer


product_category_list_and_create_view = ProductCategoryListCreateView.as_view()


class SingleProductCategory(api_views.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer


single_product_category_view = SingleProductCategory.as_view()