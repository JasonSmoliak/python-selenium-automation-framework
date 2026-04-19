from faker import Faker
import random

fake = Faker()

def seed_data(seed_value=42):
    Faker.seed(seed_value)
    random.seed(seed_value)


def random_post_data():
    return {
        "title": fake.sentence(nb_words=6),
        "body": fake.paragraph(nb_sentences=3),
        "userId": random.randint(1, 10)
    }
