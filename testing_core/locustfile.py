import random

from locust import HttpUser, task
from faker import Faker


fake = Faker()
created_users_list = []


class DjangoTesterUser(HttpUser):
    """
    url: http://localhost:8000
    """
    
    def __do_auth(self, username, password):
        r = self.client.post(
            "/accounts/auth/token/",
            json={
                "username": username,
                "password": password
            }
        )
        data = r.json()
        self.client.headers = {'Authorization': f"Bearer {data['access']}"}
    
    def __add_created_user_to_a_list(self, creation_response):
        data = creation_response.json()
        created_users_list.append(data['id'])
        print(f"create user with id #{data['id']}")
        
    def on_start(self):
        self.username = fake.unique.first_name()
        self.email = f"{self.username}@gmail.com"
        self.password = self.email
        r = self.client.post(
            "/accounts/create_user/",
            data={'username': self.username, 'email': self.email, 'password': self.email}
        )
        if r.status_code == 201:
            self.__add_created_user_to_a_list(r)
        self.__do_auth(self.username, self.email)
    
    def on_stop(self):
        for user_id in created_users_list:
            self.client.delete(f"/accounts/delete_user/{user_id}/")
            print(f"delete created user with id #{user_id}")
        print("all created users got deleted")
    
    @task
    def create_random_user(self):
        """
        create random user
        
        It's ok that this function fails sometimes, because some usernames are not unique.
        """
        random_name = fake.unique.first_name()
        email = f"{random_name}@gmail.com"
        r = self.client.post(
            "/accounts/create_user/",
            data={'username': random_name, 'email': email, 'password': email}
        )
        if r.status_code == 201:
            self.__add_created_user_to_a_list(r)

    @task
    def update_user_info(self):
        r = self.client.put(
            "/accounts/user_info/edit/",
            data={
                'username': self.username,
                'password': self.password,
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
            }
        )
        self.__do_auth(self.username, self.email)
    
    @task
    def fetch_users_list(self):
        self.client.get("/accounts/all/")


class GoTesterUser(HttpUser):
    """
    url: http://localhost:3000
    """
    
    @task
    def fetch_homepage(self):
        self.client.get("/")
