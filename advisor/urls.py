from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('', views.home, name='home'),
    path('analyzer/', views.analyzer, name='analyzer'),
    path('news/', views.news, name='news'),
    path('risk/', views.risk, name='risk'),
    path('wealth/', views.wealth, name='wealth'),
    path('compare/', views.compare, name='compare'),
    path('about/', views.about, name='about'),
    
    # APIs
    path('api/market_status/', views.api_market_status, name='api_market'),
    path('api/analyze/', views.api_analyze, name='api_analyze'),
    path('api/news/', views.api_news, name='api_news'),
    path('api/risk/', views.api_risk, name='api_risk'),
    path('api/compare/', views.api_compare, name='api_compare'),
]