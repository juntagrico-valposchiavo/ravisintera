from django.conf import settings

class Mailer:
    def send(msg):
        from_email = msg.from_email
        if msg.reply_to is None or len(msg.reply_to)==0:
            msg.reply_to = [from_email]
        msg.from_email = getattr(settings, 'EMAIL_HOST_USER', None)
        msg.send()
