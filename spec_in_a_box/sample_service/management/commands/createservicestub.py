from django.core.management.base import BaseCommand, CommandError
import shutil
import fileinput
import sys

class Command(BaseCommand): 
    args = '<service name>'
    help = 'Creates a service stub so you can implement your own Spec in a Box'
    
    def handle(self, *args, **options):

        if not args:
            raise CommandError("Enter a service name")
        shutil.copytree("sample_service", args[0])

        files_to_replace = ['/urls.py', '/views.py', '/models.py', '/auth_backend.py']
        for file in files_to_replace:
            for line in fileinput.FileInput(args[0]+file,inplace=1):
                if "sample_service" in line:
                    line = line.replace('sample_service', args[0])
                sys.stdout.write(line)
