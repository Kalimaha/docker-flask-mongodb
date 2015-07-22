from argh import dispatch_commands
from argh.decorators import named, arg
import imp
import subprocess
import json
import shutil
# from geobricks_rest_engine.config.common_settings import settings as common_settings
# from geobricks_rest_engine.config.rest_settings import settings as rest_settings
# from geobricks_rest_engine.core.utils import dict_merge


@named('corr')
@arg('--common_settings', help='Common Settings file')
@arg('--rest_settings',help='Rest Settings file')
@arg('--processes', help='Processes')
def start_engine(**kwargs):
    # shutil.copyfile('/geobricks/__init__.py', '/geobricks/config/__init__.py')
    shutil.copyfile(kwargs['common_settings'], '/geobricks/common_settings.py')
    shutil.copyfile(kwargs['rest_settings'], '/geobricks/rest_settings.py')

    # run script
    subprocess.call(["sh", "/script.sh"])

    # run engine
    #rest_engine.run_engine(False)

    # run uwsgi
    #from geobricks_rest_engine.rest.engine import app
    #subprocess.call(["env/bin/uwsgi", "--socket", "127.0.0.1:21000", "-w", app])
    # env/bin/uwsgi --socket 127.0.0.1:21000 -w WSGI:app -p 2




def main():
    dispatch_commands([start_engine])

if __name__ == '__main__':
    main()