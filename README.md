# get_one_nntp_article

Just get one nntp article ...

Probably only for debugging purposes.

And, yes, it uses NNTPS (not NNTP).

# usage

```
python3 get_one_nntp_article.py news.eweka.nl user123 MyPass '63561079zqpJFZVHYdeLFxZbCHHVIfi@aMBzkj'
```

Notes about the article ID parameter:
* can be with and without < and >
* must be within single or double quotes because of funny chars like the @


# Result

Article and Body are written to corresponding files:

```
-rw-rw-r-- 1 sander sander 545469 Oct 27 20:40 'myarticle-news.eweka.nl-<63561079zqpJFZVHYdeLFxZbCHHVIfi@aMBzkj>.bin'
-rw-rw-r-- 1 sander sander 545091 Oct 27 20:40 'mybody-news.eweka.nl-<63561079zqpJFZVHYdeLFxZbCHHVIfi@aMBzkj>.bin'
```

# Bad things

No exception handling, so if something is wrong, you get a raw, self-explaining traceback, like

```
socket.gaierror: [Errno -2] Name or service not known
nntplib.NNTPPermanentError: 502 Authentication Failed
nntplib.NNTPTemporaryError: 430 No Such Article
```
