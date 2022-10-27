#!/usr/bin/env python 

"""
Go to Frame Number

URL:

    http://github.com/khanrahan/go-to-frame-number

Description:

    Takes one or more selected clips and/or sequences and moves the positioner to a
    specific frame number.

Menus:

    Right-click selected clips and/or sequences on the Desktop Reels --> Navigate...
    --> Go to Frame Number

    Right-click selected clips and/or sequences in the Media Panel --> Navigate...
    --> Go to Frame Number

To Install:

    For all users, copy this file to:                                                   
    /opt/Autodesk/shared/python                                                         
                                                                                        
    For a specific user, copy this file to:                                             
    /opt/Autodesk/user/<user name>/python 
"""


from __future__ import print_function

__title__ = "Go to Frame Number"
__title_version__ = "{} v{}".format(__title__, __version__)
__version_info__ = (0, 1, 0)
__version__ = ".".join([str(num) for num in __version_info__])

MESSAGE_PREFIX = "[PYTHON HOOK]"


def input_dialog(title, field):
    """Basic pop up window."""

    from PySide2.QtWidgets import QInputDialog

    text, ok = QInputDialog.getText(None, title, field)
    return text, ok


def message(string):
    """Print message to shell window and append global MESSAGE_PREFIX."""

    print(" ".join([MESSAGE_PREFIX, string]))


def go_to_frame(selection):
    """ """

    import flame
    
    message(__title_version__)
    message("Script called from {}".format(__file__))
    
    user_input = input_dialog(__title_version__, "Frame Number")

    if user_input[1] is True:
        tc = flame.PyTime(int(user_input[0]))

        for clip in selection:
            clip.current_time = tc
            message("{} positioner moved to frame {}".format(clip.name.get_value(),
                                                             user_input[0]))


def scope_clip(selection):
    """PyClip includes PySequences.  It is the parent, so this will be true
    for individual clips or full sequences."""

    import flame

    for item in selection:
        if isinstance(item, flame.PyClip):
            return True
    return False


def get_media_panel_custom_ui_actions():

    return [{'name': "Navigate...",
             'actions': [{'name': "Go to Frame Number",
                          'isVisible': scope_clip,
                          'execute': go_to_frame,
                          'minimumVersion': "2020.3.1"}]
            }]
