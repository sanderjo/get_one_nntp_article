# get_one_nntp_article

Just get one nntp article ...

Probably only for debugging purposes.

And, yes, it uses NNTPS (not NNTP).

# usage

```
python3 get_one_nntp_article.py news.eweka.nl user123 MyPass '63561079zqpJFZVHYdeLFxZbCHHVIfi@aMBzkj'
```

# Result

Article and Body are written to corresponding files:

```
-rw-rw-r-- 1 sander sander 545469 Oct 27 20:40 'myarticle-news.eweka.nl-<63561079zqpJFZVHYdeLFxZbCHHVIfi@aMBzkj>.bin'
-rw-rw-r-- 1 sander sander 545091 Oct 27 20:40 'mybody-news.eweka.nl-<63561079zqpJFZVHYdeLFxZbCHHVIfi@aMBzkj>.bin'
```
