from locust import HttpUser, task


class DjangoTesterUser(HttpUser):
    """
    url: http://localhost:8000
    """
    
    def on_start(self):
        r = self.client.post("/accounts/auth/token/", json={"username":"sina", "password":"123"})
        data = r.json()
        self.client.headers = {'Authorization': f"Bearer {data['access']}"}
        
    @task
    def hello_world(self):
        self.client.get("/accounts/all/")
