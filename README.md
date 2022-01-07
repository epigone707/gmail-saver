# gmailSaver

The gmailSaver can download emails from a gmail account by using Gmail API and extract all url links in them.

# Setup
You need to follow the [gmail python tutorial](https://developers.google.com/gmail/api/quickstart/python).

The tutorial prerequisites contain:
- Python 2.6 or greater.
- The pip package management tool.
- A Google Cloud Platform project with the API enabled. To create a project and enable an API, refer to [Create a project and enable the API](https://developers.google.com/workspace/guides/create-project). Enable the "Gmail API".
- Authorization credentials for a desktop application. To learn how to create credentials for a desktop application, refer to [Create credentials](https://developers.google.com/workspace/guides/create-credentials). There're 3 types of credentials. I choose [OAuth client ID credentials(application type = Desktop app)](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id).
- A Google account with Gmail enabled.

Follow the tutorial, install the Google client library for Python, run the following command:
```
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
After you've done, download the credential file and name it as `credentials.json` . 


# Usage

Print help message.
```
$ python gmailscraper.py -h
usage: gmailscraper.py [-h] [-l LABEL] [-s STARTDATE] [-e ENDDATE]

gmail scrapper. All dates used in the search query are interpreted as midnight on that date in the PST
timezone.

optional arguments:
  -h, --help            show this help message and exit
  -l LABEL, --label LABEL
                        target label id
  -s STARTDATE, --startdate STARTDATE
                        The Start Date - format YYYY-MM-DD. e.g. 2022-01-01
  -e ENDDATE, --enddate ENDDATE
                        The End Date format YYYY-MM-DD
```

Print all labels in your gmail account. Gmail API will ask you to log in a gmail account and give permission. After that, `token.json` will be created automatically when the authorization flow completes.

```
$ python gmailscraper.py
Print all labels:
{'id': 'CHAT', 'name': 'CHAT', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'SENT', 'name': 'SENT', 'type': 'system'}
{'id': 'INBOX', 'name': 'INBOX', 'type': 'system'}
{'id': 'IMPORTANT', 'name': 'IMPORTANT', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'TRASH', 'name': 'TRASH', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'DRAFT', 'name': 'DRAFT', 'type': 'system'}
{'id': 'SPAM', 'name': 'SPAM', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'CATEGORY_FORUMS', 'name': 'CATEGORY_FORUMS', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'CATEGORY_UPDATES', 'name': 'CATEGORY_UPDATES', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'CATEGORY_PERSONAL', 'name': 'CATEGORY_PERSONAL', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'CATEGORY_PROMOTIONS', 'name': 'CATEGORY_PROMOTIONS', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'CATEGORY_SOCIAL', 'name': 'CATEGORY_SOCIAL', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'STARRED', 'name': 'STARRED', 'type': 'system'}
{'id': 'UNREAD', 'name': 'UNREAD', 'type': 'system'}
{'id': 'Label_7090689821639516814', 'name': 'testLabel', 'type': 'user'}
==============================
```

Print messages in a label given the label id and the date range. Here, I choose the 'INBOX' label.
```
$ python gmailscraper.py -l INBOX -s 2021-11-20 -e 2022-01-01
Filter messages by date range:  before: 2022/01/01 after: 2021/11/20
print messages info in label:  INBOX
{'messages': [{'id': '17e124d392914484', 'threadId': '17e124d392914484'}, {'id': '17e086cade84f299', 'threadId': '17e086cade84f299'}, {'id': '17dff28a8e2a9ad2', 'threadId': '17dff28a8e2a9ad2'}, {'id': '17dfca8b8d591eb5', 'threadId': '17dfca8b8d591eb5'}, {'id': '17df7d34603cae8a', 'threadId': '17df7d34603cae8a'}, {'id': '17ded64af41efd50', 'threadId': '17ded64af41efd50'}, {'id': '17de40a1095b50f5', 'threadId': '17de40a1095b50f5'}, {'id': '17dddfd8ead14bee', 'threadId': '17dddfd8ead14bee'}, {'id': '17dd9e74af4fb8b2', 'threadId': '17dd9e74af4fb8b2'}, {'id': '17dd3e3098cd2e49', 'threadId': '17dd3e3098cd2e49'}, {'id': '17dcfaa0dab3b288', 'threadId': '17dcfaa0dab3b288'}, {'id': '17dc97cab7c5b45e', 'threadId': '17dc97cab7c5b45e'}, {'id': '17dc466740c73961', 'threadId': '17dc466740c73961'}, {'id': '17dc01504d9faa5d', 'threadId': '17dc01504d9faa5d'}, {'id': '17dbbdb5e12496a5', 'threadId': '17dbbdb5e12496a5'}, {'id': '17db4f8b084883c0', 'threadId': '17db4f8b084883c0'}, {'id': '17dafbabe49f20f8', 'threadId': '17dafbabe49f20f8'}, {'id': '17daf6cc33f853ce', 'threadId': '17daf6cc33f853ce'}, {'id': '17daa7acff368815', 'threadId': '17daa7acff368815'}, {'id': '17da64eb84c7abe6', 'threadId': '17da64eb84c7abe6'}, {'id': '17d9bb73dab5bb74', 'threadId': '17d9bb73dab5bb74'}, {'id': '17d9b27807f2c270', 'threadId': '17d9b27807f2c270'}, {'id': '17d96da56e30cfd1', 'threadId': '17d96da56e30cfd1'}, {'id': '17d8d4fcbd045871', 'threadId': '17d8d4fcbd045871'}, {'id': '17d833cb5c8d96f3', 'threadId': '17d833cb5c8d96f3'}, {'id': '17d7e1fae3dc52ab', 'threadId': '17d7e1fae3dc52ab'}, {'id': '17d77a1d4578fc6e', 'threadId': '17d77a1d4578fc6e'}, {'id': '17d5e6aa213dfc03', 'threadId': '17d5e6aa213dfc03'}, {'id': '17d58318680373f9', 'threadId': '17d58318680373f9'}, {'id': '17d5828ba23ef210', 'threadId': '17d5828ba23ef210'}, {'id': '17d4d9fb72346201', 'threadId': '17d4d9fb72346201'}], 'resultSizeEstimate': 31}
==============================
Dumping the messages and extracting urls in them...
Finished. Total messages count: 31
Dump messages to 2021-11-20 - 2022-01-01 label INBOX msgs.txt
Dump extracted urls to 2021-11-20 - 2022-01-01 label INBOX urls.txt
```

Here's how dumped urls file look like:
```
...
17d5828ba23ef210 extracted urls:https://github.com/epigone707/441f21/blob/975718e35ff745098adfc0b67e861aab29a1e49e/lab2/kotlinChatter/app/src/debug/res/values/google_maps_api.xml, 
17d4d9fb72346201 extracted urls:https://www.netflix.com?nftoken=BQAbAAEBEP4xDAkMbZez6ra0pXpqKAKAkFAas9Zpq54idfRWOl6o78UPXLXLpZhDuT0lV01m2l5OVmrYJaaNvy3K6YThc1Yvtws1zcO%2BofOUm5OpGoBDQ426j5urlspzLEhchPogDTdIHxE27%2FJpuD9KDSafteBSnXChc7Czdp9OPI58N6MqPA5jApm69g3WWtk%2F93bIj8ylVauf1aK4XLqFYVY3S7AbEg%3D%3D&lnktrk=EMP&g=9310EDDA1ECBA18C85A880EE7DFA5C83645592C7&lkid=URL_SIGNUP_CTA, https://www.netflix.com/ManageSubscriptions?id=BQE0AAEBEATrvPT2XXqVmmgKvb2ZjR%2BAkAot36WJeeik6PZiu%2FEKkCxDTZIS8Ig0OJnYXmxjjf%2B356p561lmy9SG3xYRAJNNK4zsm9c1OVH%2FiknucM%2B9CXr0crdMMfxnSfnKSV3XF1Crfn%2FdgZ19Tr4SbwzsDXhzLVeIujiQx0hZx3yDFyr4RnhVeouuSD2%2FXIlxglFBkIT3dISpPYLkGpJ13Sj6vBojNA%3D%3D&g=9310EDDA1ECBA18C85A880EE7DFA5C83645592C7&mid=49539558&nonm=true&lkid=URL_UNSUB&lnktrk=EMP, https://www.netflix.com/TermsOfUse?lnktrk=EMP&g=9310EDDA1ECBA18C85A880EE7DFA5C83645592C7&lkid=URL_TERMS, https://www.netflix.com/PrivacyPolicy?lnktrk=EMP&g=9310EDDA1ECBA18C85A880EE7DFA5C83645592C7&lkid=URL_PRIVACY, https://help.netflix.com/help?lnktrk=EMP&g=9310EDDA1ECBA18C85A880EE7DFA5C83645592C7&lkid=URL_HELP_3, 
Total messages count: 31
```

