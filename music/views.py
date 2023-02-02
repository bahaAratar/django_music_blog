from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models import Music
from music.serializers import MusicSerializers

@api_view(['GET'])
def get_hello(request):
    return Response('hello work')

@api_view(['GET'])
def get_music(reqest):
    music = Music.objects.all()
    serializer = MusicSerializers(music, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_song(reqest, id):
    try:
        song = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('нет такой песни')

    serializer = MusicSerializers(song, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_title(reqest, title):
    try:
        song = Music.objects.get(title=title)
    except Music.DoesNotExist:
        return Response('нет такой песни')

    serializer = MusicSerializers(song, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def post_music(reqest):
    serializer = MusicSerializers(data=reqest.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# DELETE, PUT, PATCH