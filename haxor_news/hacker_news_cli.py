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


import click

from .hacker_news import HackerNews

pass_hacker_news = click.make_pass_decorator(HackerNews)


class HackerNewsCli:
    """Encapsulate the Hacker News Command Line Interface."""

    @click.group()
    @click.pass_context
    def cli(ctx):
        """Browse Hacker News from the command line."""
        # Create a HackerNews object and remember it as the context object.
        # From this point onwards other commands can refer to it by using the
        # @pass_hacker_news decorator.
        ctx.obj = HackerNews()

    @cli.command()
    @click.argument("limit", required=False, default=10)
    @pass_hacker_news
    def ask(hacker_news: HackerNews, limit: int) -> None:
        """
        Display Ask HN posts.

        Examples:

        \b
            hn ask
            hn ask 5
        """
        hacker_news.ask(limit)

    @cli.command()
    @click.argument("limit", required=False, default=10)
    @pass_hacker_news
    def best(hacker_news: HackerNews, limit: int) -> None:
        """
        Display the best posts of the past few days.

        Examples:

        \b
            hn best
            hn best 20
        """
        hacker_news.best(limit)

    @cli.command()
    @click.argument("regex_query", required=False)
    @click.option("-i", "--id_post", required=False, default=0)
    @pass_hacker_news
    def freelance(hacker_news: HackerNews, regex_query: str, id_post: int) -> None:
        """
        Display comments from the seeking freelancer posts.

        Searches the monthly Hacker News seeking freelancer post for comments
        matching the given regex_query. Defaults to searching the latest post.

        You can search any post by providing a freelancer_post_id:
            Example: https://news.ycombinator.com/item?id=10492087
            freelancer_post_id = 10492087

        Examples:

        \b
            hn freelance
            hn freelance "Python"
            hn freelance "(?i)Python|JavaScript"  # (?i) case insensitive
            hn freelance "(?i)Python" -i 8394339  # search post 8394339
            hn freelance "(?i)(Python|JavaScript).*(rockstar)" > rockstars.txt
        """
        if id_post == 0:
            hacker_news.config.load_hiring_and_freelance_ids()
            id_post = hacker_news.config.freelance_id
        hacker_news.hiring_and_freelance(regex_query, id_post)

    @cli.command()
    @click.argument("regex_query", required=False)
    @click.option("-i", "--id_post", required=False, default=0)
    @pass_hacker_news
    def hiring(hacker_news: HackerNews, regex_query: str, id_post: int) -> None:
        """
        Display comments from the who is hiring posts.

        Searches the monthly Hacker News who is hiring post for comments
        matching the given regex_query. Defaults to searching the latest post.

        You can search any post by providing a who_is_hiring_post_id:
            Example: https://news.ycombinator.com/item?id=10492086
            who_is_hiring_post_id = 10492086

        Examples:

        \b
            hn hiring
            hn hiring "Python"
            hn hiring "(?i)Python|JavaScript"  # (?i) case insensitive
            hn hiring "(?i)Python|JavaScript" -i 8394339  # search post 8394339
            hn hiring "(?i)(Python|JavaScript).*(rockstar)" > rockstars.txt
        """
        if id_post == 0:
            hacker_news.config.load_hiring_and_freelance_ids()
            id_post = hacker_news.config.hiring_id
        hacker_news.hiring_and_freelance(regex_query, id_post)

    @cli.command()
    @click.argument("limit", required=False, default=10)
    @pass_hacker_news
    def jobs(hacker_news: HackerNews, limit: int) -> None:
        """
        Display job posts.

        Examples:

        \b
            hn jobs
            hn jobs 15
        """
        hacker_news.jobs(limit)

    @cli.command()
    @click.argument("limit", required=False, default=10)
    @pass_hacker_news
    def new(hacker_news: HackerNews, limit: int) -> None:
        """
        Display the latest posts.

        Examples:

        \b
            hn new
            hn new 20
        """
        hacker_news.new(limit)

    @cli.command()
    @click.argument("limit", required=False, default=50)
    @pass_hacker_news
    def onion(hacker_news: HackerNews, limit: int) -> None:
        """
        Display onions.

        Examples:

        \b
            hn onion
            hn onion 10
        """
        hacker_news.onion(limit)

    @cli.command()
    @click.argument("limit", required=False, default=10)
    @pass_hacker_news
    def show(hacker_news: HackerNews, limit: int) -> None:
        """
        Display Show HN posts.

        Examples:

        \b
            hn show
            hn show 5
        """
        hacker_news.show(limit)

    @cli.command()
    @click.argument("limit", required=False, default=10)
    @pass_hacker_news
    def top(hacker_news: HackerNews, limit: int) -> None:
        """
        Display the top recent posts.

        Examples:

        \b
            hn top
            hn top 20
        """
        hacker_news.top(limit)

    @cli.command()
    @click.argument("user_id")
    @click.option("-l", "--limit", required=False, default=10)
    @pass_hacker_news
    def user(hacker_news: HackerNews, user_id: str, limit: int) -> None:
        """
        Display basic user info and submitted posts.

        Examples:

        \b
            hn user tptacek
            hn user patio11
        """
        hacker_news.user(user_id, limit)

    @cli.command()
    @click.argument("index")
    @click.option("-cq", "--comments_regex_query", required=False, default=None)
    @click.option("-c", "--comments", is_flag=True)
    @click.option("-cr", "--comments_recent", is_flag=True)
    @click.option("-cu", "--comments_unseen", is_flag=True)
    @click.option("-b", "--browser", is_flag=True)
    @click.option("-cc", "--clear_cache", is_flag=True)
    @click.option("-ch", "--comments_hide_non_matching", is_flag=True)
    @pass_hacker_news
    def view(
        hacker_news: HackerNews,
        index: str,
        comments_regex_query: str,
        comments: bool,
        comments_recent: bool,
        comments_unseen: bool,
        comments_hide_non_matching: bool,
        clear_cache: bool,
        browser: bool,
    ) -> None:
        """
        View a post by index or ID.

        The index can be either:
        1) A post index from a recent list (e.g., from 'hn top')
        2) An actual Hacker News post ID (values > 1000)

        Examples:

        \b
            hn top
            hn view 3
            hn view 3 -c | less
            hn view 3 -c > comments.txt
            hn view 3 -cr
            hn view 3 --comments_recent
            hn view 3 -cu
            hn view 3 --comments_unseen
            hn view 3 -cu -ch
            hn view 3 --comments_unseen --comments_hide_non_matching
            hn view 3 --browser
            hn view 3 -b -c
            hn view 3 -comments -clear_cache
            hn view 3 "(?i)case insensitive match" --comments
            hn view 3 "(?i)programmer" --comments
            hn view 3 "(?i)programmer" --comments | less
            hn view 10492086
            hn view 10492086 "Python"
            hn view 10492086 "(?i)case insensitive match"
            hn view 10492086 "(?i)(Python|Django)" > comments.txt
        """
        try:
            post_index = int(index)
        except ValueError:
            click.secho("Error: Expected an integer post index", fg="red")
        else:
            hacker_news.view_setup(
                post_index,
                comments_regex_query,
                comments,
                comments_recent,
                comments_unseen,
                comments_hide_non_matching,
                clear_cache,
                browser,
            )
