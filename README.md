# gmailSaver

The gmailSaver can download emails from a gmail account by using Gmail API and extract all url links in them.

# Usage
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
After you've done, download the credential file and name it as `credentials.json` . You can then Run:

```
python gmailUrlExtract.py
```

Gmail API will then ask you to log in a gmail account and give permission. After that, `token.json` will be created automatically when the authorization flow completes. You can then view the output for `gmailUrlExtract.py`. It will first print all labels in your gmail account:

```
Labels:
{'id': 'CHAT', 'name': 'CHAT', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}
{'id': 'SENT', 'name': 'SENT', 'type': 'system'}
{'id': 'INBOX', 'name': 'INBOX', 'type': 'system'}
{'id': 'IMPORTANT', 'name': 'IMPORTANT', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 
'system'}
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
...
```
Then it will print all messages in a specified label id. Here, I choose the 'testLabel' with id 'Label_7090689821639516814'. There're only three messages in this label:
```
...
==============================
Enter the label Id you want to scrape: Label_7090689821639516814
print all messages info in label:  Label_7090689821639516814
{'messages': [{'id': '17ca398c3246183d', 'threadId': '17ca398c3246183d'}, {'id': '179eb8d36ae69e8b', 'threadId': '179eb8d36ae69e8b'}, {'id': '178d983e8a8fd203', 'threadId': '178d983e8a8fd203'}], 'resultSizeEstimate': 3}
msg id:  17ca398c3246183d
msg id:  179eb8d36ae69e8b
msg id:  178d983e8a8fd203
==============================
...
```
Finally, it will print the extracted urls of all messages in the specified label id:

```
################ msg:  17ca398c3246183d  ################

extracted urls:
['https://github.com/epigone707', 'https://cse.engin.umich.edu/academics/undergraduate/computer-science-eng/']

################ msg:  179eb8d36ae69e8b  ################

extracted urls:
['http://url9969.lezhin.com/ls/click?upn=4ZwTYcUSMjfUPPRT3IBbQyBL8JJt1JlbmERQp0r-2FOmB3AJ7H7k-2Flp8Nnf-2F0r6uFVQZ7H_-2FXmyPErK4HGQx3x8wFtbh4Dt18-2BheXWPIAct0uj75l6daMwvgeNJ1yMPC2Xcv3pH4hKDsr-2BmaRdaAQgimx7zVbOPZUCO8Rso0hAkw5QBv3s1S6VYEEPfy1x7Z2k1Wc8AcrcIRsviMa-2BnF2xbZpJuDiHkZ8cuXPr4CV3fs2w0fbu5rmGDuSt4eO3hs5Mx0etd93BYZVQ81pT5KsGmxamJLA-3D-3D', 'http://url9969.lezhin.com/ls/click?upn=4ZwTYcUSMjfUPPRT3IBbQyBL8JJt1JlbmERQp0r-2FOmDxeg9iTr0PyaEiaCP-2Bzfx2NatDfYYGt295re7tlrOV9w-3D-3Dhxav_-2FXmyPErK4HGQx3x8wFtbh4Dt18-2BheXWPIAct0uj75l6daMwvgeNJ1yMPC2Xcv3pHuPI2JzwfneIVbT4GB1-2Fg97rOT65x3H4NDNBKCHLvEiUn5DTrpg5ObbvF-2B4KagEjHeR0GvoCRvfaxJRMBCk4S7ksmSBYRTPtVLXRkTSXQ7plHe9CrY011wWIMJ25JCWKkxQBy4SpVqGVJ64nQ3jmKtA-3D-3D', 'http://url9969.lezhin.com/ls/click?upn=4ZwTYcUSMjfUPPRT3IBbQyBL8JJt1JlbmERQp0r-2FOmDcOr8zBnpc-2FLwM50E3aTEBHRRAJLPUZbeCdlJhT6yQiw-3D-3Dz1u4_-2FXmyPErK4HGQx3x8wFtbh4Dt18-2BheXWPIAct0uj75l6daMwvgeNJ1yMPC2Xcv3pHRR-2FENmlu-2BHyqwBOPBkZJzKRb3-2FmVSMHjoQARomqqPXkDoe0uqHswxFKBNV4JXnidCtprXo3jd3UHK786Ke0fYJ9AyvzKUSxqpGkwQEJuWN-2BlNUBFjVBkGjmNhMPKkdsQ7LRAli3-2B-2FM-2FB6s3zBIFFTA-3D-3D', 'http://url9969.lezhin.com/ls/click?upn=4ZwTYcUSMjfUPPRT3IBbQyBL8JJt1JlbmERQp0r-2FOmD3d-2FkfpAtb2Dih-2FGVgDPLNd-2FWtSYEgE4hRLfLD9OXhBQ-3D-3DIBEB_-2FXmyPErK4HGQx3x8wFtbh4Dt18-2BheXWPIAct0uj75l6daMwvgeNJ1yMPC2Xcv3pHf9-2BPNVsj1cZUaK4o9GbJ0s6FAOEYP08rSH-2FXQjGMI53VMADF7-2F8-2B6gA1-2Bag4myUclDKeoGkz6gDeWwbsFvS0hbJZks4ElrbTyEqY9ZSzbZzpXe-2BvMleqN-2FIXECFy19cu-2FsvcRKhVv4IAl8dj7WnhHQ-3D-3D', 'http://url9969.lezhin.com/ls/click?upn=4ZwTYcUSMjfUPPRT3IBbQ1XndouXzYuAj9DKRxkbc9qHMivtOwNUDUaYbEksvZ5Bm_9f_-2FXmyPErK4HGQx3x8wFtbh4Dt18-2BheXWPIAct0uj75l6daMwvgeNJ1yMPC2Xcv3pHRr8qVy-2FGhRwKEkafGY7X1eOFLZY4aB3y4LI2g8KmtxN8LeGmduZgtSzLG0MYhH2q4txT3fmQdxnfEvHXS13aVHJe5DZ5Hapam0Ka4wKCCHDKGu84GJHyy8w0dJ57vf0lK6g6v7UNOXasrtYCpNBERw-3D-3D', 'http://url9969.lezhin.com/ls/click?upn=4ZwTYcUSMjfUPPRT3IBbQyBL8JJt1JlbmERQp0r-2FOmAQWVVxubi-2BnCmgnLE4noHXOe8pyVR4IZzsxEYvreD3vA-3D-3DNS8q_-2FXmyPErK4HGQx3x8wFtbh4Dt18-2BheXWPIAct0uj75l6daMwvgeNJ1yMPC2Xcv3pHBcYBLcTyA42M8jp9RfEHajVzBXgmew42vuppmRWHiX3TEyqT12sAQ-2B8nCMAPQw8HZmd1yGJRa8BoS0hu-2BTOALnyHDxJxn06dTJzn-2BaipFxFcAqk240A4OEBPUcBXSfiILAVHeoo2-2BF5GvJbe9WQRxg-3D-3D', 'http://url9969.lezhin.com/ls/click?upn=4ZwTYcUSMjfUPPRT3IBbQyBL8JJt1JlbmERQp0r-2FOmCCc3XcmwAGkMfqZKv23h484MHS2bipf-2FVGJO-2F8mUacfwCQ4RqPhBUKK2IElPyYfk4-3DTtkk_-2FXmyPErK4HGQx3x8wFtbh4Dt18-2BheXWPIAct0uj75l6daMwvgeNJ1yMPC2Xcv3pHNwYauoJiK3SjtXqv-2Feyc9RHEGZaT5AOWigMsif4OIUVmSXmIO2X-2Bys2Ze-2Bxrrs-2FLRnH7LjLWo8VxqZQailQ-2BL6e6PSgk-2FSaJaZs41sYfkietLsf3FB380puzXDcji1P7GhVGoPt1-2FQGeUs-2FKn2DqcA-3D-3D']

################ msg:  178d983e8a8fd203  ################

extracted urls:
['https://medium.com/@yanfuguo2000?source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://medium.com/plans?source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://medium.com/me/following/suggestions?source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://medium.com/@kubut?source=email-55bf5f0cf5f2-1618542940248-digest.reader-d0b105d10f0a-19a41ba70411----0-73------------------2658d360_1576_4235_ae23_6a3dd26dc89a-1-142f9a7f_4db4_464a_93e0_07b1ce4d7380', 'https://medium.com/better-programming?source=email-55bf5f0cf5f2-1618542940248-digest.reader-d0b105d10f0a-19a41ba70411----0-73------------------2658d360_1576_4235_ae23_6a3dd26dc89a-1-142f9a7f_4db4_464a_93e0_07b1ce4d7380', 'https://medium.com/@vj0809?source=email-55bf5f0cf5f2-1618542940248-digest.reader-5517fd7b58a6-ed9b90a96355----1-73------------------2658d360_1576_4235_ae23_6a3dd26dc89a-1-142f9a7f_4db4_464a_93e0_07b1ce4d7380', 'https://medium.com/gitconnected?source=email-55bf5f0cf5f2-1618542940248-digest.reader-5517fd7b58a6-ed9b90a96355----1-73------------------2658d360_1576_4235_ae23_6a3dd26dc89a-1-142f9a7f_4db4_464a_93e0_07b1ce4d7380', 'https://medium.com/@kbandersen?source=email-55bf5f0cf5f2-1618542940248-digest.reader-ae2a65f35510-1bb82e1da6----2-73------------------2658d360_1576_4235_ae23_6a3dd26dc89a-1-142f9a7f_4db4_464a_93e0_07b1ce4d7380', 'https://medium.com/gen?source=email-55bf5f0cf5f2-1618542940248-digest.reader-ae2a65f35510-1bb82e1da6----2-73------------------2658d360_1576_4235_ae23_6a3dd26dc89a-1-142f9a7f_4db4_464a_93e0_07b1ce4d7380', 'https://medium.com/@dan-hansen?source=email-55bf5f0cf5f2-1618542940248-digest.reader-d1f54550947b-a112e0bff13d----3-73------------------2658d360_1576_4235_ae23_6a3dd26dc89a-1-142f9a7f_4db4_464a_93e0_07b1ce4d7380', 'https://medium.com/macoclock?source=email-55bf5f0cf5f2-1618542940248-digest.reader-d1f54550947b-a112e0bff13d----3-73------------------2658d360_1576_4235_ae23_6a3dd26dc89a-1-142f9a7f_4db4_464a_93e0_07b1ce4d7380', 'https://medium.com/@rae-gomes?source=email-55bf5f0cf5f2-1618542940248-digest.reader-e4206a871598-370a9cb8f654----0-72------------------2658d360_1576_4235_ae23_6a3dd26dc89a-28-', 'https://medium.com/acid-sugar?source=email-55bf5f0cf5f2-1618542940248-digest.reader-e4206a871598-370a9cb8f654----0-72------------------2658d360_1576_4235_ae23_6a3dd26dc89a-28-', 'https://medium.com/@karennimmo?source=email-55bf5f0cf5f2-1618542940248-digest.reader-de4b53c10bc7-75e1d5bbc2ae----1-72------------------2658d360_1576_4235_ae23_6a3dd26dc89a-28-', 'https://medium.com/on-the-couch?source=email-55bf5f0cf5f2-1618542940248-digest.reader-de4b53c10bc7-75e1d5bbc2ae----1-72------------------2658d360_1576_4235_ae23_6a3dd26dc89a-28-', 'https://medium.com/@michael-thompson?source=email-55bf5f0cf5f2-1618542940248-digest.reader-2bd10c577f94-da8ac2013349----2-72------------------2658d360_1576_4235_ae23_6a3dd26dc89a-28-', 'https://medium.com/simple-pub?source=email-55bf5f0cf5f2-1618542940248-digest.reader-2bd10c577f94-da8ac2013349----2-72------------------2658d360_1576_4235_ae23_6a3dd26dc89a-28-', 'https://medium.com/@hakluke?source=email-55bf5f0cf5f2-1618542940248-digest.reader--cb96597b6cc4----0-59------------------2658d360_1576_4235_ae23_6a3dd26dc89a-16-fdab7a6c_0314_44bb_b0b3_25fc7ce6a266', 'https://medium.com/@krishbhanushali?source=email-55bf5f0cf5f2-1618542940248-digest.reader-61061eb0c96b-86c70dada52d----1-59------------------2658d360_1576_4235_ae23_6a3dd26dc89a-16-fdab7a6c_0314_44bb_b0b3_25fc7ce6a266', 'https://medium.com/codeburst?source=email-55bf5f0cf5f2-1618542940248-digest.reader-61061eb0c96b-86c70dada52d----1-59------------------2658d360_1576_4235_ae23_6a3dd26dc89a-16-fdab7a6c_0314_44bb_b0b3_25fc7ce6a266', 'https://medium.com/@vickieli?source=email-55bf5f0cf5f2-1618542940248-digest.reader-f5af2b715248-383266799832----2-59------------------2658d360_1576_4235_ae23_6a3dd26dc89a-16-fdab7a6c_0314_44bb_b0b3_25fc7ce6a266', 'https://medium.com/swlh?source=email-55bf5f0cf5f2-1618542940248-digest.reader-f5af2b715248-383266799832----2-59------------------2658d360_1576_4235_ae23_6a3dd26dc89a-16-fdab7a6c_0314_44bb_b0b3_25fc7ce6a266', 'https://medium.com/@whitson.gordon?source=email-55bf5f0cf5f2-1618542940248-digest.reader-444d13b52878-b4e24f8e8a----0-50----------d4e7f4144ac5--------2658d360_1576_4235_ae23_6a3dd26dc89a-12-', 'https://medium.com/one-zero?source=email-55bf5f0cf5f2-1618542940248-digest.reader-444d13b52878-b4e24f8e8a----0-50----------d4e7f4144ac5--------2658d360_1576_4235_ae23_6a3dd26dc89a-12-', 'https://medium.com/@lizbrody0?source=email-55bf5f0cf5f2-1618542940248-digest.reader-444d13b52878-ac6da1408fba----1-50----------d4e7f4144ac5--------2658d360_1576_4235_ae23_6a3dd26dc89a-12-', 'https://medium.com/one-zero?source=email-55bf5f0cf5f2-1618542940248-digest.reader-444d13b52878-ac6da1408fba----1-50----------d4e7f4144ac5--------2658d360_1576_4235_ae23_6a3dd26dc89a-12-', 'https://medium.com/@thetechtutor?source=email-55bf5f0cf5f2-1618542940248-digest.reader--4aca5b3ffee----2-50----------d4e7f4144ac5--------2658d360_1576_4235_ae23_6a3dd26dc89a-12-', 'https://medium.com/@aliciamccauley?source=email-55bf5f0cf5f2-1618542940248-digest.reader-544c7006046e-d429a37f0a2d----0-62----------6b39042c05cc--------2658d360_1576_4235_ae23_6a3dd26dc89a-21-', 'https://medium.com/human-parts?source=email-55bf5f0cf5f2-1618542940248-digest.reader-544c7006046e-d429a37f0a2d----0-62----------6b39042c05cc--------2658d360_1576_4235_ae23_6a3dd26dc89a-21-', 'https://medium.com/@clarech?source=email-55bf5f0cf5f2-1618542940248-digest.reader-544c7006046e-124be1b80907----1-62----------6b39042c05cc--------2658d360_1576_4235_ae23_6a3dd26dc89a-21-', 'https://medium.com/human-parts?source=email-55bf5f0cf5f2-1618542940248-digest.reader-544c7006046e-124be1b80907----1-62----------6b39042c05cc--------2658d360_1576_4235_ae23_6a3dd26dc89a-21-', 'https://medium.com/@meghandaum?source=email-55bf5f0cf5f2-1618542940248-digest.reader-3f6ecf56618-c204af037d37----0-13------------------2658d360_1576_4235_ae23_6a3dd26dc89a-6-', 'https://medium.com/forge?source=email-55bf5f0cf5f2-1618542940248-digest.reader-3f6ecf56618-c204af037d37----0-13------------------2658d360_1576_4235_ae23_6a3dd26dc89a-6-', 'https://medium.com/@tarahaelle?source=email-55bf5f0cf5f2-1618542940248-digest.reader-8d6b8a439e32-69015afe0296----1-13------------------2658d360_1576_4235_ae23_6a3dd26dc89a-6-', 'https://medium.com/elemental-by-medium?source=email-55bf5f0cf5f2-1618542940248-digest.reader-8d6b8a439e32-69015afe0296----1-13------------------2658d360_1576_4235_ae23_6a3dd26dc89a-6-', 'https://medium.com/@casiracopes?source=email-55bf5f0cf5f2-1618542940248-digest.reader-9dc80918cc93-18cfa53b5219----2-13------------------2658d360_1576_4235_ae23_6a3dd26dc89a-6-', 'https://medium.com/the-movement-blog?source=email-55bf5f0cf5f2-1618542940248-digest.reader-9dc80918cc93-18cfa53b5219----2-13------------------2658d360_1576_4235_ae23_6a3dd26dc89a-6-', 'https://medium.com/me/missioncontrol?source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://medium.com/?source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://medium.com/me/email-settings/55bf5f0cf5f2/dbbd3d3aa2b?type=social&source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://medium.com/me/email-settings/55bf5f0cf5f2/dbbd3d3aa2b?type=social&preference=2&source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://help.medium.com/hc/en-us?source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a', 'https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=email-55bf5f0cf5f2-1618542940248-digest.reader-------------------------2658d360_1576_4235_ae23_6a3dd26dc89a']
```
