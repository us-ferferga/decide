import json
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.http import Http404
from base import mods


# TODO: check permissions and census
class BoothView(TemplateView):
    template_name = 'old/booth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            # Casting numbers to string to manage in javascript with BigInt
            # and avoid problems with js and big number conversion
            for k, v in r[0]['pub_key'].items():
                r[0]['pub_key'][k] = str(v)

            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        context['KEYBITS'] = settings.KEYBITS

        return context

class NewBoothFrontendView(TemplateView):
    def get(self, request):
        return render(request, 'new/index.html')
    
class PingView(APIView):
    """
    Simplemente devuelve un 200 OK para que el cliente sepa que el servidor está activo y existe una API REST disponible
    """
    def get():
        return Response(status=status.HTTP_200_OK)
    
class BoothApiView(APIView):
    def get(self, request, vid):
        try:
            r = mods.get('voting', params={'id': vid})
            # Casting numbers to string to manage in javascript with BigInt
            # and avoid problems with js and big number conversion
            for k, v in r[0]['pub_key'].items():
                r[0]['pub_key'][k] = str(v)

            voting_data = r[0]
        except:
            return Response(status=status.HTTP_404_OK)

        keybits = settings.KEYBITS

        context = {
            'voting': voting_data,
            'KEYBITS': keybits
        }

        return Response(context, status=status.HTTP_200_OK)
