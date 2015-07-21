import click
import imp
from geobricks_common.core.log import logger

# Logger
log = logger(__file__)

@click.command()
@click.argument('--common_settings', nargs=1)
@click.argument('--rest_settings', nargs=1)
def start_server(common_settings, rest_settings):

    log.info(common_settings, rest_settings)
    from geobricks_rest_engine.config.common_settings import settings as common_settings
    from geobricks_rest_engine.config.rest_settings import settings as rest_settings
    from geobricks_rest_engine.core.utils import dict_merge
    from geobricks_rest_engine.rest import engine as rest_engine

    settings_app = imp.load_source('geobricks_common_settings', common_settings)
    settings_rest_modules = imp.load_source('geobricks_rest_settings', rest_settings)
    # loading settings
    common_settings["settings"] = dict_merge(common_settings, settings_app.settings_app)
    common_settings["settings"] = common_settings["settings"]["settings"]

    print common_settings

    # loading  modules
    rest_settings["settings"] = dict_merge(rest_settings, settings_rest_modules.settings_rest_modules)
    rest_settings["settings"] = rest_settings["settings"]["settings"]

    print rest_settings

    rest_engine.run_engine()


if __name__ == '__main__':
    start_server()