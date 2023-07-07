# gcp-cloud-functions
begin with the GCP cloud functions


## Install required packages 
```
pip install -r requirements.txt
```
## deploying our function
First, we have to set our project using
```
gcloud config set project [YOUR_PROJECT_ID]
```

then, we deploy out=r func with 
```
gcloud functions deploy [FUNC_NAME] --runtime python37 --trigger-http
```