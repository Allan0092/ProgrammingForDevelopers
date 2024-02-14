class Node:
    def __init__(self, _data):
        self.data = _data
        self.left = self.right = None


class Graph:
    def __init__(self, root: Node):
        self.root = root



class User:
    def __init__(self, username: str, following: list=[], liked: list=[], disliked: list=[], oid: int=None):
        self.username = username
        self.following = following
        self.liked = liked
        self.disliked = disliked
        self.oid = oid
    
    def print_details(self):
        print(f"username: {self.username} \nfollowing: {self.following}\nliked: {self.liked}\ndisliked: {self.disliked}\n oid: {self.oid}")


class Content:
    def __init__(self, _posted_by: User, _type:str="", _paragraph: str = "", _likes: int=0, _dislikes: int=0) -> None:
        self._posted_by = _posted_by
        self.type = _type
        self.paragraph = _paragraph
        self.likes = _likes
        self.disliked = _dislikes


