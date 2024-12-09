from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer) :
    
    password = serializers.CharField(max_length = 150 , write_only =  True)
    
    
    class Meta :
        
        model = User 
        fields = ['username', 'email','password']
        
        
    def create (self , validated_data) :
            
        return User.objects.create_user (**validated_data)
        

class LoginSerializer(serializers.ModelSerializer) :
    
    password = serializers.CharField(max_length = 150 , write_only =  True)
    
    
    class Meta :
        
        model = User 
        fields = ['username', 'email','password', 'token']
        read_only_fields = ['token' ,]
        
     
        