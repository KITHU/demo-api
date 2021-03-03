from os import getenv
import africastalking


def send_sms(message,cell):
    ''' 
        Function to send sms
            arguments:
                        - mobile number: '+254722000000'
                        - message to send : 'hello there'
    '''
    username = getenv('USERNAME')
    api_key = getenv('API_KEY')


    africastalking.initialize(username, api_key)

    sms = africastalking.SMS

    try:
        response = sms.send(message, [cell])
        print(response)
    except Exception as e:
        print(f"Something went wrong {e}")
