import os
from supabase import create_client, Client
from dotenv import load_dotenv, dotenv_values 

class Database():
    def __init__(self):
        load_dotenv()
        url: str = os.getenv("SUPABASE_URL")
        key: str = os.getenv("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

    def create_user(self,email: str, password: str,username: str):
        response = self.supabase.auth.sign_up(
            {
                "email": email, 
                "password": password,
                 "options": {"data": {"username": username}},
            }
        )
    def login_user(self,email: str, password: str):
        response = self.supabase.auth.sign_in_with_password(
            {
                "email": email, 
                "password": password,
            }
        )
        
    def check_username_given(self,username: str):
        response = (
            self.supabase.table("users")
            .select("name")
            .eq("name",username)
            .execute()
        )
        return len(response.data) > 1

    def check_email(self,email:str):
        return False

    def check_password(self,password: str):
        return False

        
