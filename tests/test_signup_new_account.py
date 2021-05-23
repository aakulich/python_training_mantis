import string
import random




def random_username(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_signup_new_account(app):
    username = "user1"
    password = "test"
    app.james.ensure_user_exists(username, password)