from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from users.models import User

from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer

# Creamos las vistas para los EndPoints
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Creamos el EndPoint que devuelva los campos y el registro de usuarios menos la contraseña
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    # Generamos un Override del metodo GET
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    # Creamos el Override del metodo PUT
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)