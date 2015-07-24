from argh import dispatch_commands
from argh.decorators import named, arg
import subprocess
import os
import shutil


@named('run')
@arg('--common_settings', help='Common Settings file')
@arg('--rest_settings',help='Rest Settings file')
@arg('--processes', help='Processes')
def start_engine(**kwargs):

    # add external configuration files
    # TODO: add check
    shutil.copyfile(kwargs['common_settings'], '/geobricks/common_settings.py')
    shutil.copyfile(kwargs['rest_settings'], '/geobricks/rest_settings.py')

    # set enviroment variable used for UWSGI
    if kwargs['processes']:
        os.environ["UWSGI_PROCESSES"] = kwargs['processes']

    # run script
    subprocess.call(["sh", "/geobricks/startup.sh"])
def main():
    dispatch_commands([start_engine])

if __name__ == '__main__':
    main()