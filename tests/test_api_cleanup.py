import pytest


@pytest.mark.api
def test_create_post_with_cleanup(created_post):
    assert "id" in created_post
    assert "title" in created_post
    assert "body" in created_post
    assert "userId" in created_post
