import os
import json
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, To, Attachment, FileContent, FileName, FileType, Disposition)

data = [
# THIS IS SAMPLE DATA
        
#     {
#         "name": "Aakanksha shivani",
#         "email": "shivaniaakanksha@gmail.com"
#     },
#     {
#         "name": "Aakash Goel",
#         "email": "goelaakash79@gmail.com"
#     },
#     {
#         "name": "Aayush sharma",
#         "email": "ayushc45xxx@gmail.com"
#     },
#     {
#         "name": "Abhishek Swaroop Shrivastava",
#         "email": "gh4abhi@gmail.com"
#     },
#     {
#         "name": "Aditya Pandey",
#         "email": "icgadi99@gmail.com"
#     },
#     {
#         "name": "Aniket Padmansh",
#         "email": "pudmaansh@gmail.com"
#     },
#     {
#         "name": "Anshul Gupta",
#         "email": "ag1507anshul@gmail.com"
#     },
#     {
#         "name": "Dhruv Aggarwal",
#         "email": "dhruv.1822it1051@kiet.edu"
#     },
#     {
#         "name": "Ishita jaiswal",
#         "email": "ishitajaiswal4m@gmail.com"
#     },
#     {
#         "name": "Lakshay kumar",
#         "email": "lakshaykumar0510@gmail.com"
#     },
#     {
#         "name": "Manvendra Pratap Singh",
#         "email": "manvendra.1923en1094@kiet.edu"
#     },
#     {
#         "name": "Mayank Shakya",
#         "email": "mayankshakya992@gmail.com"
#     },
#     {
#         "name": "Nidhaan Srivastava",
#         "email": "nidhanranjan@gmail.com"
#     },
#     {
#         "name": "Priyanshu Sharma",
#         "email": "priyanshus.edu@gmail.com"
#     },
#     {
#         "name": "Ritik Srivastava",
#         "email": "ritiksr25@gmail.com"
#     },
#     {
#         "name": "Ritwick Bhargav",
#         "email": "ritwickbhargav80@gmail.com"
#     },
#     {
#         "name": "Satyam Sharma",
#         "email": "satyamx64@gmail.com"
#     },
#     {
#         "name": "Shashank Jaitly",
#         "email": "shashank16vasu@gmail.com"
#     },
#     {
#         "name": "Shreeyanshi Gupta",
#         "email": "shree21gupta@gmail.com"
#     },
#     {
#         "name": "Shubham Goswami",
#         "email": "sgshubham98@gmail.com"
#     },
#     {
#         "name": "Shubham Singh",
#         "email": "ss100ev@gmail.com"
#     },
#     {
#         "name": "Shubhangi",
#         "email": "shubhangi22062000@gmail.com"
#     },
#     {
#         "name": "Umang",
#         "email": "umang0503@gmail.com"
#     },
#     {
#         "name": "Vidit Jha",
#         "email": "jhavidit@gmail.com"
#     },
#     {
#         "name": "Ashutosh dubey",
#         "email": "ashutoshdubey2508@gmail.com"
#     },
#     {
#         "name": "Rohan Mehta",
#         "email": "rhnmht30@gmail.com"
#     },
#     {
#         "name": "Harshal Sharma",
#         "email": "sharma.harshal509@gmail.com"
#     }

# ]
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
    from_email=('from@gmail.com', 'sender\'s name'),
    to_emails=to_emails,
    subject='Hi -name-, this is a test mail',
    html_content=""" PUT YOUR MAILING TEMPLATE HERE """,
    
    is_multiple=True)

# Sample for attachments
# with open('attachment.pdf', 'rb') as f:
#     data = f.read()
#     f.close()
# encoded_file = base64.b64encode(data).decode()

# attachedFile = Attachment(
#     FileContent(encoded_file),
#     FileName('attachment.pdf'),
#     FileType('application/pdf'),
#     Disposition('attachment')
# )
# message.attachment = attachedFile

try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)



