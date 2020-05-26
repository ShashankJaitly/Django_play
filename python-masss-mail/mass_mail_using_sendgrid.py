import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To

data = [
# THIS IS SSAMPLE DATA
#     {
#     "email": "shashank.1822co1053@kiet.edu",
#     "name": "Shashank Jaitly"
#   },
#   {                                                   
#     "email": "shashank16vasu@gmail.com",
#     "name": "Shashank"
#   },
]
recipent_list=[]
user_list = []
for user in data:
        recipent_list.append(user['email'])
        user_list.append(user['name'])

to_emails = []
for recipent in range(0,len(recipent_list)):
    email=To(email=recipent_list[recipent],
            name=user_list[recipent],
            substitutions={
                '-name-': user_list[recipent],
            })
    to_emails.append(email)

   

message = Mail(
    from_email=('shashank16jaitly@gmail.com', 'Shashank'),
    to_emails=to_emails,
    subject='Hi -name-, this is a test mail',
    html_content=""" PUT YOUR MAILING TEMPLATE HERE """,
    
    is_multiple=True)
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)



