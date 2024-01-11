import streamlit as st
from google.cloud import bigquery

# Set your GCP project ID
project_id = 'q-gcp-00863-fsihackathon-23-12'

# Set your BigQuery dataset and table
dataset_id = 'nba_synthesizer_forecast_modifier'
table_id = 'forecasted_output_firstpass'

# Create a BigQuery client
client = bigquery.Client(project=project_id)

# Query to retrieve data from BigQuery table
query = f'SELECT * FROM `{project_id}.{dataset_id}.{table_id}`'

# Execute the query
query_job = client.query(query)

# Fetch the results
results = query_job.result()

# Display the results in Streamlit
st.write("## BigQuery Table Contents:")
for row in results:
    st.write(row)

st.write('hello')
