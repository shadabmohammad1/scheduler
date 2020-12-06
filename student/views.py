# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response

from student.serializers import LoginSerializer

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username, password)
        
        return Response({'status': 'SUCCESS'})

