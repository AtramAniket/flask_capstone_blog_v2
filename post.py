import os
import requests
from dotenv import load_dotenv

class Post:

    def __init__(self):

        load_dotenv()

        self.posts = self.get_all_blog_posts()

    def get_all_blog_posts(self) -> dict:

        response = requests.get(os.getenv("BLOG_API"))

        data = response.json()

        return data 

    def get_post_by_id(self, post_id) -> dict:
        """
            This method is used for filtering post based on ID
        """

        return [post for post in self.posts if post["id"] == post_id]
    
