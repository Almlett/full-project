# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Api,Proyect

class gateway(APIView):
    authentication_classes = ()

    def api_list(self, request):
        proyects = Proyect.objects.all()
        result = []
        for item in proyects:
            proyect = {
                'name':item.name,
                'host':item.host,
                'port':item.port,
                'urls':[],
            }

            urls = Api.objects.filter(origin=item)
            urls_list = {}
            for url in urls:
                urls_list["/" + url.name] = "http://{}:{}/{}".format(proyect['host'],proyect['port'],url.request_path)
            proyect['urls'] = urls_list
            
            result.append(proyect)
        return result

    def operation(self, request):
        path = request.path_info.split('/')
        print(path)
        if len(path) < 2:
            return Response('bad request', status=status.HTTP_400_BAD_REQUEST)

        if path[1] == 'api_list':
            data = self.api_list(request)
            return Response(data={'result':data}, status=status.HTTP_200_OK)

        apimodel = Api.objects.filter(name=path[1])
        if apimodel.count() != 1:
            return Response({'result':'bad request', 'description':'url not found'}, status=status.HTTP_400_BAD_REQUEST)

        valid, msg = apimodel[0].check_plugin(request)
        if not valid:
            return Response({'result':msg}, status=status.HTTP_400_BAD_REQUEST)

        res = apimodel[0].send_request(request)
        if res.headers.get('Content-Type', '').lower() == 'application/json':
            data = res.json()
        else:
            data = res.content
        return Response(data={'result':data}, status=res.status_code)
    
    def get(self, request):
        return self.operation(request)

    def post(self, request):
        return self.operation(request)

    def put(self, request):
        return self.operation(request)
    
    def patch(self, request):
        return self.operation(request)
    
    def delete(self, request):
        return self.operation(request)
