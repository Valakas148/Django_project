import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class EmailService:
    @staticmethod
    def __send_email(to: str, template_name:str, context:dict, subject='')-> None:
        template = get_template(template_name)
        html_content = template.render(context)
        message = EmailMultiAlternatives(subject=subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        message.attach_alternative(html_content, "text/html")
        message.send()

    @classmethod
    def send_test(cls):
        cls.__send_email('mmj51334@gmail.com', 'email_message_to_manager.html', {}, 'Test Email')