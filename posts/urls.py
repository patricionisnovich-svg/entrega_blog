from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acercade/', views.acercade, name='acercade'),
    path("lista/", views.lista_posts, name="lista_posts"),
    path("crear/", views.crear_post, name="crear_post"),
    path("<slug:slug>/editar/", views.editar_post, name="editar_post"),
    path("<slug:slug>/eliminar/", views.eliminar_post, name="eliminar_post"),
    path("<slug:slug>/", views.detalle_post, name="detalle_post"), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)