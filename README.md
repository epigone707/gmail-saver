# gmail-saver

The gmailSaver can download emails from a gmail account by using Gmail API and extract all url links in them.

# Usage
You need to follow [gmail API tutorial](https://developers.google.com/gmail/api/quickstart/python) which will teach you how to get a credential. After you've done, you will have `credentials.json` together with `gmailUrlExtract.py` in your local folder. You can then Run:

```
python gmailUrlExtract.py
```

Gmail API will then ask you to log in a gmail account and give permission. After that, `token.json` will be created automatically when the authorization flow completes. You can then view the output for `gmailUrlExtract.py`:

```
################ msg:  17ca398c3246183d  ################


extracted urls:
['https://github.com/epigone707', 'https://cse.engin.umich.edu/academics/undergraduate/computer-science-eng']

################ finish:  17ca398c3246183d  ################


################ msg:  179eb8d36ae69e8b  ################


extracted urls:
['gmail.com', 'http://url9969.lezhin.com/ls/click', 'http://url9969.lezhin.com/ls/click', 'http://url9969.lezhin.com/ls/click', 'http://url9969.lezhin.com/ls/click', 'lezhin.com', 'http://url9969.lezhin.com/ls/click', 'http://url9969.lezhin.com/ls/click', 'http://url9969.lezhin.com/ls/click', 'lezhin.com']

################ finish:  179eb8d36ae69e8b  ################


################ msg:  178d983e8a8fd203  ################


extracted urls:
['https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/plans', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/me/following/suggestions', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/better-programming', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/gitconnected', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 
'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/gen', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/macoclock', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/acid-sugar', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/on-the-couch', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/simple-pub', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/codeburst', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/swlh', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'whitson.gordon', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/one-zero', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/one-zero', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/human-parts', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/human-parts', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/forge', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/elemental-by-medium', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/the-movement-blog', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/me/missioncontrol', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/me/email-settings/55bf5f0cf5f2/dbbd3d3aa2b', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/me/email-settings/55bf5f0cf5f2/dbbd3d3aa2b', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://help.medium.com/hc/en-us', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://policy.medium.com/medium-privacy-policy-f03bf92035c9', 'email-55bf5f0cf5f2-1618542940248-digest.reader', 'https://policy.medium.com/medium-terms-of-service-9db0094a1e0f', 'email-55bf5f0cf5f2-1618542940248-digest.reader']

################ finish:  178d983e8a8fd203  ################
```
