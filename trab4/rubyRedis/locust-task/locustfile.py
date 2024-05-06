import os
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    @task
    def extract_link(self):
        urls = [
            "https://github.com/",
            "https://stackoverflow.com/",
            "https://techcrunch.com/",
            "https://arstechnica.com/",
            "https://www.theverge.com/",
            "https://www.wired.com/",
            "https://www.producthunt.com/",
            "https://slashdot.org/",
            "https://www.cnet.com/",
            "https://medium.com/"
        ]
        for url in urls:
            self.client.get(f"/?url={url}")