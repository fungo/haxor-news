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


from unittest import mock

from prompt_toolkit.keys import Keys

from haxor_news.haxor import Haxor
from tests.compat import unittest


class KeysTest(unittest.TestCase):
    def setUp(self):
        self.haxor = Haxor()
        self.bindings = self.haxor.key_manager.bindings

    def _find_binding(self, key):
        """Find a binding for the given key."""
        for binding in self.bindings.bindings:
            if binding.keys == (key,):
                return binding
        return None

    def test_f2_binding_exists(self):
        """Test that F2 key is bound."""
        binding = self._find_binding(Keys.F2)
        assert binding is not None, "F2 key binding not found"

    def test_f10_binding_exits(self):
        """Test that F10 key calls app.exit()."""
        binding = self._find_binding(Keys.F10)
        assert binding is not None, "F10 key binding not found"

        # Test the handler behavior
        mock_event = mock.Mock()
        mock_app = mock.Mock()
        mock_event.app = mock_app

        # Call the F10 handler
        binding.handler(mock_event)

        # Verify app.exit() was called
        mock_app.exit.assert_called_once()

    def test_ctrl_space_binding_autocomplete(self):
        """Test that Ctrl+Space triggers autocomplete."""
        # Ctrl+Space is bound as 'c-@' in prompt-toolkit
        binding = self._find_binding(Keys.ControlAt)
        assert binding is not None, "Ctrl+Space key binding not found"

        # Test the handler behavior with incomplete state
        mock_event = mock.Mock()
        mock_buffer = mock.Mock()
        mock_buffer.complete_state = None
        mock_event.app.current_buffer = mock_buffer

        # Call the handler
        binding.handler(mock_event)

        # Verify start_completion was called
        mock_buffer.start_completion.assert_called_once_with(select_first=False)

        # Test with existing complete state
        mock_buffer.reset_mock()
        mock_buffer.complete_state = mock.Mock()

        binding.handler(mock_event)

        # Verify complete_next was called instead
        mock_buffer.complete_next.assert_called_once()
