from django.urls import path, include
from elements import views


urlpatterns = [
    path('import', views.element_import),
    path('detail/<str:element_name>/<int:element_id>', views.detail_element),
    path('detail/<str:element_name>/', views.detail_element),
    path('reset/', views.reset_db)
]
