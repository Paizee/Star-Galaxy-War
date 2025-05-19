import os
from supabase import create_client, Client
from dotenv import load_dotenv, dotenv_values 
import Player
import Leaderboard

class Database():
    def __init__(self):
        load_dotenv()
        url: str = os.getenv("SUPABASE_URL")
        key: str = os.getenv("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

    def create_user(self,email: str, password: str,username: str, player: Player.Player):
        response = self.supabase.auth.sign_up(
            {
                "email": email, 
                "password": password,
                "options": {"data": {"username": username}},
            }
        )
        
        self.get_user_info(user_id=response.user.id,player=player)
        
        
    def login_user(self,email: str, password: str, player: Player.Player):
        response = self.supabase.auth.sign_in_with_password(
            {
                "email": email, 
                "password": password,
            }
        )
        
        self.get_user_info(user_id=response.user.id,player=player)

    def check_username_given(self,username: str):
        response = (
            self.supabase.table("users")
            .select("name")
            .eq("name",username)
            .execute()
        )
        return len(response.data) > 1


    def check_email_given(self,email:str):
        response = (
            self.supabase.rpc("email_exists",params={"user_email": email})
            .execute()
        )
        print(response.data)
        return response.data # true if exist
    
    def check_password_correct(self,email:str ,password: str):
        response = (
            self.supabase.rpc("check_password",params={"password": password,"user_email": email})
            .execute()
        )
        return response.data

    def get_user_info(self,user_id: str,player: Player.Player):
        response_user = (
            self.supabase.table("users")
            .select("coins,name")
            .eq("user_id",user_id)
            .maybe_single()
            .execute()
        )
        
        player.coins = int(response_user.data["coins"])
        player.name = response_user.data["name"]
        player.user_id = user_id # uuid
        
    def logout(self,player: Player.Player): 
        
        player.name = "Player"
        player.user_id = None
        player.coins = 0

    def db_add_coins(self,player: Player.Player,amount: int):
        
        response_user = (
            self.supabase.table("users")
            .select("coins")
            .eq("user_id",player.user_id)
            .maybe_single()
            .execute()
        )
                
        (
            self.supabase.table("users")
            .update({"coins": int(response_user.data["coins"]) + amount})
            .eq("user_id", player.user_id)
            .execute()
        )
    
    def get_leaderboard(self):
        
        response_leaderboard = (
            self.supabase.table("users")
            .select("coins,name")
            .limit(size=5)
            .execute()
        )
        
        leaderboard_list = []
        
        for x in response_leaderboard.data:
           leaderboard_list.append(Leaderboard.Leaderboard_Item(username=x["name"],coins=x["coins"])) 
        
        if len(leaderboard_list) < 5:
            for x in range(5 - len(leaderboard_list)):
                leaderboard_list.append(Leaderboard.Leaderboard_Item(username="Placeholder",coins=0)) 
                
        return leaderboard_list