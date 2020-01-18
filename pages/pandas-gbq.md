title: Pandas & Google Big Query
image: /static/pictures/pandas-gbq/pandas_logo.png
date: 2020-01-21

# Querying data from pandas for local analysis

I'm a big fan of the Google BigQuery (GBQ) platform, it's powerful, and relatively cheap for what it can do, in fact the first 10GB of storage per month is free along with the first 1 TB of query data processed per month (as of 2020-01-18). In fact it contains a lot of interesting public datasets which can be used, and analysed for practice, the storage costs for these datasets are completely free.

<img src="/static/pictures/pandas-gbq/gbq-pricing.png" alt="BigQuery Pricing" style="width:400px;display:block;margin-left:0;"/>

## Setting up the environment

To get started with BigQuery you need to [set up](https://cloud.google.com/gcp/getting-started/) your GCP account. BigQuery has a well-designed [web interface](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui), I'd encourage you to get a feel for BigQuery using the web UI and the query editor. The query editor has some [linting](https://code.visualstudio.com/docs/python/linting) capabilities, as well as a as code validator.

While GBQ is a fantastic cloud database, it's isn't appropriate for all of our data analysis needs, sometimes we want to get the data out of GBQ and into our python environment. [pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/) is designed for exactly this situation. Using your preferred [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) (conda can handle this too), install pandas gbq, using pip the command would be `pip install pandas-gbq`.

<img src="/static/pictures/pandas-gbq/gbq-screenshot.png" alt="BigQuery UI" style="width:400px;display:block;margin-left:0;"/>
## Security and Credentials

While the GBQ public datasets are available to anyone your personal datasets, or any business datasets you use need to be secured so that only authorised and credentialed people and [service accounts](https://cloud.google.com/iam/docs/understanding-service-accounts) can access sensitive data. This means that when we want to download data from GBQ we need to authories our application too. While this can be fiddly to set up for the first time, it's not too difficult to set up after you've done it once.  

There are a number of methods for authenticating using GBQ, and it can become a bit confusing however the documentation provides a useful [guide](https://pandas-gbq.readthedocs.io/en/latest/howto/authentication.html).  

I'm going to connect using the service account method. To do this we'll have to create a service account on [Google Cloud Platform](https://console.cloud.google.com/apis/credentials/serviceaccountkey). We have to make sure that the service account has the appropriate permissions to run a job on GBQ. I gave my service account the `BigQuery Job User`. When we're assigning permissions it's important to follow the principle of least privilege. The principle of least privilege is the idea that at any user, program, or process should have only the bare minimum privileges necessary to perform its function. The idea behind this is that if the credentials are compromised either by accident or by malicious activity, this reduced the amount of harm that can be caused.

## Code

The python code to actually download from GBQ is then relatively straightforward.

```[python]
import pandas as pd
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('./private-key.json')

df = pd.read_gbq(
    query=baseball_query,
    project_id='pandas-gbq-example-project',
    credentials=credentials)
```

The full jupyter notebook showing this code can be found [here](https://github.com/jaspajjr/pandas-gbq-example).

## Debugging

Hopefully this step isn't required, but when learning a new technology I usually trip over something unexpected. If I bump into trouble with downloading data from GBQ, my issue is usually related to the permissions for the service account I've created. If you bump into any issues let me know on twitter and I'll add to this section.
