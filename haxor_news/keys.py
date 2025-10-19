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

from prompt_toolkit.key_binding import KeyBindings


class KeyManager:
    """Custom key bindings for haxor-news.

    Handles:
        * F10: Exit application
        * Ctrl+Space: Toggle completion menu
        * F2: Toggle comment pagination (disabled)

    :type bindings: :class:`prompt_toolkit.key_binding.KeyBindings`
    :param bindings: An instance of KeyBindings.
    """

    def __init__(self, set_paginate_comments, get_paginate_comments):
        self.bindings = KeyBindings()
        self._create_key_bindings(set_paginate_comments, get_paginate_comments)

    def _create_key_bindings(self, set_paginate_comments, get_paginate_comments):
        """Create and initialize key bindings.

        :type set_paginate_comments: callable
        :param set_paginate_comments: Sets the paginate comments config.

        :type get_paginate_comments: callable
        :param get_paginate_comments: Gets the paginate comments config.
        """
        assert callable(set_paginate_comments)
        assert callable(get_paginate_comments)

        @self.bindings.add("f2")
        def handle_f2(event):
            """Enable/Disable paginate comments mode.

            This method is currently disabled.

            :type event: :class:`prompt_toolkit.key_processor.KeyPressEvent`
            :param event: Key press event.
            """
            # set_paginate_comments(not get_paginate_comments())
            pass

        @self.bindings.add("f10")
        def handle_f10(event):
            """Quit when F10 is pressed.

            :type event: :class:`prompt_toolkit.key_processor.KeyPressEvent`
            :param event: Key press event.
            """
            event.app.exit()

        @self.bindings.add("c-space")
        def handle_ctrl_space(event):
            """Initialize autocompletion at the cursor.

            If the autocompletion menu is not showing, display it with the
            appropriate completions for the context.

            If the menu is showing, select the next completion.

            :type event: :class:`prompt_toolkit.key_processor.KeyPressEvent`
            :param event: Key press event.
            """
            buff = event.app.current_buffer
            if buff.complete_state:
                buff.complete_next()
            else:
                buff.start_completion(select_first=False)
