# AppEngine
App Engine App

Root directory for app engine app:
app.yaml  -- application and web deployment configuration file
main.py -- main python file that is going to handle responses to my requests 
.template files -- Jinja applications 
base .template -- main template files: define our header and footer and leave free space in the middle for the content. Other templates will load the content in the middle depending on the page

1. On the Google Cloud Platform menu, click Activate Google Cloud Shell 
2. Clone the source code repository for a sample application called guestbook:
git clone https://github.com/GoogleCloudPlatform/appengine-guestbook-python
3. Run the application using the built-in App Engine development server.
dev_appserver.py ./app.yaml
The App Engine development server is now running the guestbook application in the local Cloud Shell. 
4. In Cloud Shell, click Web preview > Preview on port 8080 to preview the application.
5.Deploy the application to App Engine using this command:
gcloud app deploy ./index.yaml ./app.yaml
6. View the application on the Internet. The URL for your application is:
https://PROJECT_ID.appspot.com/
7. In the GCP Console, on the Products & Services () menu, click App Engine > Settings.
Click Disable application.

