from rest_framework.views import APIView, Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializer, models, permissions


class HelloApiView(APIView):
    """ API view test """
    serializer_class = serializer.HelloSerializer

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
            "message": "Hello",
            "an_apiview": an_apiview
        })

    def post(self, request):
        """ create a message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                "message": message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Update a object """
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """ update partial a object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """ delete a object """
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """ Test API view set """
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """ Return hello world message """
        a_viewset = [
            "Usa acciones (list, create, retrive, uptdate, partial_update, destroy)",
            "Automaticamenta mapea los URLs usando Routers",
            "Provee mas funcionalidad con menos codigo"
        ]

        return Response({
            "message": "Hola!",
            "a_viewset":  a_viewset
        })

    def create(self, request):
        """ create new hello world message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            
            return Response({
                "message": message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ get a object and id """
        return Response({
            "http method": "GET"
        })

    def update(self, request, pk=None):
        """ Update a object """
        return Response({
            "http method": "PUT"
        })

    def partial_update(self, request, pk=None):
        """ update a object """
        return Response({
            "http method": "PATCH"
        })

    def destroy(self, request, pk=None):
        """ delete a object """
        return Response({
            "http method": "DELETE"
        })


class UserProfileViewSet(viewsets.ModelViewSet):
    """ create and update profiles """
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
