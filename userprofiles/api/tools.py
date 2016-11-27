from datetime import datetime, timedelta

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from oauth2_provider.models import AccessToken, Application, RefreshToken
from oauthlib.common import generate_token

from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse


def get_token_json(access_token):
    return JsonResponse({
        'access_token':access_token.token,
        'expires_in':datetime.now() + timedelta(days=365),
        'token_type':'Bearer',
        'refresh_token':access_token.refresh_token.token,
        'scope':access_token.scope
    })


def get_access_token(user):
    application = Application.objects.get(name="Foodie")
    try:
        old_access_token = AccessToken.objects.get(user=user, application=application)
        old_refresh_token = RefreshToken.objects.get(user=user, access_token=old_access_token)
    except ObjectDoesNotExist:
        return HttpResponse('Have not set any token')
    else:
        old_access_token.delete()
        old_refresh_token.delete()
    new_token = generate_token()
    refresh_token = generate_token()
    access_token=AccessToken.objects.create(user=user, application=app, expires=datetime.now() + timedelta(days=365),token=new_token)
    RefreshToken.objects.create(user=user, application=app, token=refresh_token, access_token=access_token)
    print('aceess',AccessToken)
    return get_token_json(access_token)
