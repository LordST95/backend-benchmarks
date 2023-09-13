import random

from locust import HttpUser, task
from faker import Faker


fake = Faker()
created_users_list = []


class DjangoTesterUser(HttpUser):
    """
    url: http://localhost:8000
    """
    main_admin_user = "sina"
    main_admin_pass = "123"
    
    def on_start(self):
        r = self.client.post(
            "/accounts/auth/token/",
            json={
                "username": self.main_admin_user,
                "password": self.main_admin_pass
            }
        )
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
            created_users_list.append(data['id'])
            print(f"create user with id #{data['id']}")
    
    def on_stop(self):
        for user_id in created_users_list:
            self.client.delete(f"/accounts/delete_user/{user_id}/")
            print(f"delete created user with id #{user_id}")
        print("all created users got deleted")
        r = self.client.put(
            "/accounts/user_info/edit/",
            data={'username': self.main_admin_user, 'password': self.main_admin_pass}
        )
            
        
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
            created_users_list.append(data['id'])
            print(f"create user with id #{data['id']}")

    @task
    def fetch_and_update_user(self):
        r = self.client.get("/accounts/user_info/")
        data = r.json()
        r = self.client.put(
            "/accounts/user_info/edit/",
            data={'username': data['username'][::-1], 'password': self.main_admin_pass}
        )
        
    @task
    def fetch_users_list(self):
        self.client.get("/accounts/all/")
