from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_bootstrap_tour(self):
        self.open("https://xkcd.com/1117/")
        self.assert_element('img[alt="My Sky"]')
        self.create_bootstrap_tour()
        self.add_tour_step("Welcome to XKCD!")
        self.add_tour_step("This is the XKCD logo.", "#masthead img")
        self.add_tour_step("Here's the daily webcomic.", "#comic img")
        self.add_tour_step("This is the title.", "#ctitle", alignment="top")
        self.add_tour_step("Click here for the next comic.", 'a[rel="next"]')
        self.add_tour_step("Click here for the previous one.", 'a[rel="prev"]')
        self.add_tour_step("Learn about the author here.", 'a[rel="author"]')
        self.add_tour_step("Click for a random comic.", 'a[href*="/random/"]')
        self.add_tour_step("Thanks for taking this tour!")
        self.export_tour(filename="bootstrap_xkcd_tour.js")  # Exports the tour
        self.play_tour()  # Plays the tour

    @pytest.fixture
    def default_context(self):
        return {"extra_context": {}}

    @pytest.fixture(
        params=[
            {"author": "alice"},
            {"project_slug": "helloworld"},
            {"author": "bob", "project_slug": "foobar"},
        ]
    )
    def extra_context(request):
        return {"extra_context": request.param}

    @pytest.fixture(params=["default", "extra"])
    def context(request):
        if request.param == "default":
            return request.getfuncargvalue("default_context")
        else:
            return request.getfuncargvalue("extra_context")

    def test_generate_project(cookies, context):
        """Call the cookiecutter API to generate a new project from a
        template.
        """
        result = cookies.bake(extra_context=context)

        assert result.exit_code == 0
        assert result.exception is None
        assert result.project.isdir()

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            ("3+5", 8),
            pytest.param("1+7", 8, marks=pytest.mark.basic),
            pytest.param("2+4", 6, marks=pytest.mark.basic, id="basic_2+4"),
            pytest.param(
                "6*9", 42, marks=[pytest.mark.basic, pytest.mark.xfail], id="basic_6*9"
            ),
        ],
    )
    def test_eval(self, test_input, expected):
        assert eval(test_input) == expected

    # studying git branching & merging
    # chautran: git checkout v1.0.24
