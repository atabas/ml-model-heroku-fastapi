# Environment Set up
* conda create -n [envname] "python=3.8" scikit-learn dvc pandas numpy pytest jupyter jupyterlab fastapi uvicorn -c conda-forge
* Install git either through conda (“conda install git”) or through your CLI, e.g. sudo apt-get git.

## Repositories
* Create a directory for the project and initialize git and dvc.
    * As you work on the code, continually commit changes. Generated models you want to keep must be committed to dvc.

## Setup S3
* In your CLI environment install the AWS CLI tool.
* In the navigation bar in the Udacity classroom select Open AWS Gateway and then click Open AWS Console. You will not need the AWS Access Key ID or Secret Access Key provided here.
* From the Services drop down select S3 and then click Create bucket.
* Give your bucket a name, the rest of the options can remain at their default.
* To use your new S3 bucket from the AWS CLI you will need to create an IAM user with the appropriate permissions:
    * Sign in to the IAM console here or from the Services drop down on the upper navigation bar.
    * In the left navigation bar select Users, then choose Add user.
    * Give the user a name and select Programmatic access.
    * In the permissions selector, search for S3 and give it AmazonS3FullAccess
    * Tags are optional and can be skipped.
    * After reviewing your choices, click create user.
    * Configure your AWS CLI to use the Access key ID and Secret Access key.
        * aws configure import --csv file://../Downloads/new_user_credentials.csv

## GitHub Actions
* Setup GitHub Actions on your repository. At a minimum it runs pytest and flake8 on push and requires both to pass without error.
* Make sure you set up the GitHub Action to have the same version of Python as you used in development.
* Add your AWS credentials to the Action.
* Set up DVC in the action and specify a command to dvc pull.

# Data
* Download census.csv and commit it to dvc:
    * git rm -r --cached 'starter/data/census.csv'
    *  git commit -m "stop tracking starter data census.csv"
    * dvc add starter/data/census.csv
    * dvc remote modify --local myremote access_key_id name1
    * dvc remote modify --local myremote secret_access_key name2
    * dvc push --remote myremote
* This data is messy, try to open it in pandas and see what you get.
* To clean it, use your favorite text editor to remove all spaces:
    * cat starter/data/census.csv | tr -d "[:blank:]" >> starter/data/census_nospace.csv
* Commit this modified data to dvc (we often want to keep the raw data untouched but then can keep updating the cooked version):
    * dvc add starter/data/census_nospace.csv
    * dvc push --remote myremote

# API Creation
* Run python starter/main.py to start the API:
    * Try out the prediction endpoint from http://127.0.0.1:8000/docs#/default/predict_predict_post
* 3 unit tests to test the API (one for the GET and two for POST, one that tests each prediction) are in starter/main_test.py.

# API Deployment
* Create a new app and have it deployed from your GitHub repository.
    - Set up a Procfile, configure New app from Heroku dashboard, select Python buildpack and change paths in app
* Write a script that uses the requests module to do one POST on your live API.
