from datetime import *
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from simple_history.models import HistoricalRecords

class Bylaws(TimeStampedModel):
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
    content = models.TextField(_('Content'))
    history = HistoricalRecords()

    objects = BylawsManager()
    adopted_objects = AdoptedManager()

    class Meta:
        verbose_name = _('Bylaws')
        verbose_name_plural = _('Bylaws')
        ordering = ('status', '-modified',)
        get_latest_by='-modified'
    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('by-bylaws-detail', None, {'slug': self.slug})
    
    @property
    def adopted(self): # Find the most recently adopted version of a set of bylaws
        for b in self.history.all():
            if b.status=='A':
                return b
        return None

    @property
    def diff(self, past_bylaws):
        return 'Call diff from cli on self and the past_bylaws'

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
