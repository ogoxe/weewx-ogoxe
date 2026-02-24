"""
Credits:
 Installer derived from https://github.com/smeisens/weewx-wundergroundlike
 in turn derived from the weewx Belchertown skin installer
 https://raw.githubusercontent.com/poblabs/weewx-belchertown/master/install.py
 which was Copyright Pat O'Brien, with re-fomatting from a PR by Vince Skahan 
"""

import configobj
from setup import ExtensionInstaller

# Python 3
from io import StringIO

#-------- extension info -----------

VERSION      = "1.0.1"
NAME         = 'OgoxeUploader'
DESCRIPTION  = 'Post to the OgoXe weather platform'
AUTHOR       = "OgoXe SAS"
AUTHOR_EMAIL = "dev@ogoxe.com"

#-------- main loader -----------

def loader():
    return OgoxeUploaderInstaller()

class OgoxeUploaderInstaller(ExtensionInstaller):
    def __init__(self):
        super(OgoxeUploaderInstaller, self).__init__(
            version=VERSION,
            name=NAME,
            description=DESCRIPTION,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            config=config_dict,
            files=files_dict,
            restful_services=restful_dict
        )

#----------------------------------
#         config stanza
#----------------------------------

extension_config = """

[StdRESTful]

    [[OgoxeUploader]]
        # This section is for configuring posts to the Ogoxe Weather Platform
        # that expects Weather Underground formatted data (without the "Rapidfire" protocol). 

        # The current uploader relies on WeeWX's builtin Weather Underground uploader,
        # thus, optional parameters supported by weewx-5.2.0 'should' work.
        # Please consult the weewx documentation for details.

        # To enable this uploader, set enable = True below and specify your
        # appropriate values for station, password.
        # The server url is preset and cannot be modified.

        enable = false
        station = replace_me
        password = replace_me

"""
config_dict = configobj.ConfigObj(StringIO(extension_config))

#----------------------------------
#  files and services stanzas
#----------------------------------
files=[('bin/user', ['bin/user/ogoxeUploader.py'])]
files_dict = files

restful_services = ['user.ogoxeUploader.OgoxeUploader']
restful_dict = restful_services

#---------------------------------
#          done
#---------------------------------
