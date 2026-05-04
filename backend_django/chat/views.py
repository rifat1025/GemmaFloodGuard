import requests
from rest_framework.views import APIView
from rest_framework.response import Response

FASTAPI_URL = "http://127.0.0.1:8001/chat"

class ChatView(APIView):
    def post(self, request):
        res = requests.post(FASTAPI_URL, json=request.data)
        return Response(res.json()) 
