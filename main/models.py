from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Notification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    notification_content = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id


class Friendship(models.Model):
    user_id1 = models.ForeignKey(User, related_name='person2persons', on_delete=models.CASCADE)
    user_id2 = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)

    def __str__(self):
        return "{} and {}".format(self.user_id1, self.user_id2)


class PrivateChatting(models.Model):
    friendship_id = models.ForeignKey(Friendship, on_delete=models.CASCADE)
    chat_time = models.DateField()
    message_content = models.TextField()

    def __str__(self):
        return "friendship id - {}".format(self.friendship_id)


class Activity(models.Model):
    happen_time = models.DateField()
    organizer_id = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return "organizer id - {}".format(self.organizer_id)


class GroupChatting(models.Model):
    activity_id = models.ForeignKey(Activity, models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_time = models.DateField()
    message_content = models.TextField()

    def __str__(self):
        return "activity id - {}".format(self.activity_id)
