from datetime import  datetime
from django.db.models import Q
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializers import UserSerializer, UserFullInfoSerializer, UserUpdateInfoSerializer
from ATPlatform.settings import PASSWORD_STRING
from utils import encrypt


class UserLoginViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    '''
    User login view
    '''
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        request_data = request.data
        encrypt_password = encrypt.encrypt_pwd_md5(request_data['password'] + PASSWORD_STRING)

        userqueryset = UserProfile.objects.filter(Q(username=request_data['username']) & Q(password = encrypt_password))
        if userqueryset:
            users_serializer = UserFullInfoSerializer(userqueryset, many=True)
            response_data = users_serializer.data[0]
            res_data= {}
            res_data['user'] = response_data
            res_data['user']['password'] = ''
            res_data['msg'] = 'Success'
            res_data['code'] = 200
            return Response(res_data, status=status.HTTP_200_OK)
        else:
            response_error = {
                'msg':'Username or password is wrong',
                'code':400
            }
            return Response(response_error,status=status.HTTP_404_NOT_FOUND)


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    User register view --- encrypt password
    '''
    queryset = UserProfile.objects.all()
    serializer_class = UserFullInfoSerializer

    def perform_create(self, serializer):
        encrypt_password = self.get_password()
        serializer.save(password=encrypt_password)

    def get_password(self):
        request_pwd = self.request.data['password']
        encrypt_pwd = encrypt.encrypt_pwd_md5(request_pwd + PASSWORD_STRING)
        return encrypt_pwd

class UserUpdateInfoViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    '''
    User update view --- not include password
    '''
    queryset = UserProfile.objects.all()
    serializer_class = UserUpdateInfoSerializer

    def perform_update(self, serializer):
        serializer.save(updated_time = datetime.now())



