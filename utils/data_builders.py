from utils.data_generator import random_post_data


class PostDataBuilder:
    def __init__(self):
        self.data = random_post_data()

    def with_title(self, title):
        self.data["title"] = title
        return self

    def with_body(self, body):
        self.data["body"] = body
        return self

    def with_user_id(self, user_id):
        self.data["userId"] = user_id
        return self

    def without_title(self):
        self.data.pop("title", None)
        return self

    def without_body(self):
        self.data.pop("body", None)
        return self

    def without_user_id(self):
        self.data.pop("userId", None)
        return self

    def with_empty_title(self):
        self.data["title"] = ""
        return self

    def with_long_title(self, length=256):
        self.data["title"] = "A" * length
        return self

    def with_invalid_user_id(self):
        self.data["userId"] = "invalid-user-id"
        return self

    def build(self):
        return self.data
