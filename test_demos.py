import pytest

class TestPolishUser:

    @pytest.mark.sanity
    def test_user_data(self, polish_user_factory):
        user = polish_user_factory()
        print(user)

        assert user is not None

    @pytest.mark.sanity
    def test_user_has_required_fields(self, polish_user_factory):
        user = polish_user_factory()

        expected_fields = {
            "full_name",
            "first_name",
            "last_name",
            "email",
            "pesel",
            "phone",
            "city",
            "gender",
        }
        assert expected_fields.issubset(user.keys())

    @pytest.mark.regression
    @pytest.mark.xfail
    def test_email_matches_name(self, polish_user_factory):
        user = polish_user_factory()

        email_prefix = user["email"].split("@")[0]

        assert user["first_name"].lower() in email_prefix
        assert user["last_name"].lower() in email_prefix

    @pytest.mark.regression
    @pytest.mark.xfail
    def test_gender_matches_pesel(self, polish_user_factory):
        user = polish_user_factory()

        last_digit = int(user["pesel"][-1])

        if user["gender"] == "male":
            assert last_digit % 2 == 1
        else:
            assert last_digit % 2 == 0

    @pytest.mark.sanity
    def test_pesel_format(self, polish_user_factory):
        user = polish_user_factory()

        pesel = user["pesel"]

        assert len(pesel) == 11
        assert pesel.isdigit()

    @pytest.mark.regression
    def test_email_domain_is_polish(self, polish_user_factory):
        user = polish_user_factory()

        domain = user["email"].split("@")[1]

        assert domain in {"gmail.com", "wp.pl", "onet.pl", "interia.pl", "o2.pl"}

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_factory_creates_unique_users(self, polish_user_factory):
        user1 = polish_user_factory()
        user2 = polish_user_factory()

        assert user1["pesel"] != user2["pesel"]
        assert user1["email"] != user2["email"]
