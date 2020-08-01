from base.testbase import Base


class TestGetToken(Base):

    def test_get_token(self):
        r = self.gettoken.get_token()
        print(r)
