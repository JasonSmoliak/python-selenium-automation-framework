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

    def build(self):
        return self.data
