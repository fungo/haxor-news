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


import time

import click


def timeit(method):
    """From: https://www.andreas-jung.com/contents/a-python-decorator-for-measuring-the-execution-time-of-methods  # NOQA"""

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        message = f"{method.__name__!r} ({args!r}, {kw!r}) {te - ts:2.2f} sec"
        click.secho(message + "\n", fg="red")
        return result

    return timed
