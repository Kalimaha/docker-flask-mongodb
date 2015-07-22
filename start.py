from geobricks_rest_engine.core.utils import dict_merge
from geobricks_rest_engine.config.common_settings import settings as common_settings
from geobricks_rest_engine.config.rest_settings import settings as rest_settings
from geobricks_rest_engine.core.utils import dict_merge
from common_settings import settings_app
from rest_settings import settings_rest_modules
from geobricks_rest_engine.rest import engine

# settings_app = imp.load_source('geobricks_common_settings', '/geobricks/config/common_settings.py')
# settings_rest_modules = imp.load_source('geobricks_rest_settings', '/geobricks/config/rest_settings.py')

#from geobricks_common.rest import common_rest


print settings_app["settings"]
# print settings_rest_modules
# print common_settings

print "----------------"
# loading settings
common_settings["settings"] = dict_merge(common_settings, settings_app)
common_settings["settings"] = common_settings["settings"]["settings"]
print common_settings["settings"]

# loading  modules
rest_settings["settings"] = dict_merge(rest_settings, settings_rest_modules)
rest_settings["settings"] = rest_settings["settings"]["settings"]
print rest_settings["settings"]

# load engine
engine.run_engine(False)

# this is the variable returning to uwsgi
from geobricks_rest_engine.rest.engine import app