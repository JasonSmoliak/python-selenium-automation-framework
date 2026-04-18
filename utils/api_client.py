import requests


class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def create_post(self, title, body, user_id=1):
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = requests.post(f"{self.BASE_URL}/posts", json=payload)
        assert response.status_code == 201, f"API failed: {response.status_code}"

        return response.json()

    def delete_post(self, post_id):
        response = requests.delete(f"{self.BASE_URL}/posts/{post_id}")
        assert response.status_code in (200, 204), (
            f"Delete failed: {response.status_code}"
        )
        return response
