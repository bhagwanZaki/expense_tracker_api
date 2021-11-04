from rest_framework import generics,permissions,viewsets
from rest_framework.response import Response
from .serializers import *
from knox.models import AuthToken
from api.models import totalAmount
# register api

class RegisterAPI(generics.GenericAPIView):
    serializer_class =  registerSerializer

    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": userSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]

        })



#login api

class LoginAPI(generics.GenericAPIView):
    serializer_class = loginSerilaizer

    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        userProfile = totalAmount.objects.filter(user_linked=user.id).values()
        if userProfile:
            profileExists = True
        else:
            profileExists = False
        return Response({
            "user": userSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "profile": userProfile,
            "profileExists":profileExists

        })
    

# get user api


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = userSerializer

    def get_object(self):
        return self.request.user


class totalAmountAPI(viewsets.ModelViewSet):
    serializer_class = totalAmountSeriliazer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    
    queryset = totalAmount.objects.all()

    def get_queryset(self):
        return super(totalAmountAPI,self).get_queryset().filter(user_linked=self.request.user)
        # return self.request.user.initial.objects.all()

    def perform_create(self, serializer):
        print('============')
        print(serializer)
        print('============')
        serializer.save(user_linked=self.request.user)