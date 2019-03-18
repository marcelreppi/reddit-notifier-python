# reddit-notifier

A service that sends email notifications for reddit posts based on keywords for specified subreddits

## How to use

* Configure the ```subreddits.json``` file with the subreddits and keywords you want to track
* Configure the ```.env``` file with your mail provider's details

## Run on server

* Run ```python index.py```

## Serverless deployment

* Configure ```serverless.yml```
* Deploy lambda function via serverless ```sls deploy -v```
