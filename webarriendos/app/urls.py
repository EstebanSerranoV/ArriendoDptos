from django.urls import path, include
from .views import home, galeria, contacto, agregar_producto, listar_productos,modificar_producto, eliminar_producto, \
    registro, ProductoViewset, error_facebook
from rest_framework import routers

#Urls de nuetra API

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)







urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    #ruta de Api
    path('api/', include(router.urls)),
    #Pagina error Facebook
    path('error-facebook/', error_facebook, name="error_facebook")

]
