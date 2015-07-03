from geobricks_rest_engine.config.common_settings import settings as common_settings
from geobricks_rest_engine.config.rest_settings import settings as rest_settings
from geobricks_rest_engine.core.utils import dict_merge
from geobricks_rest_engine.rest import engine as rest_engine
import imp


# TODO: add CLI interface
settings_app = imp.load_source('geobricks_common_settings','/geobricks/config/geobricks_common_settings.py')
settings_rest_modules = imp.load_source('geobricks_rest_settings', '/geobricks/config/geobricks_rest_settings.py')

print settings_rest_modules.settings_rest_modules
print settings_app.settings_app

# loading settings
common_settings["settings"] = dict_merge(common_settings, settings_app.settings_app)
common_settings["settings"] = common_settings["settings"]["settings"]

print common_settings

# loading  modules
rest_settings["settings"] = dict_merge(rest_settings, settings_rest_modules.settings_rest_modules)
rest_settings["settings"] = rest_settings["settings"]["settings"]

print rest_settings

rest_engine.run_engine()
