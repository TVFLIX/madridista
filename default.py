# -*- coding: utf-8 -*-
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.madridistatvflix'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "PLVcXfaIvw6awbAsa5Fj1qOyKdHRvvjiTO"

# Entry point
def run():
    plugintools.log("madridista tv.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("madridista tv.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="PARTIDOS COMPLETOS REAL MADRID",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://i.imgur.com/xxLqmN9.png",
        folder=True )

        
run()
