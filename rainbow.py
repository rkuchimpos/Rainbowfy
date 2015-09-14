from __future__ import print_function
import hexchat

__module_name__ = 'Rainbow'
__module_version__ = '1.0'
__module_description__ = 'Rainbowfies text'
__author__ = 'bigboy42'

rainbow_codes = [13, 4, 7, 8, 3, 11, 12]

def rainbow(word, word_eol, userdata):
    rainbow_text = ""
    i = 0
    max_len = len(rainbow_codes) - 1
    if len(word) > 1:
        for char in word_eol[1]:
            i += 1
            color = rainbow_codes[i % max_len]
            rainbow_text += '\003' + str(color) + char
        hexchat.command("say {}".format(rainbow_text))
    else:
        hexchat.command("help RAINBOW <text>")

    return hexchat.EAT_ALL

hexchat.hook_command("rainbow", rainbow, help="RAINBOW <text>")