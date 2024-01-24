from django.shortcuts import render
from rest_framework.views import APIViews
from .serializers import *
from .models import *
from rest_framework.response import Response
# Create your views here.


class ReactView(APIView):
    def get(self, request):
        output = [{"employee": output.employee,
                   "department": output.department}
                    for output in React.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializers = ReactSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)