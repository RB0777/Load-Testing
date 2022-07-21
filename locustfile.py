from locust import HttpUser,task,between
import random

sentences=["HELLO, Doing a load testing using locust",
"It is a python based framework",
"Can be used to do multiple load testing"]
class AppUser(HttpUser):
    wait_time=between(1,5)

    @task 
    def index_page(self):
        self.client.get("/")

    @task(8)
    def sentiment_page(self):
        mytext = random.choice(sentences)
        self.client.get("/sentiment/"+str(mytext))