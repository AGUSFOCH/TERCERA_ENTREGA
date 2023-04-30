from django.db import models

#class clase_Usuario:
    
    #def __init__(self,login,birthday,mail,name,interest):
        #self.login=login
        #self.birthday = birthday
        #self.mail= mail
        #self.name=name
        #self.interest=[interest]
    ##Metodo para calcular la edad del usuario
    #def edad(self):
        #from datetime import datetime,timedelta
        #a=datetime.strptime(self.birthday, "%d/%m/%Y").year
        #b=datetime.now().year
       # edad=(b-a)
       # print(f"Tienes {edad} años")
    #def __len__(self):
        #return len(self.interest)
    #Metodo para poder imprimir los atributos de la instancia
    #def __str__(self):
       # return f"Login:{self.login} \nNombre:{self.name} \nEmail:{self.mail}\nFecha de nacimiento:{self.birthday}\nIntereses:{self.interest}"
    #def __getitem__(self):
      #  return self.interest
   # #Metodo para agregar intereses
   #def __setitem__(self,interest,value):
        #self.interest=value

class Pasajero(models.Model):
    pasajero_nombre=models.CharField(max_length=20)
    pasajero_apellido=models.CharField(max_length=30)
    pasajero_id=models.CharField(max_length=10, primary_key=True)
    pasajero_mail=models.EmailField()
    pasajero_fecha_nac=models.DateField()  
    
class viajes(models.Model):
    viajes_reserva= models.CharField(max_length=10, primary_key=True)
    viajes_origen=models.CharField(max_length=40)
    viajes_destino= models.CharField(max_length=40)
    viajes_fecha_ini=models.DateField()  
    viajes_pasajero_id=models.CharField(max_length=10)
    viajes_cant_pasajeros=models.IntegerField()
    viajes_comentarios= models.CharField(max_length=300, blank=True)
    

class Hoteles(models.Model):
    hotel_reserva=models.CharField(max_length=30, primary_key=True)
    hotel_nombre=models.CharField(max_length=30)
    hotel_direccion=models.CharField(max_length=30)
    hotel_pasajero_id=models.CharField(max_length=10)
    hotel_ciudad=models.CharField(max_length=30)
    hotel_fecha_ini= models.DateField()
    hotel_cant_noches=models.IntegerField()
    hotel_contacto=models.EmailField(blank=True)

    