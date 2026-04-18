import random
import string


def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_post_data():
    return {
        "title": f"Test Title {random_string()}",
        "body": f"Test Body {random_string(20)}",
        "userId": random.randint(1, 10)
    }
