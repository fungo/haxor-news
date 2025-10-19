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


import unittest

from haxor_news.haxor import Haxor
from haxor_news.toolbar import Toolbar


class ToolbarTest(unittest.TestCase):
    def setUp(self):
        self.haxor = Haxor()
        self.toolbar = Toolbar(lambda: self.haxor.paginate_comments)

    def test_toolbar_on(self):
        self.haxor.paginate_comments = True
        # In prompt-toolkit 3.x, toolbar returns a string
        expected = " [F10] Exit "
        assert expected == self.toolbar.handler()

    def test_toolbar_off(self):
        self.haxor.paginate_comments = False
        # In prompt-toolkit 3.x, toolbar returns a string
        expected = " [F10] Exit "
        assert expected == self.toolbar.handler()
