# Q8) Social Media Platform:
# Develop a simplified social media platform with classes for users, posts,
# comments, likes, and interactions. Implement functionalities for user profiles, 
# content creation, and engagement.

# User class
class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id
        self.posts = []

    def create_post(self, content, platform):
        post = Post(self, content)
        self.posts.append(post)
        platform.add_post(post)
        print(f"{self.username} created a post: {content}")

    def print_profile(self):
        print(f"\nUser: {self.username} (ID: {self.user_id})")
        print(f"Number of posts: {len(self.posts)}")


# Post class
class Post:
    post_counter = 1

    def __init__(self, user, content):
        self.post_id = Post.post_counter
        Post.post_counter += 1
        self.user = user
        self.content = content
        self.comments = []
        self.likes = 0

    def add_comment(self, comment):
        self.comments.append(comment)
        print(f"{comment.user.username} commented on post {self.post_id}: {comment.content}")

    def add_like(self):
        self.likes += 1
        print(f"Post {self.post_id} liked! Total likes: {self.likes}")

    def print_post(self):
        print(f"\nPost ID: {self.post_id} by {self.user.username}")
        print(f"Content: {self.content}")
        print(f"Likes: {self.likes}")
        if self.comments:
            print("Comments:")
            for c in self.comments:
                print(f"- {c.user.username}: {c.content}")


# Comment class
class Comment:
    def __init__(self, user, content):
        self.user = user
        self.content = content


# Platform class
class Platform:
    def __init__(self):
        self.users = []
        self.posts = []

    def add_user(self, user):
        self.users.append(user)

    def add_post(self, post):
        self.posts.append(post)

    def show_all_posts(self):
        print("\nAll Posts on Platform:")
        if not self.posts:
            print("No posts yet.")
            return
        for post in self.posts:
            post.print_post()


platform = Platform()

# Add users
u1 = User("Suhana", 101)
u2 = User("Aman", 102)
platform.add_user(u1)
platform.add_user(u2)

# Users create posts
u1.create_post("Hello World! This is my first post.", platform)
u2.create_post("Excited to join this platform!", platform)

# Users interact with posts
post1 = platform.posts[0]
post2 = platform.posts[1]

# Likes
post1.add_like()
post2.add_like()
post2.add_like()

# Comments
c1 = Comment(u2, "Welcome Suhana!")
c2 = Comment(u1, "Thanks Aman!")
post1.add_comment(c1)
post2.add_comment(c2)

# Show all posts
platform.show_all_posts()

# Show user profiles
u1.print_profile()
u2.print_profile()
