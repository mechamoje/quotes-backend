from rest_framework import serializers
from .models import Quote, Author, Favorite
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'birthday_date', 'photo' ]

class QuoteSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many= True)

    class Meta:
        model = Quote
        fields = [ 'id', 'body_text', 'title', 'authors' , 'created_date', 'feeling' ]

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ['user', 'quote' ]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {
                        'write_only': True
                        }}

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('The password should have more than 8 characters.')
        else:
            return value
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user= user)
        return user
