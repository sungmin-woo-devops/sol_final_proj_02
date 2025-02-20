from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Post(models.Model):
    title = models.CharField(max_length=200)  # 제목
    content = models.TextField()              # 내용
    author = models.CharField(max_length=100) # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일

    def __str__(self):
        return self.title

@receiver(post_migrate, sender='board')
def create_sample_posts(sender, **kwargs):
    from django.db import transaction
    if not Post.objects.exists():
        with transaction.atomic():
            posts = [
                {"title": "첫 번째 게시글", "content": "내용1", "author": "사용자1"},
                {"title": "두 번째 게시글", "content": "내용2", "author": "사용자2"},
                {"title": "세 번째 게시글", "content": "내용3", "author": "사용자3"},
                {"title": "네 번째 게시글", "content": "내용4", "author": "사용자4"},
                {"title": "다섯 번째 게시글", "content": "내용5", "author": "사용자5"},
            ]
            for post_data in posts:
                Post.objects.create(
                    title=post_data["title"],
                    content=post_data["content"],
                    author=post_data["author"]
                )
