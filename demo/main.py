import json
from app.db.database import initital_db,LocalSession
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment

initital_db()

def insert_users():
    
    with open("demo/MOCK_DATA.json") as json_file:
        data = json.load(json_file)
        
    users = []
    
    for item in data:
        user = User(
            first_name = item["first_name"],
            last_name = item["last_name"],
            username = item["username"],
            gender = item["gender"],
            phone = item["phone"]   
        )
        users.append(user)
        
    db = LocalSession()
    
                                # db.add_all(users)
    db.bulk_save_objects(users)   #  -> BIG datalarni texkor uzulda ma'lumotlar bazasiga yozish.

    db.commit()

 
def insert_posts():
    
    with open("demo/posts.json") as json_file:
        data = json.load(json_file)
        
        db = LocalSession()
        
        posts = []
        
        for item in data:
            
            post = Post(
                title = item["title"],
                description = item["description"],
                author_id = item["author_id"]
            )
            
            posts.append(post)
            
        db.bulk_save_objects(posts)
        db.commit()
        
def insert_comment():
    
    with open("demo/comments.json") as json_file:
        
        data = json.load(json_file)
        
        db = LocalSession()
        
        comments = []
        
        for item in data:
            
            com = Comment(
                text = item["text"],
                author_id = item["author_id"],
                post_id = item["post_id"]
            )

            comments.append(com)
            
            
        db.add_all(comments)
        db.commit()
        
    
    

    
    
        
