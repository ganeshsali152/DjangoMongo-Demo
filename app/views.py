from django.shortcuts import render
from rest_framework_mongoengine.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from .serializers import MovieSerializer, MovieGetSerializer
from .models import Movie
from rest_framework.response import Response

class MovieCreateAPIView(CreateAPIView):
    serializer_class = MovieSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({"Status": 400,"ResponseCode":0,"Message":serializer.errors})

        serializer.save()
        # Movie.objects.create(**serializer.validated_data)
        return Response({"Status": 200,"ResponseCode":1,"Message":"Movie Added",
            "Results":serializer.data})
            
class MovieViewSet(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieGetSerializer


class MovieByTitleAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        if Movie.objects.filter(title=self.kwargs["title"]).first():
            obj = Movie.objects.get(title=self.kwargs["title"])
            serializer = self.get_serializer(obj)
            return Response({"Status": 200,"ResponseCode":1,"Message":"Data found",
                "Results":serializer.data})
        else:
           return Response({"Status": 400,"ResponseCode":0,"Message":"Invalid Request (Movie not found)"})


class MovieUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MovieSerializer

    def patch(self, request, *args, **kwargs):
        
        if not Movie.objects.filter(title=self.kwargs["title"]).first():
           return Response({"Status": 400,"ResponseCode":0,"Message":"Invalid Request (Movie not found)"})
        else:
            obj = Movie.objects.get(title=self.kwargs["title"])

        serializer = MovieUpdateSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            return Response({"Status": 200,"ResponseCode":1,"Message":"Movie Updated",
                    "Results":serializer.data})
        return Response({"Status": 400,"ResponseCode":0,"Message":serializer.errors})    



class MovieDeleteAPIView(RetrieveDestroyAPIView):

    def delete(self, request, *args, **kwargs):
        if not Movie.objects.filter(title=self.kwargs["title"]).first():
           return Response({"Status": 400,"ResponseCode":0,"Message":"Invalid Request (Movie not found)"})
        else:
            obj = Movie.objects.get(title=self.kwargs["title"])
            obj.delete()

        return Response({"Status": 200,"ResponseCode":1,"Message":"Movie Deleted"})   