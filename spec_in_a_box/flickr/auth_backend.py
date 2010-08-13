from django.contrib.auth.models import User
from spec_in_a_box import settings

class flickrIdentityCreator:
    @staticmethod
    def create_or_find(credential, save_on_create=False):
        pass
    
class flickrBackend:
    def authenticate(self, credential):
        identity = flickrIdentityCreator.create_or_find(credential)
        if identity.user is None:
            count = User.objects.filter(username__startswith = "flickr_%s" % identity.flickr_user_id)
            if count:
                username = 'flickr_%s%s' % (identity.flickr_user_id, count+1)
            else:
                username = 'flickr_%s%s'
            
            email_address = '%sflickruser.%s.com' % (username, settings.SITE_NAME)
            
            user = User.objects.create_user(username=username, email=email_address)  # the password should be unusable
            
            identity.user = user
            identity.save()
            return user
        else:
            return identity.user
    
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except:
            return None