from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def extract_link(self):
        urls = [
            "https://github.com",
        ]

        for url in urls:
            self.client.post("/api/", json={"url": url}, headers={"Content-Type": "application/json"})

