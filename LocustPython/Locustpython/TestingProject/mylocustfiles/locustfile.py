import time
from locust import HttpUser, task, between, tag

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    i=0
    if(i==0):
        @tag('newpage')
        @task
        def hello_world(self):
            self.client.get("/",name='testpage')
    elif(i>0):
        @tag('blogpage')
        @task
        def hello_world(self):
            self.client.get("/page2-2")
    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})