# ll 
python -V
curl https://sdk.cloud.google.com | bash
sudo snap install google-cloud-cli --classic
gcloud init
git clone https://github.com/GoogleCloudPlatform/python-docs-samples
 cd python-docs-samples/appengine/standard/hello_world
dev_appserver.py app.yml
Ctrl + C .
gcloud app deploy
