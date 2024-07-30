"""This module is modified from yt-dlp's utils.py (
https://github.com/yt-dlp/yt-dlp/blob/94a1c5e642e468cebeb51f74c6c220434cb47d96/yt_dlp/utils/_utils.py#L612) The 
original code is licensed under the Unlicense License (https://unlicense.org), and the modified code is licensed under 
GNU General Public License v3.0 (https://www.gnu.org/licenses/gpl-3.0.html)
"""

import itertools
import re

# needed for sanitizing filenames in restricted mode
ACCENT_CHARS = dict(zip('ÂÃÄÀÁÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖŐØŒÙÚÛÜŰÝÞßàáâãäåæçèéêëìíîïðñòóôõöőøœùúûüűýþÿ',
                        itertools.chain('AAAAAA', ['AE'], 'CEEEEIIIIDNOOOOOOO', ['OE'], 'UUUUUY', ['TH', 'ss'],
                                        'aaaaaa', ['ae'], 'ceeeeiiiionooooooo', ['oe'], 'uuuuuy', ['th'], 'y')))


def sanitize_filename(s):
    """Sanitizes a string, so it could be used as part of a filename.
    @param s:           string to sanitize
    """
    if s == '':
        return ''

    def replace_insane(char):
        if char in ACCENT_CHARS:
            return ACCENT_CHARS[char]
        elif char == '\n':
            return ''
        elif char in '"*:<>?|/\\':
            # Replace with their full-width unicode counterparts
            return {'/': '\u29F8', '\\': '\u29f9'}.get(char, chr(ord(char) + 0xfee0))
        elif char == '?' or ord(char) < 32 or ord(char) == 127:
            return ' '
        elif char == '"':
            return ''
        elif char == ':':
            return '_-'
        elif char in '\\/|*<>':
            return '_'
        return char

    s = re.sub(r'[0-9]+(?::[0-9]+)+', lambda m: m.group(0).replace(':', '_'), s)  # Handle timestamps
    result = ''.join(map(replace_insane, s))

    return result
