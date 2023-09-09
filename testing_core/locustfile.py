import random

from locust import HttpUser, task
from faker import Faker


fake = Faker()
created_users_list = []


class DjangoTesterUser(HttpUser):
    """
    url: http://localhost:8000
    """
    
    def on_start(self):
        r = self.client.post("/accounts/auth/token/", json={"username":"sina", "password":"123"})
        data = r.json()
        self.client.headers = {'Authorization': f"Bearer {data['access']}"}
        # create a user
        random_name = fake.unique.first_name()
        email = f"{random_name}@gmail.com"
        r = self.client.post(
            "/accounts/create_user/",
            data={'username': random_name, 'email': email, 'password': email}
        )
        if r.status_code == 201:
            data = r.json()
            created_users_list.append(data['username'])
    
    def on_stop(self):
        for user in created_users_list:
            # TODO, delete created users
            pass
        
        
    @task
    def create_random_user(self):
        random_name = fake.unique.first_name()
        email = f"{random_name}@gmail.com"
        r = self.client.post(
            "/accounts/create_user/",
            data={'username': random_name, 'email': email, 'password': email}
        )
        if r.status_code == 201:
            data = r.json()
            created_users_list.append(data['username'])
        
    @task
    def fetch_and_update_user(self):
        r = self.client.get("/accounts/user_info/")
        data = r.json()
        r = self.client.put(
            "/accounts/user_info/edit/",
            data={'username': data['username'][::-1], 'password': '123'}
        )
        
    @task
    def fetch_users_list(self):
        self.client.get("/accounts/all/")
