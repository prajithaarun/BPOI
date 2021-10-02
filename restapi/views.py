from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import student
from .serializers import studentSerializer


def restapi(request):
    return HttpResponse("Welcome To Rest API Page")
@csrf_exempt
def student_list(request):

    if request.method == 'GET':
        students = student.objects.all()
        serializer = studentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = studentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        students = student.objects.get(pk=pk)
    except students.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = studentSerializer(students)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = studentSerializer(students, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        students.delete()
        return HttpResponse(status=204)