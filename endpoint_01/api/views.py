from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from users.models import User
from . serializers import UserSerializer
import requests
from requests.auth import HTTPBasicAuth
import json


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        mail = serializer.validated_data['email']
        key = serializer.validated_data['key']
        url = f"https://fundacja997.atlassian.net/rest/api/2/user/search?query={mail}"
        basic = HTTPBasicAuth(mail, key)
        header = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.get(url, auth=basic, headers=header)
        fixed = response.content.decode()
        try:
            if json.loads(fixed)[0]["emailAddress"]:
                if serializer.is_valid():
                    serializer.save()
                    res_data = {"success": "true", "msg": "success"}
                    return Response(res_data, status=status.HTTP_201_CREATED)
        except IndexError:
            res_data = {"success": "false", "msg": "user not found"}
            return Response(res_data, status=status.HTTP_404_NOT_FOUND)
    res_data = {"success": "false", "msg": "bad request"}
    return Response(res_data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_issue(request):
    pass