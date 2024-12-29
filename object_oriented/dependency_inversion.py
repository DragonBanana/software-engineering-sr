# Exercise 11 - Dependency Inversion
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class Notification:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        self.service.send(message)

if __name__ == '__main__':
    email_notification = Notification(EmailService())
    sms_notification = Notification(SMSService())
    email_notification.notify("Email message")
    sms_notification.notify("SMS message")
