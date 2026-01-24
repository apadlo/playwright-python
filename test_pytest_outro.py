class TestPytesOutro:

    def test_hi_again(self, get_name):
        print(f"Hi again, {get_name}")

    def test_many_users(self, polish_user_factory):
        user1 = polish_user_factory()
        user2 = polish_user_factory()
        assert user1["email"] != user2["email"]
        print("\n", user1)
        print(user2)