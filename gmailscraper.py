from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import base64
import email
import argparse
import re
from datetime import date, timedelta
import datetime
import time

# https://github.com/lipoja/URLExtract
from urlextract import URLExtract
"""
Gmail API python quickstart tutorial:
https://developers.google.com/gmail/api/quickstart/python

Gmail API PyDoc documentation:
https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/index.html
"""

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    # Initialize parser
    msg = "gmail scrapper. All dates used in the search query are interpreted as midnight on that date in the PST timezone."
    parser = argparse.ArgumentParser(description=msg)
    # Adding optional argument
    parser.add_argument("-l", "--label", help="target label id")
    parser.add_argument('-s',
                        "--startdate",
                        help="The Start Date - format YYYY-MM-DD. e.g. 2022-01-01",
                        type=datetime.date.fromisoformat)
    parser.add_argument('-e',
                        "--enddate",
                        help="The End Date format YYYY-MM-DD",
                        type=datetime.date.fromisoformat)

    # Read arguments from command line
    args = parser.parse_args()

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
        return

    if not args.label:
        print('Print all labels:')
        for label in labels:
            # print(label['name'])
            print(label)
        print("==============================")
        return

    # get all messages in the specified label
    labelId = args.label
    msg_results = []
    if args.startdate and args.enddate:
        # Dates have to formatted in YYYY/MM/DD format for gmail
        query = "before: {0} after: {1}".format(
            args.enddate.strftime('%Y/%m/%d'),
            args.startdate.strftime('%Y/%m/%d'))
        print("Filter messages by date range: ", query)
        msg_results = service.users().messages().list(maxResults=1000,
                                                      userId='me',
                                                      labelIds=labelId,
                                                      includeSpamTrash=True,
                                                      q=query).execute()
    else:
        print("No filter. Print last 1000 messages.")
        msg_results = service.users().messages().list(
            maxResults=1000,
            userId='me',
            labelIds=labelId,
            includeSpamTrash=True,
        ).execute()

    msg_id_list = []
    if not msg_results:
        print('No msg found.')
        return
    else:
        print('print messages info in label: ', labelId)
        print(msg_results)
        for msg in msg_results["messages"]:
            msg_id_list.append(msg["id"])
    print("==============================")
    # Gets the messages.
    count = 0
    if args.startdate and args.enddate:
        messagesfile= open(f'{args.startdate} - {args.enddate} label {labelId} msgs.txt',"w+")
        urlsfile= open(f'{args.startdate} - {args.enddate} label {labelId} urls.txt',"w+")
    else:
        messagesfile= open(f'{time.time()} label {labelId} 1000 msgs.txt',"w+")
        urlsfile= open(f'{time.time()} label {labelId} 1000.txt',"w+")
    print("Dumping the messages and extracting urls in them...")
    for msg_id in msg_id_list:
        msg = service.users().messages().get(userId='me',
                                             id=msg_id,
                                             format="raw").execute()
        messagesfile.write(f'\n\n################ msg: {msg_id}  ################\n\n')
        msg_str = base64.urlsafe_b64decode(msg["raw"].encode('ASCII'))
        mime_msg = email.message_from_bytes(msg_str)
        msg_text_str = ""
        for part in mime_msg.walk():
            if part.get_content_type() == "text/plain":
                message = part.get_payload(decode=True)
                msg_text_str = msg_text_str + message.decode() + "\n\n"
        messagesfile.write(msg_text_str)

        # extract url links
        urlsfile.write(f'{msg_id} extracted urls:')
        messagesfile.write(f'\nextracted urls:')
        extractor = URLExtract()
        url_links = extractor.find_urls(msg_text_str)
        for url_link in url_links:
            urlsfile.write(url_link + ", ")
            messagesfile.write(url_link + ", ")
        urlsfile.write("\n")
        count = count + 1
    urlsfile.write(f'Total messages count: {count}')
    print(f'Finished. Total messages count: {count}')
    print(f'Dump messages to {messagesfile.name}')
    print(f'Dump extracted urls to {urlsfile.name}')
    urlsfile.close()
    messagesfile.close()


if __name__ == '__main__':
    main()