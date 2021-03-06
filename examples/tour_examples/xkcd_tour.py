from contextlib import contextmanager

import pytest
from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_create_tour(self):
        self.open("https://xkcd.com/1117/")
        self.assert_element('img[alt="My Sky"]')
        self.create_tour(theme="dark")
        self.add_tour_step("Welcome to XKCD!")
        self.add_tour_step("This is the XKCD logo.", "#masthead img")
        self.add_tour_step("Here's the daily webcomic.", "#comic img")
        self.add_tour_step("This is the title.", "#ctitle", alignment="top")
        self.add_tour_step("Click here for the next comic.", 'a[rel="next"]')
        self.add_tour_step("Click here for the previous one.", 'a[rel="prev"]')
        self.add_tour_step("Learn about the author here.", 'a[rel="author"]')
        self.add_tour_step("Click here for the license.", 'a[rel="license"]')
        self.add_tour_step("Click for a random comic.", 'a[href*="/random/"]')
        self.add_tour_step("Thanks for taking this tour!")
        self.export_tour(filename="xkcd_tour.js")  # Exports the tour
        self.play_tour()  # Plays the tour

    def test_setup_fails(self):
        pass

    def test_call_fails(self):
        assert 0

    def test_fail2(self):
        assert 0

    # Hi Chau, something wrong with this testcase; pls help to correct.
    # @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    # def test_eval(self, expected):
    #     assert eval(self) == expected

    """
    Hi American guy, I have fixed the code.
    --Chau
    """

    @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    def test_eval(self, test_input, expected):
        assert eval(test_input) == expected
        # self.assertEqual(a, b) -> unittest style

    # a map specifying multiple argument sets for a test method
    params = {
        "test_equals": [dict(a=1, b=2), dict(a=3, b=3)],
        "test_zerodivision": [dict(a=1, b=0)],
    }

    def test_equals(self, a, b):
        assert a == b

    def test_zerodivision(self, a, b):
        with pytest.raises(ZeroDivisionError):
            a / b

    # OK thanks Chau
    @pytest.fixture(
            params=[
                pytest.fixture_request("default_context"),
                pytest.fixture_request("extra_context"),
            ]
        )
    def context(request):
        """Returns all values for ``default_context``, one-by-one before it
        does the same for ``extra_context``.

        request.param:
            - {}
            - {'author': 'alice'}
            - {'project_slug': 'helloworld'}
            - {'author': 'bob', 'project_slug': 'foobar'}
        """
        return request.param

    # studying git branching & merging
    # chautran: git checkout v1.0.24
    # git pull origin v1.0.24

    @contextmanager
    def does_not_raise(self):
        yield

    @pytest.mark.parametrize(
        "example_input,expectation",
        [
            (3, does_not_raise()),
            (2, does_not_raise()),
            (1, does_not_raise()),
            (0, pytest.raises(ZeroDivisionError)),
        ],
    )
    def test_division(example_input, expectation):
        """Test how much I know division."""
        with expectation:
        assert (6 / example_input) is not None