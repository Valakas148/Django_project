import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from configs.celery import app


class EmailService:
    @staticmethod
    @app.task
    def __send_email(to: str, template_name:str, context:dict, subject='')-> None:
        template = get_template(template_name)
        html_content = template.render(context)
        message = EmailMultiAlternatives(subject=subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        message.attach_alternative(html_content, "text/html")
        message.send()

    @classmethod
    def send_email_to_manager(cls, announcement_id):
        context = {'id': announcement_id}
        manager_email = 'mmj51334@gmail.com'
        cls.__send_email('mmj51334@gmail.com', 'email_message_to_manager.html', context, 'User exhausted edit attempts')

    # @classmethod
    # def send_test(cls):
    #     cls.__send_email('mmj51334@gmail.com', 'email_message_to_manager.html', {}, 'Test Email')