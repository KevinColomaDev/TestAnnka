from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Socio
import csv
import codecs
import json
from django.core.serializers import serialize
from django.core.mail import send_mail

def index(request):
    return render(request, 'url/index.html');

# Create your views here.

#Funcion para cargar csv, con llamado a la funcion de procesar_datos_csv
def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        archivo = request.FILES['csv_file']
        # Aquí puedes realizar el procesamiento que desees con el archivo CSV, por ejemplo, guardarlo en el servidor o procesar sus datos
        procesar_datos_csv(archivo)
            
        return render(request, 'url/upload_success.html')  # Renderiza una plantilla para mostrar el mensaje de éxito
    else:
        return render(request, 'url/upload_form.html')  # Renderiza una plantilla con un formulario para cargar el archivo CSV

#Funcion de validaciones de archivo csv y sobreescribir datos si en socio existe o para crear un socio nuevo
def procesar_datos_csv(archivo):

    
    csv_reader = csv.reader(codecs.iterdecode(archivo, 'utf-8'))
    next(csv_reader)

    for row in csv_reader:

        compania = row[1]
        nombre = row[2]
        apellido = row[3]
        cedula = row[4]
        ruc = row[5]
        ciudad = row[6]
        provincia = row[7]
        email = row[8]

        #Validadciones
        if not compania:
            raise ValueError('La compania no puede estar vacia')
        
        if nombre:
            try:
                nombre=str(nombre)
            except ValueError:
                raise ValueError('El nombre no puede contener numeros')
        else:
            nombre = None

        if apellido:
            try:
                apellido=str(apellido)
            except ValueError:
                raise ValueError('El apellido no puede contener numeros')
        else:
            apellido = None

        if cedula:
            try:
                cedula = int(cedula)
            except ValueError:
                raise ValueError('La cedula debe ser un valor numérico')
        else:
            cedula = None

        if ruc:
            try:
                ruc = int(ruc)
            except ValueError:
                raise ValueError('El RUC debe ser un valor numérico')
        else:
            raise ValueError('El RUC no puede estar vacio')

        if not ciudad:
            raise ValueError('La ciudad no puede estar vacia')

        if not provincia:
            raise ValueError('La provincia no puede estar vacia')
        
        if not email:
            raise ValueError('El email no puede estar vacio')

        #Se encarga de buscar si el socio existe por RUC
        socio_existente =Socio.objects.filter(ruc=ruc).first()

        if socio_existente:
            
            socio_existente.compania = compania
            socio_existente.nombre = nombre
            socio_existente.apellido = apellido
            socio_existente.cedula = cedula
            socio_existente.ruc = ruc
            socio_existente.ciudad = ciudad
            socio_existente.provincia = provincia
            socio_existente.email = email

            socio_existente.save()
            print(f"Socio existente actualizado: {socio_existente}")

        else:
            nuevo_socio = Socio(compania=compania, nombre=nombre, apellido=apellido, cedula=cedula, ruc=ruc, ciudad=ciudad, provincia=provincia, email=email)
            nuevo_socio.save()

            #Envio de correo electronico a un socio nuevo
            subject = 'Te damos la bienvenida como nuevo socio'
            message = f'Hola {Socio.nombre}, bienvenido como nuevo socio de Annka'
            from_email = 'ckevin100000@gmail.com'
            to_email = Socio.email
            send_mail(subject, message, from_email, [to_email], fail_silently= True)

            print(f"Nuevo socio creado: {nuevo_socio}")

    print("Procesamiento del archivo CSV completado") 
#Funcion para devolver la lista de socios en formato JSON
def obtener_socios(request):

    socios = Socio.objects.all()
    socios_json = serialize('json', socios)
    socios_list = json.loads(socios_json)

    return JsonResponse(socios_list, safe=False)