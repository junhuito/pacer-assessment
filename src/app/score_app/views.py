from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from score_app.models import Score

from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response



# Task 1: Simple Backend Endpoint
@swagger_auto_schema(
    method='get',
    operation_description='Given a input, return input + 1',
    manual_parameters=[
        openapi.Parameter(
            name='input',
            in_=openapi.IN_QUERY,
            required=True,
            type=openapi.TYPE_INTEGER,
            example=42
        )
    ],
    responses={
        200: openapi.Response(
            description='',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'score': openapi.Schema(type=openapi.TYPE_INTEGER)
                }
            )
        )
    }
)
@api_view(['GET'])
def get_score(request):
    input_score = int(request.GET.get('input'))
    score = input_score + 1
    return Response({'score': score})

@swagger_auto_schema(
    method='post',
    operation_description='Create a new user',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name', 'score'],
        properties={
            'name': openapi.Schema(
                type=openapi.TYPE_STRING,
                example='John',
            ),
            'score': openapi.Schema(
                type=openapi.TYPE_INTEGER,
                example=99,
            ),
        },
    ),
)
@csrf_exempt
@api_view(['POST'])
def create(request):
    name = request.POST.get('name')
    score = request.POST.get('score')
    Score.objects.create(name=name, score=score)
    return Response({'message': "success"})

@swagger_auto_schema(
    method='get',
    operation_description='Get all user',
    responses={
        200: openapi.Response(
            description='',
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'created_at': openapi.Schema(type=openapi.FORMAT_DATETIME),
                        'field2': openapi.Schema(type=openapi.TYPE_STRING),
                        'score': openapi.Schema(type=openapi.TYPE_INTEGER)
                    }
                )
            )
        )
    }
)
@api_view(['GET'])
def getAll(request):
    try:
        scores = Score.objects.all().values()
        return Response(list(scores))
    except Score.DoesNotExist:
        return Response({'message': 'User not found'}, status=404)

@swagger_auto_schema(
    method='get',
    operation_description='Get single user',
    responses={
        200: openapi.Response(
            description='',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'created_at': openapi.Schema(type=openapi.FORMAT_DATETIME),
                    'score': openapi.Schema(type=openapi.TYPE_INTEGER)
                }
            )
        )
    }
)
@api_view(['GET'])
def get(request, id):
    try:
        score = Score.objects.get(id=id)
        response = {
            "name": score.name,
            "created_at": score.created_at,
            "score": score.score,
        }
        return Response(response)
    except Score.DoesNotExist:
        return Response({'message': 'User not found'}, status=404)