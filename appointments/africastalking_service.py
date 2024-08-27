import africastalking
from django.conf import settings

# Initialize the Africa's Talking SDK
africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)

# Create an instance of the SMS service
sms = africastalking.SMS

def send_sms(to, message):
    try:
        response = sms.send(message, to)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
