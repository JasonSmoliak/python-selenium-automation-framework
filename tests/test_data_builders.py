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


def test_post_data_builder_can_remove_required_fields():
    data = (
        PostDataBuilder()
        .without_title()
        .without_body()
        .without_user_id()
        .build()
    )

    assert "title" not in data
    assert "body" not in data
    assert "userId" not in data


def test_post_data_builder_can_create_edge_case_values():
    data = (
        PostDataBuilder()
        .with_empty_title()
        .with_long_title(300)
        .with_invalid_user_id()
        .build()
    )

    assert data["title"] == "A" * 300
    assert data["userId"] == "invalid-user-id"
