import json
from rest_framework.views import APIView, Response

class HelloApiView(APIView):
    """ API view test """

    def get(self, request, format=None):
        """ return list of api view characteristics"""
        an_apiview = [
            "usamos metodos htpp como funciones (get, post, patch, delete, put)",
            "Es similar a una vista tradicional de django",
            "nos da mayor control sobre la logica de la aplicacione",
            "Mapeado manualmente a los URLs",
        ]

        # convierte la info a json (tiene que ser una lista o un diccionario)
        return Response({
            "message" : "Hello",
            "an_apiview": an_apiview
        })