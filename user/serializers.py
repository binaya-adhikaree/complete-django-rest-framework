from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
       

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password,**validated_data)
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
            email = data.get("email")
            password = data.get("password")

            if email and password:
                user = authenticate(email=email, password=password)
                if user and user.is_active:
                    data["user"] = user
                    return data
                else :
                    raise serializers.ValidationError("invalid username or passwrod")
            else:
                raise serializers.ValidationError("email and password are required")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email",'avatar','email_verified']

        extra_kwargs = {
            "avatar" : {"required":False},
        }


class ChangePasswordSerailizer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


