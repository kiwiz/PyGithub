############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Balázs Rostás <rostas.balazs@gmail.com>                       #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2018 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2018 Bruce Richardson <itsbruce@workshy.org>                       #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Riccardo Pittau <elfosardo@users.noreply.github.com>          #
# Copyright 2018 Shubham Singh <41840111+singh811@users.noreply.github.com>    #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Surya Teja <94suryateja@gmail.com>                            #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Anuj Bansal <bansalanuj1996@gmail.com>                        #
# Copyright 2020 Glenn McDonald <testworksau@users.noreply.github.com>         #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 MeggyCal <MeggyCal@users.noreply.github.com>                  #
# Copyright 2021 秋葉 <ambiguous404@gmail.com>                                   #
# Copyright 2022 KimSia Sim <245021+simkimsia@users.noreply.github.com>        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Chris Wells <ping@cwlls.com>                                  #
# Copyright 2024 Eduardo Ramírez <edu.rh90@gmail.com>                          #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Oskar Jansson <56458534+janssonoskar@users.noreply.github.com>#
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from datetime import datetime, timezone

import github

from . import Framework


class AuthenticatedUser(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.user = self.g.get_user()

    def testAttributes(self):
        self.assertEqual(
            self.user.avatar_url,
            "https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png",
        )
        self.assertEqual(self.user.bio, "")
        self.assertEqual(self.user.blog, "http://vincent-jacques.net")
        self.assertEqual(self.user.collaborators, 0)
        self.assertEqual(self.user.company, "Criteo")
        self.assertEqual(
            self.user.created_at,
            datetime(2010, 7, 9, 6, 10, 6, tzinfo=timezone.utc),
        )
        self.assertEqual(self.user.disk_usage, 16692)
        self.assertEqual(self.user.email, "vincent@vincent-jacques.net")
        self.assertEqual(self.user.followers, 13)
        self.assertEqual(self.user.following, 24)
        self.assertEqual(self.user.gravatar_id, "b68de5ae38616c296fa345d2b9df2225")
        self.assertFalse(self.user.hireable)
        self.assertEqual(self.user.html_url, "https://github.com/jacquev6")
        self.assertEqual(self.user.id, 327146)
        self.assertEqual(self.user.location, "Paris, France")
        self.assertEqual(self.user.login, "jacquev6")
        self.assertEqual(self.user.name, "Vincent Jacques")
        self.assertEqual(self.user.owned_private_repos, 5)
        self.assertEqual(self.user.plan.name, "micro")
        self.assertEqual(self.user.plan.collaborators, 1)
        self.assertEqual(self.user.plan.space, 614400)
        self.assertEqual(self.user.plan.private_repos, 5)
        self.assertEqual(self.user.private_gists, 5)
        self.assertEqual(self.user.public_gists, 1)
        self.assertEqual(self.user.public_repos, 10)
        self.assertEqual(self.user.total_private_repos, 5)
        self.assertEqual(self.user.type, "User")
        self.assertEqual(self.user.url, "https://api.github.com/users/jacquev6")
        self.assertEqual(self.user.node_id, "MDQ6VXNlcjMyNzE0Ng==")
        self.assertEqual(repr(self.user), 'AuthenticatedUser(login="jacquev6")')
        self.assertTrue(self.user.two_factor_authentication)

    def testEditWithoutArguments(self):
        self.user.edit()

    def testEditWithAllArguments(self):
        self.user.edit(
            "Name edited by PyGithub",
            "Email edited by PyGithub",
            "Blog edited by PyGithub",
            "Company edited by PyGithub",
            "Location edited by PyGithub",
            True,
            "Bio edited by PyGithub",
        )
        self.assertEqual(self.user.name, "Name edited by PyGithub")
        self.assertEqual(self.user.email, "Email edited by PyGithub")
        self.assertEqual(self.user.blog, "Blog edited by PyGithub")
        self.assertEqual(self.user.company, "Company edited by PyGithub")
        self.assertEqual(self.user.location, "Location edited by PyGithub")
        self.assertTrue(self.user.hireable)
        self.assertEqual(self.user.bio, "Bio edited by PyGithub")

    def testEmails(self):
        emails = self.user.get_emails()
        self.assertEqual(
            [item.email for item in emails],
            ["vincent@vincent-jacques.net", "github.com@vincent-jacques.net"],
        )
        self.assertTrue(emails[0].primary)
        self.assertTrue(emails[0].verified)
        self.assertEqual(emails[0].visibility, "private")
        self.user.add_to_emails("1@foobar.com", "2@foobar.com")
        self.assertEqual(
            [item.email for item in self.user.get_emails()],
            [
                "vincent@vincent-jacques.net",
                "1@foobar.com",
                "2@foobar.com",
                "github.com@vincent-jacques.net",
            ],
        )
        self.user.remove_from_emails("1@foobar.com", "2@foobar.com")
        self.assertEqual(
            [item.email for item in self.user.get_emails()],
            ["vincent@vincent-jacques.net", "github.com@vincent-jacques.net"],
        )

    def testFollowing(self):
        nvie = self.g.get_user("nvie")
        self.assertListKeyEqual(
            self.user.get_following(),
            lambda u: u.login,
            [
                "schacon",
                "jamis",
                "chad",
                "unclebob",
                "dabrahams",
                "jnorthrup",
                "brugidou",
                "regisb",
                "walidk",
                "tanzilli",
                "fjardon",
                "r3c",
                "sdanzan",
                "vineus",
                "cjuniet",
                "gturri",
                "ant9000",
                "asquini",
                "claudyus",
                "jardon-u",
                "s-bernard",
                "kamaradclimber",
                "Lyloa",
                "nvie",
            ],
        )
        self.assertTrue(self.user.has_in_following(nvie))
        self.user.remove_from_following(nvie)
        self.assertFalse(self.user.has_in_following(nvie))
        self.user.add_to_following(nvie)
        self.assertTrue(self.user.has_in_following(nvie))
        self.assertListKeyEqual(
            self.user.get_followers(),
            lambda u: u.login,
            [
                "jnorthrup",
                "brugidou",
                "regisb",
                "walidk",
                "afzalkhan",
                "sdanzan",
                "vineus",
                "gturri",
                "fjardon",
                "cjuniet",
                "jardon-u",
                "kamaradclimber",
                "L42y",
            ],
        )

    def testWatching(self):
        gitflow = self.g.get_user("nvie").get_repo("gitflow")
        self.assertListKeyEqual(
            self.user.get_watched(),
            lambda r: r.name,
            [
                "git",
                "boost.php",
                "capistrano",
                "boost.perl",
                "git-subtree",
                "git-hg",
                "homebrew",
                "celtic_knot",
                "twisted-intro",
                "markup",
                "hub",
                "gitflow",
                "murder",
                "boto",
                "agit",
                "d3",
                "pygit2",
                "git-pulls",
                "django_mathlatex",
                "scrumblr",
                "developer.github.com",
                "python-github3",
                "PlantUML",
                "bootstrap",
                "drawnby",
                "django-socketio",
                "django-realtime",
                "playground",
                "BozoCrack",
                "FatherBeaver",
                "PyGithub",
                "django",
                "django",
                "TestPyGithub",
            ],
        )
        self.assertTrue(self.user.has_in_watched(gitflow))
        self.user.remove_from_watched(gitflow)
        self.assertFalse(self.user.has_in_watched(gitflow))
        self.user.add_to_watched(gitflow)
        self.assertTrue(self.user.has_in_watched(gitflow))

    def testStarring(self):
        gitflow = self.g.get_user("nvie").get_repo("gitflow")
        self.assertListKeyEqual(
            self.user.get_starred(),
            lambda r: r.name,
            [
                "git",
                "boost.php",
                "capistrano",
                "boost.perl",
                "git-subtree",
                "git-hg",
                "homebrew",
                "celtic_knot",
                "twisted-intro",
                "markup",
                "hub",
                "gitflow",
                "murder",
                "boto",
                "agit",
                "d3",
                "pygit2",
                "git-pulls",
                "django_mathlatex",
                "scrumblr",
                "developer.github.com",
                "python-github3",
                "PlantUML",
                "bootstrap",
                "drawnby",
                "django-socketio",
                "django-realtime",
                "playground",
                "BozoCrack",
                "FatherBeaver",
                "amaunet",
                "django",
                "django",
                "moviePlanning",
                "folly",
            ],
        )
        self.assertTrue(self.user.has_in_starred(gitflow))
        self.user.remove_from_starred(gitflow)
        self.assertFalse(self.user.has_in_starred(gitflow))
        self.user.add_to_starred(gitflow)
        self.assertTrue(self.user.has_in_starred(gitflow))

    def testSubscriptions(self):
        gitflow = self.g.get_user("nvie").get_repo("gitflow")
        self.assertListKeyEqual(
            self.user.get_subscriptions(),
            lambda r: r.name,
            [
                "gitflow",
                "ViDE",
                "Boost.HierarchicalEnum",
                "QuadProgMm",
                "DrawSyntax",
                "DrawTurksHead",
                "PrivateStuff",
                "vincent-jacques.net",
                "Hacking",
                "C4Planner",
                "developer.github.com",
                "PyGithub",
                "PyGithub",
                "django",
                "CinePlanning",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "IpMap",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
            ],
        )
        self.assertTrue(self.user.has_in_subscriptions(gitflow))
        self.user.remove_from_subscriptions(gitflow)
        self.assertFalse(self.user.has_in_subscriptions(gitflow))
        self.user.add_to_subscriptions(gitflow)
        self.assertTrue(self.user.has_in_subscriptions(gitflow))

    def testGetAuthorizations(self):
        self.assertListKeyEqual(self.user.get_authorizations(), lambda a: a.id, [372294])

    def testCreateRepository(self):
        repo = self.user.create_repo(name="TestPyGithub")
        self.assertEqual(repo.url, "https://api.github.com/repos/jacquev6/TestPyGithub")

    def testCreateProject(self):
        project = self.user.create_project(name="TestPyGithub", body="This is the body")
        self.assertEqual(project.url, "https://api.github.com/projects/4084610")

    def testCreateRepositoryWithAllArguments(self):
        repo = self.user.create_repo(
            name="TestPyGithub",
            description="Repo created by PyGithub",
            homepage="http://foobar.com",
            private=False,
            has_issues=False,
            has_projects=False,
            has_wiki=False,
            has_discussions=False,
            has_downloads=False,
            allow_squash_merge=False,
            allow_merge_commit=False,
            allow_rebase_merge=True,
            delete_branch_on_merge=False,
        )
        self.assertEqual(repo.url, "https://api.github.com/repos/jacquev6/TestPyGithub")

    def testCreateRepositoryWithAutoInit(self):
        repo = self.user.create_repo(name="TestPyGithub", auto_init=True, gitignore_template="Python")
        self.assertEqual(repo.url, "https://api.github.com/repos/jacquev6/TestPyGithub")

    def testCreateAuthorizationWithoutArguments(self):
        authorization = self.user.create_authorization()
        self.assertEqual(authorization.id, 372259)

    def testCreateAuthorizationWithAllArguments(self):
        authorization = self.user.create_authorization(
            ["repo"], "Note created by PyGithub", "http://vincent-jacques.net/PyGithub"
        )
        self.assertEqual(authorization.id, 372294)

    def testCreateAuthorizationWithClientIdAndSecret(self):
        # I don't have a client_id and client_secret so the ReplayData for this test is forged
        authorization = self.user.create_authorization(
            client_id="01234567890123456789",
            client_secret="0123456789012345678901234567890123456789",
        )
        self.assertEqual(authorization.id, 372294)

    def testCreateGist(self):
        gist = self.user.create_gist(
            True,
            {"foobar.txt": github.InputFileContent("File created by PyGithub")},
            "Gist created by PyGithub",
        )
        self.assertEqual(gist.description, "Gist created by PyGithub")
        self.assertEqual(list(gist.files.keys()), ["foobar.txt"])
        self.assertEqual(gist.files["foobar.txt"].content, "File created by PyGithub")

    def testCreateGistWithoutDescription(self):
        gist = self.user.create_gist(True, {"foobar.txt": github.InputFileContent("File created by PyGithub")})
        self.assertEqual(gist.description, None)
        self.assertEqual(list(gist.files.keys()), ["foobar.txt"])
        self.assertEqual(gist.files["foobar.txt"].content, "File created by PyGithub")

    def testCreateKey(self):
        key = self.user.create_key(
            "Key added through PyGithub",
            "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA2Mm0RjTNAYFfSCtUpO54usdseroUSIYg5KX4JoseTpqyiB/hqewjYLAdUq/tNIQzrkoEJWSyZrQt0ma7/YCyMYuNGd3DU6q6ZAyBeY3E9RyCiKjO3aTL2VKQGFvBVVmGdxGVSCITRphAcsKc/PF35/fg9XP9S0anMXcEFtdfMHz41SSw+XtE+Vc+6cX9FuI5qUfLGbkv8L1v3g4uw9VXlzq4GfTA+1S7D6mcoGHopAIXFlVr+2RfDKdSURMcB22z41fljO1MW4+zUS/4FyUTpL991es5fcwKXYoiE+x06VJeJJ1Krwx+DZj45uweV6cHXt2JwJEI9fWB6WyBlDejWw== vincent@IDEE",
        )
        self.assertEqual(key.id, 2626650)

    def testGetEvents(self):
        self.assertListKeyBegin(
            self.user.get_events(),
            lambda e: e.type,
            ["PushEvent", "IssuesEvent", "IssueCommentEvent", "PushEvent"],
        )

    def testGetOrganizationEvents(self):
        self.assertListKeyBegin(
            self.user.get_organization_events(self.g.get_organization("BeaverSoftware")),
            lambda e: e.type,
            ["CreateEvent", "CreateEvent", "PushEvent", "PushEvent"],
        )

    def testGetGists(self):
        self.assertListKeyEqual(
            self.user.get_gists(),
            lambda g: g.id,
            [
                "2793505",
                "2793179",
                "11cb445f8197e17d303d",
                "1942384",
                "dcb7de17e8a52b74541d",
            ],
        )
        self.assertListKeyEqual(
            self.user.get_gists(since=datetime(2012, 3, 1, 23, 0, 0)),
            lambda g: g.id,
            ["2793505", "2793179", "11cb445f8197e17d303d"],
        )

    def testGetStarredGists(self):
        self.assertListKeyEqual(
            self.user.get_starred_gists(),
            lambda g: g.id,
            ["1942384", "dcb7de17e8a52b74541d"],
        )

    def testGetIssues(self):
        self.assertListKeyEqual(
            self.user.get_issues(),
            lambda i: (i.id, i.repository.name),
            [
                (4639931, "PyGithub"),
                (4452000, "PyGithub"),
                (4356743, "PyGithub"),
                (3716033, "PyGithub"),
                (3715946, "PyGithub"),
                (3643837, "PyGithub"),
                (3628022, "PyGithub"),
                (3624595, "PyGithub"),
                (3624570, "PyGithub"),
                (3624561, "PyGithub"),
                (3624556, "PyGithub"),
                (3619973, "PyGithub"),
                (3527266, "PyGithub"),
                (3527245, "PyGithub"),
                (3527231, "PyGithub"),
            ],
        )

    def testGetIssuesWithAllArguments(self):
        requestedByUser = self.user.get_repo("PyGithub").get_label("Requested by user")
        issues = self.user.get_issues(
            "assigned",
            "closed",
            [requestedByUser],
            "comments",
            "asc",
            datetime(2012, 5, 28, 23, 0, 0),
        )
        self.assertListKeyEqual(
            issues,
            lambda i: i.id,
            [
                6816576,
                8495415,
                6889934,
                8339699,
                8075253,
                8033963,
                9089893,
                9489725,
                11746141,
                5152384,
                5177381,
                5783131,
                6454054,
                6641076,
                6653907,
                7331214,
                9489813,
                9776615,
                10360280,
                4356743,
                6583381,
                6751469,
                8189836,
                10758585,
                12097154,
                12867103,
                5191621,
                5256315,
                6363719,
                9209408,
                6912733,
                9948505,
                11503771,
                10922412,
                11844658,
                12566144,
                6353712,
                9323084,
                10379143,
                5387373,
                12179668,
                6911794,
                11731917,
                6807542,
                6780606,
            ],
        )

    def testGetUserIssues(self):
        self.assertListKeyEqual(
            self.user.get_user_issues(),
            lambda i: i.id,
            [
                14447880,
                13505356,
                12541184,
                10586808,
                6741461,
                6741457,
                6727331,
                5641572,
            ],
        )

    def testGetUserIssuesWithAllArguments(self):
        requestedByUser = self.user.get_repo("PyGithub").get_label("Requested by user")
        issues = self.user.get_user_issues(
            "assigned",
            "closed",
            [requestedByUser],
            "comments",
            "asc",
            datetime(2012, 5, 28, 23, 0, 0),
        )
        self.assertListKeyEqual(
            issues,
            lambda i: i.id,
            [
                6816576,
                8495415,
                6889934,
                8339699,
                8075253,
                8033963,
                9089893,
                9489725,
                11746141,
                5152384,
                5177381,
                5783131,
                6454054,
                6641076,
                6653907,
                7331214,
                9489813,
                9776615,
                10360280,
                4356743,
                6583381,
                6751469,
                8189836,
                10758585,
                12097154,
                12867103,
                5191621,
                5256315,
                6363719,
                9209408,
                6912733,
                9948505,
                11503771,
                10922412,
                11844658,
                12566144,
                6353712,
                9323084,
                10379143,
                5387373,
                12179668,
                6911794,
                11731917,
                6807542,
                6780606,
            ],
        )

    def testGetKeys(self):
        self.assertListKeyEqual(
            self.user.get_keys(),
            lambda k: k.title,
            ["vincent@home", "vincent@gandi", "vincent@aws", "vincent@macbook"],
        )

    def testGetOrgs(self):
        self.assertListKeyEqual(self.user.get_orgs(), lambda o: o.login, ["BeaverSoftware"])

    def testGetRepos(self):
        self.assertListKeyEqual(
            self.user.get_repos(),
            lambda r: r.name,
            [
                "TestPyGithub",
                "django",
                "PyGithub",
                "developer.github.com",
                "acme-public-website",
                "C4Planner",
                "Hacking",
                "vincent-jacques.net",
                "Contests",
                "Candidates",
                "Tests",
                "DrawTurksHead",
                "DrawSyntax",
                "QuadProgMm",
                "Boost.HierarchicalEnum",
                "ViDE",
            ],
        )

    def testGetReposWithArguments(self):
        self.assertListKeyEqual(
            self.user.get_repos("all", "owner", "public", "full_name", "desc"),
            lambda r: r.name,
            [
                "ViDE",
                "QuadProgMm",
                "PyGithub",
                "DrawTurksHead",
                "DrawSyntax",
                "django",
                "developer.github.com",
                "C4Planner",
                "Boost.HierarchicalEnum",
                "acme-public-website",
            ],
        )

    def testCreateFork(self):
        repo = self.user.create_fork(self.g.get_user("nvie").get_repo("gitflow"))
        self.assertEqual(repo.source.full_name, "nvie/gitflow")

    def testCreateRepoFromTemplate(self):
        template_repo = self.g.get_repo("actions/hello-world-docker-action")

        repo = self.user.create_repo_from_template("hello-world-docker-action-new", template_repo)
        self.assertEqual(
            repo.url,
            "https://api.github.com/repos/jacquev6/hello-world-docker-action-new",
        )
        self.assertFalse(repo.is_template)

    def testCreateRepoFromTemplateWithAllArguments(self):
        template_repo = self.g.get_repo("actions/hello-world-docker-action")

        description = "My repo from template"
        private = True
        repo = self.user.create_repo_from_template(
            "hello-world-docker-action-new",
            template_repo,
            description=description,
            include_all_branches=True,
            private=private,
        )
        self.assertEqual(repo.description, description)
        self.assertTrue(repo.private)

    def testGetNotification(self):
        notification = self.user.get_notification("8406712")
        self.assertEqual(notification.id, "8406712")
        self.assertEqual(notification.unread, False)
        self.assertEqual(notification.reason, "author")
        self.assertEqual(notification.subject.title, "Feature/coveralls")
        self.assertEqual(notification.subject.type, "PullRequest")
        self.assertEqual(notification.repository.id, 8432784)
        self.assertEqual(
            notification.updated_at,
            datetime(2013, 3, 15, 5, 43, 11, tzinfo=timezone.utc),
        )
        self.assertEqual(notification.url, None)
        self.assertEqual(notification.subject.url, None)
        self.assertEqual(notification.subject.latest_comment_url, None)
        self.assertEqual(
            repr(notification),
            'Notification(subject=NotificationSubject(title="Feature/coveralls"), id="8406712")',
        )
        self.assertEqual(repr(notification.subject), 'NotificationSubject(title="Feature/coveralls")')

    def testGetNotifications(self):
        self.assertListKeyEqual(self.user.get_notifications(participating=True), lambda n: n.id, ["8406712"])

    def testGetNotificationsWithOtherArguments(self):
        self.assertListKeyEqual(self.user.get_notifications(all=True), lambda n: n.id, [])

    def testMarkNotificationsAsRead(self):
        self.user.mark_notifications_as_read(datetime(2018, 10, 18, 18, 20, 0o1, 0))

    def testGetTeams(self):
        self.assertListKeyEqual(
            self.user.get_teams(),
            lambda t: t.name,
            [
                "Owners",
                "Honoraries",
                "Honoraries",
                "Honoraries",
                "Honoraries",
                "Honoraries",
                "Honoraries",
                "Honoraries",
                "Honoraries",
                "Honoraries",
            ],
        )

    def testAcceptInvitation(self):
        self.assertEqual(self.user.accept_invitation(4294886), None)

    def testGetInvitations(self):
        invitation = self.user.get_invitations()[0]
        self.assertEqual(repr(invitation), "Invitation(id=17285388)")
        self.assertEqual(invitation.id, 17285388)
        self.assertEqual(invitation.permissions, "write")
        created_at = datetime(2019, 6, 27, 11, 47, tzinfo=timezone.utc)
        self.assertEqual(invitation.created_at, created_at)
        self.assertEqual(invitation.expired, True)
        self.assertEqual(
            invitation.url,
            "https://api.github.com/user/repository_invitations/17285388",
        )
        self.assertEqual(invitation.html_url, "https://github.com/jacquev6/PyGithub/invitations")
        self.assertEqual(invitation.node_id, "MDIwOlJlcG9zaXRvcnlJbnZpdGF0aW9uMTcyODUzODg=")
        self.assertEqual(invitation.repository.name, "PyGithub")
        self.assertEqual(invitation.invitee.login, "foobar-test1")
        self.assertEqual(invitation.inviter.login, "jacquev6")

    def testCreateMigration(self):
        self.assertTrue(isinstance(self.user.create_migration(["sample-repo"]), github.Migration.Migration))

    def testGetMigrations(self):
        self.assertEqual(self.user.get_migrations().totalCount, 46)

    def testInstallations(self):
        installations = self.user.get_installations()
        self.assertEqual(installations[0].id, 123456)
        self.assertEqual(installations[0].app_id, 10101)
        self.assertEqual(installations[0].target_id, 3344556)
        self.assertEqual(installations[0].target_type, "User")
        self.assertEqual(installations.totalCount, 1)

    def testGetMemberships(self):
        membership_data = self.user.get_organization_memberships()
        self.assertListKeyEqual(
            membership_data,
            lambda e: e.organization.login,
            ["aneyem-github", "nko4", "geoservel", "iic2154-uc-cl", "nnodes", "sushiclm"],
        )
        self.assertListKeyEqual(
            membership_data, lambda e: e.role, ["member", "member", "admin", "member", "member", "admin"]
        )
