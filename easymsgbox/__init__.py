import ctypes



ICON_NUM={
    'error':16,
    'question':32,
    'warning':48,
    'info':64
}



def alert(title:str, text:str, icon = 'info'):
    """Creates a message box with OK button on it. Returns nothing.

    Args:
        `title`: Title of message box
        `text`: Description of message box
        `icon` (optional) : Icon, which will be used in message box. 
            Accepts values: 
                `error` - Stop-sign icon

                `question` -  Question-mark icon

                `warning` - Warning icon

                `info` (default) - Information-sign icon consisting of an 'i' in a circle.
    """
    msg_box = ctypes.windll.user32.MessageBoxW(0, text, title, ICON_NUM[icon])


def confirm(title:str, text:str, icon = 'question'):
    """Creates a message box with OK and Cancel buttons on it. 
    
    Returns `True`, if user clicked OK, `False` otherwise.

    Args:
        `title`: Title of message box
        `text`: Description of message box
        `icon` (optional) : Icon, which will be used in message box. 
            Accepts values: 
                `error` - Stop-sign icon

                `question` (default) -  Question-mark icon

                `warning` - Warning icon

                `info` - Information-sign icon consisting of an 'i' in a circle.
    """

    msg_box = ctypes.windll.user32.MessageBoxW(0, text, title, 1+ICON_NUM[icon])

    if msg_box==1:
        return True
    elif msg_box==2:
        return False


def agreement(title:str, text:str, is_cancel = False, icon = 'question',):
    """Creates a message box with Yes and No buttons on it. 
    
    Returns `True`, if user clicked Yes, 
    `False`, if user clicked No, 
    and `None`, if user clicked Cancel or closed the message box.

    Args:
        `title`: Title of message box
        `text`: Description of message box
        `icon` (optional) : Icon, which will be used in message box
            Accepts values: 
                `error` - Stop-sign icon

                `question` (default) -  Question-mark icon

                `warning` - Warning icon

                `info` - Information-sign icon consisting of an 'i' in a circle.
        `is_cancel`: if `True`, adds Cancel button
    """
    if is_cancel:
        msg_box = ctypes.windll.user32.MessageBoxW(0, text, title, 3+ICON_NUM[icon])
    else:
        msg_box = ctypes.windll.user32.MessageBoxW(0, text, title, 4+ICON_NUM[icon])

    if msg_box==6:
        return True
    elif msg_box==7:
        return False
    elif is_cancel and msg_box==2:
        return None
