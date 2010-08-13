from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

# This isn't "GeoDjango" aware because Spec-In-A-Box is meant to be as easy
# as possible to get up and running.  GeoDjango is not that easy to get running
# and we use our own Geo system that is different anyway.
# (hint, see: http://github.com/nickvlku/mongoengine )
  
class Location(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    
    def __unicode__(self):
        return "(%s, %s)" % (self.x, self.y)

class Credential(models.Model):
    # Put in here the appropriate credential
    # Be it OAuth token, or something else
    pass
    
class Identity(models.Model):
    user = models.ForeignKey(User)
    sample_service_user_id = models.CharField(max_length=255)  # different services have different length requirements
    credential = models.ForeignKey(Credential)
    created_on = models.DateTimeField(auto_now_add=True)
    
    # Below add all the custom attributes for your identity
    
    # End custom attributes

class Url(models.Model):
    url = models.URLField(verify_exists=False)
    type = models.CharField(max_length=255)  # Something like 'thumbnail', 'medium', etc
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

# We're not using a tagging library because we want this as simple as possible
# and we have our own tagging system that we can port this too.

class Tag(models.Model):
    tag = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(Identity)
    description = models.CharField(max_length=255, blank=True, null=True)
    internal_service_id = models.CharField(max_length=255)
    internal_album_id = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    height = models.IntegerField()
    width = models.IntegerField()
    location = models.ForeignKey(Location)
    public = models.BooleanField(default=True)
    date_created = models.DateTimeField()
    urls = generic.GenericRelation(Url)
    tags = generic.GenericRelation(Tag)
    
    
