# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 BigNoid
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import xbmc
import xbmcgui
import xbmcaddon
import sys
# import web_pdb; web_pdb.set_trace()

ADDON = xbmcaddon.Addon()


def main():
    videoTag = sys.listitem.getVideoInfoTag()
    if videoTag:
        title = videoTag.getTitle()
        year = videoTag.getYear()
        search = "{} ({}) trailer ita".format(title, year)
    # xbmcgui.Dialog().notification("Searching trailer", "{} ({})".format(title, year) )
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.youtube/kodion/search/query?q={}")'.format(search) )


if __name__ == '__main__':
    main()
