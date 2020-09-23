from django.db import models

# Create your models here.
class TodoModel(models.Model):
    #Charfield
    #migrationのカラムの設定
    title = models.CharField(max_length=100)
    memo = models.TextField()
    #テーブルのカラム名ような名前を作成
    def __str__(self):
        return self.title
    