# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

haxor-news is a command-line tool that brings Hacker News to the terminal, allowing users to view, filter, and browse posts, comments, and web content without leaving the command line.

**Supported Python versions**: 3.10, 3.11, 3.12, 3.13

## Development Setup

**Important**: This project uses a virtual environment in `.venv`. Always activate it before running tests or development commands:

```bash
# Activate virtual environment (required before any dev work)
source .venv/bin/activate

# Install in development mode with test and dev dependencies
pip install -e '.[test,dev]'

# Or using uv (faster)
uv venv --python 3.13 .venv
source .venv/bin/activate
uv pip install -e '.[test,dev]'
```

## Testing

```bash
# Run all tests with coverage
pytest

# Run specific test file
pytest tests/test_hacker_news.py

# Run tests with verbose output
pytest -vv

# Legacy test runner (still supported)
python tests/run_tests.py
```

## Code Quality Tools

All tools configured in `pyproject.toml`:

```bash
# Format code with Ruff
ruff format .

# Check formatting without changes
ruff format --check .

# Lint with Ruff
ruff check .

# Auto-fix issues
ruff check --fix .

# Type check with MyPy
mypy -m haxor_news
```

**Important**: The `haxor_news/lib/haxor/` directory contains third-party code and is excluded from Ruff and MyPy checks.

## Before Committing

**MUST RUN** before committing any changes:

```bash
# Activate virtual environment first
source .venv/bin/activate

# Run all regression tests
pytest

# Format code
ruff format .

# Check linting
ruff check .

# Type check
mypy -m haxor_news
```

All checks must pass before committing. If any check fails, fix the issues and re-run.

## Building

```bash
# Build distribution packages
python -m build

# Output: dist/haxor_news-*.tar.gz and dist/haxor_news-*.whl
```

## Architecture

### Two Entry Points

1. **`haxor-news`** (`main.py`): Interactive REPL mode with auto-completion
   - Uses prompt-toolkit 3.x for rich terminal interaction
   - Features: history, auto-suggest, key bindings (F10, Ctrl+Space)
   - Pagination support via `less` (Unix) or `more` (Windows)

2. **`hn`** (`main_cli.py`): Direct command-line interface
   - Click-based CLI for one-off commands
   - Example: `hn top 20`, `hn view 1 -c`

### Core Components

**`Haxor` class** (`haxor.py`): REPL orchestrator
- Creates `PromptSession` with custom completer, key bindings, and toolbar
- Manages pagination by injecting `| less -r` or `| more` into commands
- Handles command execution via subprocess.call()

**`HackerNewsCli` class** (`hacker_news_cli.py`): Click command definitions
- Defines all CLI commands: `top`, `best`, `ask`, `show`, `new`, `jobs`, `view`, `hiring`, `freelance`, `user`, `onion`
- Uses Click decorators for argument parsing and validation
- Passes `HackerNews` context object to all commands

**`HackerNews` class** (`hacker_news.py`): Business logic layer
- Fetches data from Hacker News API (via `lib/haxor/haxor.py`)
- Formats and prints items, comments, user info
- Handles comment filtering (unseen, recent, regex)
- Manages web content viewing via `WebViewer`

**`Config` class** (`config.py`): User configuration
- Reads/writes `~/.haxornewsconfig` (or `%userprofile%\.haxornewsconfig` on Windows)
- Stores color preferences, item IDs, freelance/hiring post IDs
- INI-based format using configparser

**`Completer` class** (`completer.py`): Auto-completion
- Provides context-aware completions for commands, options, and arguments
- Fuzzy matching support (optional)
- Integrated with prompt-toolkit 3.x completion API

**`KeyManager` class** (`keys.py`): Keyboard shortcuts
- F10: Exit
- Ctrl+Space: Toggle completion menu
- F2: Toggle comment pagination (currently disabled)

### Third-Party Code

**`lib/haxor/`**: Embedded Hacker News API client (external library)
- Excluded from formatting/linting (see pyproject.toml)
- Handles HTTP requests to official Hacker News API
- Defines API models: Item, User, etc.

**`lib/pretty_date_time.py`**: Date formatting utility
**`lib/debug_timer.py`**: Performance timing decorator

### Comment Filtering Architecture

The `HackerNews` class supports multiple comment filtering modes:

1. **Unseen comments** (`-cu`): Marks new comments with `[!]`, collapses seen ones
2. **Recent comments** (`-cr`): Shows comments from last 60 minutes
3. **Regex query** (`-cq`): Filters comments matching regex pattern
4. **Hide mode** (`-ch`): Hides non-matching comments instead of collapsing them

Filtering happens in `_print_comments()` method using recursive traversal of the comment tree.

## Configuration Files

- **`pyproject.toml`**: Modern Python packaging (PEP 517/518/621)
  - All tool configs: pytest, black, ruff, mypy, coverage
  - Dynamic versioning from `haxor_news.__version__`
  - Optional dependencies: `[test]`, `[dev]`

- **`~/.haxornewsconfig`**: User preferences
  - Color scheme customization
  - Cached item indices for quick access
  - Latest hiring/freelance post IDs

## CI/CD

GitHub Actions workflows (`.github/workflows/`):

- **test.yml**: Runs on push/PR
  - Matrix: Ubuntu/macOS × Python 3.10/3.13
  - Steps: pytest, black, mypy, ruff, build

- **publish.yml**: Triggered on GitHub releases
  - Runs tests before publishing
  - Uses trusted publishing to PyPI (OIDC)

## Platform Considerations

- **Windows**: Uses `more` instead of `less` for pagination
- **Linux/Mac**: Uses `less -r` for ANSI color support
- **History file**: `~/.haxornewshistory` stores command history

## Prompt-Toolkit 3.x Migration

This project recently migrated from prompt-toolkit 1.x to 3.x. Key changes:

- `CommandLineInterface` → `PromptSession`
- `KeyBindingManager` → `KeyBindings`
- Removed `AbortAction`, `AcceptAction` (use standard exceptions)
- `completer.get_completions()` now takes `complete_event` parameter
- Toolbar handler no longer receives `cli` parameter

When modifying REPL code, follow the prompt-toolkit 3.x API patterns in `haxor.py`.
