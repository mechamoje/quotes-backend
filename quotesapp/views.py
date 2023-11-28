from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import Quote, Author, Favorite
from .serializers import QuoteSerializer, AuthorSerializer, FavoriteSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def show_quotes(request):
    quotes = Quote.objects.all()
    serialized = QuoteSerializer(quotes, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def quote_details(request, id):
    try:
        quote = Quote.objects.get(id=id)
        serialized = QuoteSerializer(quote)  
        return Response(serialized.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def show_authors(request):
    authors = Author.objects.all()
    serialized = AuthorSerializer(authors, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def show_favorites(request):
    favorites = Favorite.objects.all()
    serialized = FavoriteSerializer(favorites, many=True)
    return Response(serialized.data)

@api_view(['POST'])
def signup_user(request):
    serialized = UserSerializer(data= request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username= username, password= password)
    if user:
        token, _ = Token.objects.get_or_create(user= user)
        return Response({'token': token.key}) 
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_quote(request):
    serialized = QuoteSerializer(data= request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)