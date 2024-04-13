from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def index(self):
        self.client.get("/")

    @task
    def blog_post_with_image(self):
        self.client.get("/blog-post-with-image")

    @task
    def blog_post_with_text(self):
        self.client.get("/blog-post-with-text")

    @task
    def blog_post_with_small_image(self):
        self.client.get("/blog-post-with-small-image")
