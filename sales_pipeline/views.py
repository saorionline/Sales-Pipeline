import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def pandadoc_webhook(request):
    if request.method == 'POST':
        try:
            # Imprime lo que llega para ver el error en la terminal
            print("Cuerpo recibido:", request.body.decode('utf-8'))
            
            payload = json.loads(request.body)
            
            # PandaDoc puede enviar un diccionario simple o una lista
            if isinstance(payload, dict):
                events = [payload]
            else:
                events = payload

            for event in events:
                event_name = event.get('event')
                print(f"Evento detectado: {event_name}")
                # Aquí irá tu lógica para guardar en la base de datos
            
            return HttpResponse(status=200)
            
        except Exception as e:
            print(f"Error procesando JSON: {e}")
            return HttpResponse(content=str(e), status=400)
        # print("¡Dato recibido de PandaDoc!")
        # return HttpResponse(status=200)
    return HttpResponse(status=405)