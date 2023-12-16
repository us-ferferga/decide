import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})                  
            context['voting'] = json.dumps(r[0])
        except:
            raise Http404("No existe la votación")

        return context
    
    def graphics(request, voting_id):
        template_graphics = 'graphics/graphics.html'
        try:
            r = mods.get('voting', params={'id': voting_id})
            context = {
            "voting_id": r[0].get('id'),
            "voting_name": r[0].get('name'),
            "results": r[0].get('postproc')
        }
        except:
            raise Http404("No existe la votación")
        
        return render(request, template_graphics, context)
