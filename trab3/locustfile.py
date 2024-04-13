from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def create_post_with_large_image(self):
        with open("/locust/1mb-image.jpg", "rb") as f:
            image_data = f.read()
        self.client.post("/wp-admin/post-new.php", files={"file": image_data})

    @task
    def create_post_with_medium_image(self):
        with open("/locust/300kb-image.jpg", "rb") as f:
            image_data = f.read()
        self.client.post("/wp-admin/post-new.php", files={"file": image_data})

    @task
    def create_post_with_large_text(self):
        with open("/locust/400kb-text.txt", "r") as f:
            text_data = f.read()
        self.client.post("/wp-admin/post-new.php", data={"content": text_data})
