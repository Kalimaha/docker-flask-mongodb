from geobricks_rest_engine.config.common_settings import settings as common_settings
from geobricks_rest_engine.config.rest_settings import settings as rest_settings
from geobricks_rest_engine.core.utils import dict_merge
from geobricks_rest_engine.rest import engine as rest_engine
from geobricks_common_settings import settings_app
from geobricks_rest_settings import settings_rest_modules

#from geobricks_common.rest import common_rest

# loading settings
common_settings["settings"] = dict_merge(common_settings, settings_app)
common_settings["settings"] = common_settings["settings"]["settings"]

# loading  modules
rest_settings["settings"] = dict_merge(rest_settings, settings_rest_modules)
rest_settings["settings"] = rest_settings["settings"]["settings"]


rest_engine.run_engine()