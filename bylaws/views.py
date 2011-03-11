from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from bylaws.models import Bylaws, UserSignature

def current_bylaws(request):
    object = Bylaws.adopted_objects.latest()
    return render_to_response('bylaws/bylaws_detail.html', locals(),
                              context_instance=RequestContext(request))
    
def bylaws_list(request):
    objects = Bylaws.objects.all()
    return render_to_response('bylaws/bylaws_list.html', locals(),
                              context_instance=RequestContext(request))

def bylaws_diff_list(request, year_month_slug):
    '''
    Returns an object looked up by when it was created so that it's history can be displayed and diffed
    '''
    year, month = year_month_slug.split('-')
    object = Bylaws.objects.get(created__year=year, created__month=month)
    try:
        history= object.history.all()
    except:
        history= None 
    return render_to_response('bylaws/bylaws_diff_list.html', locals(),
                              context_instance=RequestContext(request))

def bylaws_diff_detail(request, year_month_slug, version_id):
    '''
    Returns an object looked up by when it was created so that it's history can be displayed and diffed
    '''
    year, month = year_month_slug.split('-')
    object = Bylaws.objects.get(created__year=year, created__month=month)
    try:
        history= object.diff(object.history.all()[version_id])
    except:
        history= None 
    return render_to_response('bylaws/bylaws_diff_detail.html', locals(),
                              context_instance=RequestContext(request))

