from utils.data_builders import PostDataBuilder


def test_post_data_builder_allows_overrides():
    data = (
        PostDataBuilder()
        .with_title("Custom Title")
        .with_body("Custom Body")
        .with_user_id(99)
        .build()
    )

    assert data["title"] == "Custom Title"
    assert data["body"] == "Custom Body"
    assert data["userId"] == 99
