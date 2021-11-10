from django.utils import timezone
from .token_manager import TokenManager, error_type, MaxRetriesExceeded
from django.core.signing import SignatureExpired, BadSignature

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

# Subscription Logic
def subscribe(first_name, second_name, email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
        'merge_fields': {
            'FNAME': first_name,
            'LNAME': second_name,
        }
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))

class _UserActivationProcess:
    """
    This class is pretty self.explanatory...
    """

    def __init__(self):
        self.token_manager = TokenManager()

    @staticmethod
    def __activate_user(user):
        user.is_active = True
        user.last_login = timezone.now()
        user.save()
        email = user.email
        first_name = user.first_name
        second_name = user.second_name
        subscribe(first_name, second_name, email)

    def verify_token(self, useremail, usertoken):
        try:
            user = self.token_manager.decrypt_link(useremail, usertoken)
            if user:
                self.__activate_user(user)
                return True
            return False
        except (ValueError, TypeError):
            return error_type.failed
        except SignatureExpired:
            return error_type.expired
        except BadSignature:
            return error_type.tempered
        except MaxRetriesExceeded:
            return error_type.mre


def _verify_user(useremail, usertoken):
    return _UserActivationProcess().verify_token(useremail, usertoken)
