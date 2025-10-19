![](http://i.imgur.com/C4mkc3L.gif)

[![Build Status](https://travis-ci.org/donnemartin/haxor-news.svg?branch=master)](https://travis-ci.org/donnemartin/haxor-news) [![Dependency Status](https://gemnasium.com/donnemartin/haxor-news.svg)](https://gemnasium.com/donnemartin/haxor-news)

[![PyPI version](https://badge.fury.io/py/haxor-news.svg)](http://badge.fury.io/py/haxor-news) [![PyPI](https://img.shields.io/pypi/pyversions/haxor-news.svg)](https://pypi.python.org/pypi/haxor-news/) [![License](http://img.shields.io/:license-apache-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)

haxor-news
==========

To view the latest `README`, `docs`, and `code` visit the GitHub repo:

https://github.com/donnemartin/haxor-news

To submit bugs or feature requests, visit the issue tracker:

https://github.com/donnemartin/haxor-news/issues

Changelog
=========

0.5.0 (2025-10-19)
------------------

### BREAKING CHANGES

* Dropped support for Python 2.x and Python 3.9 and earlier
* Minimum required Python version is now 3.10

### Features

* Add support for Python 3.10, 3.11, 3.12, and 3.13

### Updates

* Upgrade prompt-toolkit from 1.x to 3.x (major rewrite of REPL interface)
* Upgrade click from 5.x/7.x to 8.x
* Upgrade all dependencies to latest stable versions:
  - colorama >= 0.4.6
  - requests >= 2.31.0
  - pygments >= 2.17.0
* Remove `six` dependency
* Remove all `__future__` imports
* Modernize codebase for Python 3 only
* Update test suite for Python 3.13 and new dependency APIs

### Technical Details

* Migrate from `CommandLineInterface` to `PromptSession` (prompt-toolkit 3.x)
* Rewrite key bindings using new `KeyBindings` API
* Update completer for prompt-toolkit 3.x  API changes
* Simplify toolbar to return plain strings instead of Token tuples
* Update style handling for prompt-toolkit 3.x compatibility
* Fix all tests for prompt-toolkit 3.x and click 8.x

0.4.2 (2017-04-08)
------------------

### Bug Fixes

* [#94](https://github.com/donnemartin/haxor-news/pull/94) - Update to `prompt-toolkit` 1.0.0, which includes a number of performance improvements (especially noticeable on Windows) and bug fixes.

0.4.1 (2016-05-30)
------------------

### Bug Fixes

* [#62](https://github.com/donnemartin/haxor-news/pull/62) - Fix `prompt-toolkit` v1.0.0 hanging while autocompleting the hn view command.  Revert back to `prompt-toolkit` v0.52.  This bug only happens on Windows.

0.4.0 (2016-05-30)
------------------

### Features

* [#52](https://github.com/donnemartin/haxor-news/issues/52) - Add `exit` and `quit` commands, which can be used instead of `ctrl-d`.
* [#53](https://github.com/donnemartin/haxor-news/issues/53) - Allow clicking of urls in some terminals to open in a browser.

### Bug Fixes

* [#36](https://github.com/donnemartin/haxor-news/issues/36) - Fix crash caused by Unicode comments on Windows.
* [#59](https://github.com/donnemartin/haxor-news/pull/59) - Update to `prompt-toolkit` 1.0.0, which includes a number of performance improvements (especially noticeable on Windows) and bug fixes.
* Fix some comments and docstrings.

### Updates

* [#48](https://github.com/donnemartin/haxor-news/issues/48), [#50](https://github.com/donnemartin/haxor-news/issues/50) - Update latest monthly hiring post ids.
* [#56](https://github.com/donnemartin/haxor-news/issues/48) - Update packaging dependencies based on semantic versioning.
* Fix `Config` docstrings.
* Update `README`:
    * Update intro
    * Add Hacker News discussion of `haxor-news`
    * Update comments discussion and examples
    * Update TODO
    * Fix urls based on redirects
    * Remove buggy Codecov graph
    * Add note about OS X 10.11 pip installation issue
* Add Gemnasium dependencies management.
* Update links in `CONTRIBUTING`.

0.3.1 (2016-04-10)
------------------

- Initial release.
