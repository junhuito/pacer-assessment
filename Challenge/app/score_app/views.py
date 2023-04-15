from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from score_app.models import Score

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Task 1: Simple Backend Endpoint
@api_view(['GET'])
@permission_classes([AllowAny])
def get_score(request):
    input_score = int(request.GET.get('input'))
    score = input_score + 1
    return JsonResponse({'score': score})

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):
    name = request.POST.get('name')
    score = request.POST.get('score')
    Score.objects.create(name=name, score=score)
    return JsonResponse({'message': "success"})

@api_view(['GET'])
@permission_classes([AllowAny])
def getAll(request):
    try:
        scores = Score.objects.all().values()
        return JsonResponse(list(scores), safe=False)
    except Score.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)

@api_view(['GET'])
@permission_classes([AllowAny])
def get(request, id):
    try:
        score = Score.objects.get(id=id)
        response = {
            "name": score.name,
            "created_at": score.created_at,
            "score": score.score,
        }
        return JsonResponse(response, safe=False)
    except Score.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)