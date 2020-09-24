from django.db import models

# Create your models here.

#''
PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))
class TodoModel(models.Model):
    #Charfield
    #migrationのカラムの設定
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()

    #テーブルのカラム名ような名前を作成
    def __str__(self):
        return self.title
