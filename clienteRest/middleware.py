from rest_framework.authtoken.models import Token
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
class TokenAuth:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated():
            response = self.get_response(request)
            user=request.user
            token=get_object_or_404(Token, user_id=user.id)
            value=token.key
            response['Authorization'] = " Token "+ value
            return response
        else:
            pass