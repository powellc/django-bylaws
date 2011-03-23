from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail
from bylaws.models import Bylaws, UserSignature
from bylaws.views import current_bylaws, bylaws_diff_list, bylaws_diff_detail


'''
 <root>/current/ - the latest adopted bylaws
 if admin:
     <root>/<year>-<month>/diff - list of past versions with option to compare
     <root>/<year>-<month>/diff/<version_id> - show diff of current version with history version
'''

urlpatterns = patterns('',
    url(r'^current/$', current_bylaws, name="by-bylaws-current"),
    url(r'^(?P<year_month_slug>[-\d]+)/$', bylaws_diff_list, name="by-bylaws-diff-list"),
    url(r'^(?P<year_month_slug>[-\d]+)/diff/(?P<version_id>[\d]+)/$', bylaws_diff_detail, name="by-bylaws-diff-detail"),
    url(r'^(?P<year_month_slug>[-\d]+)/diff/(?P<version_id>[\d]+)/to/(?P<second_version_id>[\d]+)/$', bylaws_diff_detail, name="by-bylaws-diff-detail"),
)

