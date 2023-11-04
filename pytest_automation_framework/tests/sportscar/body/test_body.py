from pytest import mark

@mark.smoke
@mark.body
class BodyTests:
    @mark.door
    def test_body_function_as_expected(self):
        assert True

    def test_bumber(self):
        assert True

    def test_windshield(self):
        assert True