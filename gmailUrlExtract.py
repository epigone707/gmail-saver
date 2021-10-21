from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import base64
import email
import re

"""
Gmail API python quickstart tutorial:
https://developers.google.com/gmail/api/quickstart/python

Gmail API PyDoc documentation:
https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/index.html
"""

# regex that can extract url links
# copy from: https://stackoverflow.com/questions/839994/extracting-a-url-in-python
url_regex=r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    # get all labels
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            # print(label['name'])
            print(label)
    print("==============================")

    # get all messages in the specified label
    msg_results = service.users().messages().list(userId='me',labelIds='Label_7090689821639516814',includeSpamTrash=True).execute()
    msg_id_list= []
    if not msg_results:
        print('No msg found.')
    else:
        print('print all messages info:')
        print(msg_results)
        for msg in msg_results["messages"]:
            print("msg id: ", msg["id"])
            msg_id_list.append(msg["id"])
    print("==============================")
    # Gets the specified message.
    for msg_id in msg_id_list:
        msg = service.users().messages().get(userId='me',id=msg_id,format="raw").execute()
        print("\n################ msg: ",msg_id," ################\n")
        msg_str = base64.urlsafe_b64decode(msg["raw"].encode('ASCII'))
        mime_msg = email.message_from_bytes(msg_str)
        msg_text_str = ""
        for part in mime_msg.walk():
            if part.get_content_type()=="text/plain" :
                message = part.get_payload(decode=True)
                msg_text_str = msg_text_str+message.decode()+"\n\n"
        # print(msg_text_str)
        # extract url links
        print("\nextracted urls:")
        url_links= re.findall(url_regex, msg_text_str)
        print(url_links)
        print("\n################ finish: ",msg_id," ################\n")



if __name__ == '__main__':
    main()