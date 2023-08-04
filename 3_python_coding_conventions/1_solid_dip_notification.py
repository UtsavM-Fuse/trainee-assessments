from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient: str, subject: str, message: str) -> None:
        """
        Send a message to the recipient with the given subject and message.

        Args:
            recipient (str): The email address of the recipient.
            subject (str): The subject of the message.
            message (str): The content of the message.

        Returns:
            None
        """
        pass


class EmailSender(MessageSender):
    def send_message(self, recipient: str, subject: str, message: str) -> None:
        """
        Send an email to the recipient with the given subject and message.

        Args:
            recipient (str): The email address of the recipient.
            subject (str): The subject of the email.
            message (str): The content of the email.

        Returns:
            None
        """
        print(f"Sending email to {recipient}: {subject} - {message}")


class NotificationService:
    def __init__(self, message_sender: MessageSender):
        self.message_sender = message_sender

    def send_notification(self, recipient: str, message: str) -> None:
        """
        Send a notification to the recipient.

        Args:
            recipient (str): The email address of the recipient.
            message (str): The content of the notification.

        Returns:
            None
        """
        self.message_sender.send_message(recipient, "Notification", message)


# Using the NotificationService with EmailSender to send a notification
email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification(
    "user123@example.com", "Hello, this is a notification!"
)
