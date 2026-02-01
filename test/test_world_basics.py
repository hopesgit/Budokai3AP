from .bases import Budokai3TestBase


class TestWorldBasics(Budokai3TestBase):
    options = {
        "choose_du_characters": ["Goku"]
    }

    def test_can_reach_goal(self):
        items = ["Goku"]
        locations = ["Victory"]
        self.assertAccessDependency(locations, items)
