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


import os
from unittest import mock

from haxor_news.hacker_news import HackerNews
from haxor_news.settings import freelancer_post_id, who_is_hiring_post_id
from tests.compat import unittest
from tests.mock_hacker_news_api import MockHackerNewsApi


class ConfigTestIntegration(unittest.TestCase):
    def setUp(self):
        self.hn = HackerNews()
        self.hn.hacker_news_api = MockHackerNewsApi()
        self.limit = len(self.hn.hacker_news_api.items)

    @mock.patch("haxor_news.config.urlretrieve")
    def test_load_hiring_and_freelance_ids(self, mock_urlretrieve):
        # Mock the network request to return different IDs
        test_hiring_id = "99999999"
        test_freelance_id = "88888888"

        def fake_urlretrieve(url, filename):
            # Write test IDs to the downloaded settings file
            with open(filename, "w") as f:
                f.write(f"who_is_hiring_post_id = {test_hiring_id}\n")
                f.write(f"freelancer_post_id = {test_freelance_id}\n")

        mock_urlretrieve.side_effect = fake_urlretrieve

        self.hn.config.load_hiring_and_freelance_ids()
        # Config stores IDs as strings after loading from file
        assert self.hn.config.hiring_id == test_hiring_id
        assert self.hn.config.freelance_id == test_freelance_id
        # Verify they are different from defaults (as strings)
        assert self.hn.config.hiring_id != str(who_is_hiring_post_id)
        assert self.hn.config.freelance_id != str(freelancer_post_id)

        # Clean up
        try:
            os.remove("./downloaded_settings.py")
        except FileNotFoundError:
            pass

    def test_load_hiring_and_freelance_ids_invalid_url(self):
        self.hn.config.load_hiring_and_freelance_ids(url="https://example.com")
        assert self.hn.config.hiring_id == who_is_hiring_post_id
        assert self.hn.config.freelance_id == freelancer_post_id
        try:
            os.remove("./downloaded_settings.py")
        except FileNotFoundError:
            pass

    def test_load_hiring_and_freelance_ids_from_cache_or_defaults(self):
        self.hn.config.load_hiring_and_freelance_ids_from_cache_or_defaults()
        assert self.hn.config.hiring_id == who_is_hiring_post_id
        assert self.hn.config.freelance_id == freelancer_post_id
