from rest_framework import serializers
from account import models
from rest_framework import validators

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
       write_only=True,
       required=True
    )
    email = serializers.CharField(
       validators=[
           validators.UniqueValidator(
               queryset = models.User.objects.all(),
                message = ("Email already exists")
            )
        ]
    )
    is_staff = serializers.BooleanField( 
        required=True
    )
    is_superuser = serializers.BooleanField(
        required=True
    )
    last_login = serializers.DateTimeField(
        read_only=True
    )
    
    def create(self, validated_data):
        instance = models.User(**validated_data)
        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    
    class Meta:
        model = models.User
        fields = ('id', 'email', 'full_name', 'password', 'is_superuser', 'is_staff', 'last_login')
        extra_kwargs = {
            "url": {
                "view_name": "account:users:item-detail",
                "lookup_field": "pk",
            }
        }

class UserAdress(serializers.ModelSerializer):
    class Meta:
        model = models.UserAdress
        fields = '__all__'