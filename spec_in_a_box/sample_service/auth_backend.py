from django.contrib.auth.models import User
from spec_in_a_box import settings

class sample_serviceIdentityCreator:
    @staticmethod
    def create_or_find(credential, save_on_create=False):
        pass
    
class sample_serviceBackend:
    def authenticate(self, credential):
        identity = sample_serviceIdentityCreator.create_or_find(credential)
        if identity.user is None:
            count = User.objects.filter(username__startswith = "sample_service_%s" % identity.sample_service_user_id)
            if count:
                username = 'sample_service_%s%s' % (identity.sample_service_user_id, count+1)
            else:
                username = 'sample_service_%s%s'
            
            email_address = '%ssample_serviceuser.%s.com' % (username, settings.SITE_NAME)
            
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