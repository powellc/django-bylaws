from django.db import models

DRAFT  = 'D'
ADOPTED= 'A'

class NoActiveBylaws(ValidationError): pass

def BylawsManager(models.Manager):
    def get_current_bylaws(self):
        try:
            return self.filter(status=ADOPTED)[0]
        except self.model.DoesNotExist:
            raise NoActiveBylaws('Please create an active Bylaws document')

def AdoptedManager(models.Manager):
	def get_query_set(self):
		return super(AdoptedManager, self).get_query_set().filter(status=ADOPTED)



