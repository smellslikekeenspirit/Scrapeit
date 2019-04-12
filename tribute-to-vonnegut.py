from google.cloud import bigquery
from google.oauth2 import service_account
from pandas import*

# use your own credentials from bigquery.cloud.google.com

credentials = service_account.Credentials.from_service_account_file(
    'service-acc-creds.json')
project_id = 'coral-silicon-237417'
client = bigquery.Client(credentials= credentials,project=project_id)
query = """
  SELECT
  *
FROM
  `fh-bigquery.reddit.top25million` 
  WHERE REGEXP_CONTAINS(title, r'(?i)\bVonnegut\b') OR REGEXP_CONTAINS(title, r'(?i)\bKurt Vonnegut\b')
  ORDER BY score DESC;"""

query_job = client.query(query)
results = query_job.result().to_dataframe() 
print(results.to_string()) 
