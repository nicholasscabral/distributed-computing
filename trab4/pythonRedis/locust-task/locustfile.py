import os
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    @task
    def extract_link(self):
        urls = [
            "https://www.reddit.com/r/brdev/",
            "https://news.ycombinator.com/",
            "https://github.com/spring-projects/spring-boot",
            "https://github.com/topics/aws",
            "https://github.com/covid19india/covid19india-react",
            "https://github.com/carlosruan12307?tab=repositories",
            "https://github.com/etcd-io/etcd",
            "https://github.com/twbs/bootstrap",
            "https://github.com/macrozheng/mall",
            "https://github.com/facebook/react-native"
        ]
        for url in urls:
            self.client.get(f"/?url={url}")