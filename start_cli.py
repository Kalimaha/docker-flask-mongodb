from argh import dispatch_commands
from argh.decorators import named, arg
import imp
from geobricks_rest_engine.config.common_settings import settings as common_settings
from geobricks_rest_engine.config.rest_settings import settings as rest_settings
from geobricks_rest_engine.core.utils import dict_merge
from geobricks_rest_engine.rest import engine as rest_engine
from geobricks_rest_engine.rest.engine import app


@named('corr')
@arg('--common_settings', help='Common Settings file')
@arg('--rest_settings',help='Rest Settings file')
@arg('--bins',help='Bins')
def start_engine(**kwargs):
    settings_app = imp.load_source('geobricks_common_settings', kwargs['common_settings'])
    settings_rest_modules = imp.load_source('geobricks_rest_settings', kwargs['rest_settings'])
    # loading settings
    common_settings["settings"] = dict_merge(common_settings, settings_app.settings_app)
    common_settings["settings"] = common_settings["settings"]["settings"]

    # loading  modules
    rest_settings["settings"] = dict_merge(rest_settings, settings_rest_modules.settings_rest_modules)
    rest_settings["settings"] = rest_settings["settings"]["settings"]

    # run engine
    rest_engine.run_engine(False)

    # run uwsgi
    # env/bin/uwsgi --socket 127.0.0.1:21000 -w WSGI:app -p 2



def main():
    dispatch_commands([start_engine])

if __name__ == '__main__':
    main()