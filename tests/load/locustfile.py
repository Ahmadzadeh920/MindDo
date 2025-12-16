from locust import HttpUser, task, between




class FastAPIUser(HttpUser):  # MUST inherit HttpUser
    wait_time = between(1, 2)

    