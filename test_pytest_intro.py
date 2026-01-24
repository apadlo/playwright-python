class TestPytestIntro:

    def test_hi(self, get_name):
        print(f"Hi, {get_name}")

    def test_user_data(self, polish_user_factory):
        print(polish_user_factory())