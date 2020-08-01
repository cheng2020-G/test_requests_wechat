from api.dept import Dept
from api.get_token import GetToken


class TestBase:

    def setup(self):
        self.gettoken = GetToken()
        self.dept = Dept()
