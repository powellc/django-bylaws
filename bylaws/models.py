from datetime import *
from django.conf import settings
from django.db import models
from django.contrib.markup.templatetags import markup
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel
from markup_mixin.models import MarkupMixin
from simple_history.models import HistoricalRecords
from bylaws.managers import BylawsManager, AdoptedManager
from bylaws.utils.diff import textDiff

DEFAULT_DB = getattr(settings, 'DEFAULT_DB', 'default')

class Bylaws(MarkupMixin, TimeStampedModel):
    '''
    Bylaws model.
    
    Just keeps track of bylaws, plus any revisions.
    '''
    DRAFT  = 'D'
    ADOPTED= 'A'
    
    BYLAW_STATUS=(
        (DRAFT, 'Draft'),
        (ADOPTED, 'Adopted'),
    )
    title = models.CharField(max_length=30, blank=True, null=True)
    slug = models.SlugField(_('Slug'))
    status  = models.CharField(_('Status'), choices=BYLAW_STATUS, default=DRAFT, max_length=1)
    adopted_date = models.DateField(_('Adopted date'), blank=True, null=True)
    content = models.TextField(_('Content'))
    rendered_content = models.TextField(_('Rendered content'), blank=True)
    sites = models.ManyToManyField(Site)
    history = HistoricalRecords()

    objects = BylawsManager()
    adopted_objects = AdoptedManager()

    class Meta:
        verbose_name = _('Bylaws')
        verbose_name_plural = _('Bylaws')
        get_latest_by='adopted_date'
    
    class MarkupOptions:
        source_field = 'content'
        rendered_field = 'rendered_content'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
      # TODO: Set adopted_date if status has gone from draft -> adopted
      super(Bylaws, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('by-bylaws-detail', None, {'year_month_slug': self.modified.year + '-' + self.modified.month})
    
    @property
    def adopted(self): # Find the most recently adopted version of a set of bylaws
        for b in self.history.all():
            if b.status=='A':
                return b
        return None

    def diff(self, past_bylaws=None):
        if past_bylaws:
            return textDiff(self.rendered_content, past_bylaws.rendered_content)
        else:
            return self.rendered_content

class UserSignature(TimeStampedModel):
    '''User signature model
    
       Keeps track of whether a user has signed the bylaws
    '''
    bylaws=models.ForeignKey(Bylaws)
    user=models.ForeignKey(User)
    
    class Meta:
        verbose_name = _('Signature')
        verbose_name_plural = _('Signatures')
    
    def __unicode__(self):
        return u'%s has signed %s' % (self.user, self.bylaws)

    @property
    def signed_on(self):
        return self.created

    def has_user_agreed_latest_bylaws(user):
        if UserSignature.objects.filter(bylaws=Bylaws.objects.get_current_bylaws(),user=user):
            return True
        return False
