from pytest import mark

@mark.smoke
@mark.engine
class EngineTests:
    def test_engine_function_as_expected(self):
        assert True