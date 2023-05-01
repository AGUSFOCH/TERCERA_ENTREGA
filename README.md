# TERCERA_ENTREGA
Web de inicio:http://127.0.0.1:8000/pasajeroformulario/inicio/

Para verificar el funcionamiento dle programa debe al menos ingresar  las siguentes clases:
PASAJEROS:
http://127.0.0.1:8000/pasajeroformulario/
VIAJES:http://127.0.0.1:8000/viajesformulario/

Nota: la Primarykey de pasajeros es pasajero_id, que esta vinculada a la Foreingt key ( viajes_pasajero_id)

Los campos IDENTIFICACIÓN que se ingres ane le formulario pasajeros, debé coincidir con PASAJERO ID  que se ingresa en el formulario viajes.

Tambien existe la clase HOTELES pero aun no esta relacionada con la busqueda.
VIAJES:http://127.0.0.1:8000/hotelesformulario/


Para verificar  que funcione el meyodo de busca se debe ingresar a la URL http://127.0.0.1:8000/busquedapasajero/

Al ingresar el id, arrojara los datos del pasajero y los viajes registrados.
En caso de no haber ingresado registros en el paso anterior se puede probar el funcionamiento con el ID: 35323982
