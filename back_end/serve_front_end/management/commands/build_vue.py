from django.conf import settings
from django.core.management.base import BaseCommand
from os import system, path


class Command(BaseCommand):
    help = 'Dumps the data to json files'

    def handle(self, *args, **kwargs):
        self.stdout.write('Start to build vue.js')

        django_dir = settings.BASE_DIR
        self.stdout.write(f'-> djago project dir: {django_dir}')
        static_dir = path.join(django_dir, 'serve_front_end/static')
        self.stdout.write(f'-> djago static dir: {static_dir}')
        template_dir = path.join(django_dir, 'serve_front_end/templates')
        self.stdout.write(f'-> djago template dir: {template_dir}')

        vue_dir = path.join(django_dir, '../front_end')
        self.stdout.write(f'\n-> vue project dir: {vue_dir}')
        vue_dist_dir = path.join(vue_dir, 'dist')
        self.stdout.write(f'-> vue dist dir: {vue_dist_dir}')

        system(f'cd {vue_dir} && BASE_URL="static/" npm run build')

        system(f'cp -r {path.join(vue_dist_dir, "css")} {static_dir}')
        system(f'cp -r {path.join(vue_dist_dir, "js")} {static_dir}')
        system(f'cp {path.join(vue_dist_dir, "favicon.ico")} {static_dir}')

        system(f'cp {path.join(vue_dist_dir, "index.html")} {template_dir}')

        self.stdout.write('End to build vue.js')
