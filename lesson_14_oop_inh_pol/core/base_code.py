# student_task_notifications.py

class Notification:
    def __init__(self, message):
        self.message = message
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    pass

notifications = [
EmailNotification("Hello via Email"),
#SMSNotification("Hello via SMS"),
#PushNotification("Hello via Push")
]

for n in notifications:
    n.send()
