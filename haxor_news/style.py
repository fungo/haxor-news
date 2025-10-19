# -*- coding: utf-8

# Copyright 2015 Donne Martin. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from pygments.token import Token
from pygments.util import ClassNotFound
from prompt_toolkit.styles import Style
import pygments.styles


class StyleFactory(object):
    """Provide styles for the autocomplete menu and the toolbar.

    :type style: :class:`pygments.style.StyleMeta`
    :param style: An instance of `pygments.style.StyleMeta`.
    """

    def __init__(self, name):
        self.style = self.style_factory(name)

    def style_factory(self, name):
        """Retrieve the specified pygments style.

        If the specified style is not found, the vim style is returned.

        :type style_name: str
        :param style_name: The pygments style name.

        :rtype: :class:`pygments.style.StyleMeta`
        :return: An instance of `pygments.style.StyleMeta`.
        """
        try:
            pygments_style = pygments.styles.get_style_by_name(name)
        except ClassNotFound:
            pygments_style = pygments.styles.get_style_by_name('native')

        # Create styles dictionary.
        # In prompt-toolkit 3.x, Style.from_dict expects string keys
        # We use pygments_style as base but only add our custom UI styles
        styles = {
            'completion-menu.completion.current': 'bg:#00aaaa #000000',
            'completion-menu.completion': 'bg:#008888 #ffffff',
            'completion-menu.meta.completion.current': 'bg:#00aaaa #000000',
            'completion-menu.meta.completion': 'bg:#00aaaa #ffffff',
            'scrollbar.background': 'bg:#00aaaa',
            'scrollbar.button': 'bg:#003333',
            'bottom-toolbar': 'bg:#222222 #cccccc',
        }

        return Style.from_dict(styles)
