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

# Model
* Write unit tests for at least 3 functions in the model code.

# API Creation
*  Create a RESTful API using FastAPI this must implement:
    * GET on the root giving a welcome message.
    * POST that does model inference.
    * Type hinting must be used.
    * Use a Pydantic model to ingest the body from POST. This model should contain an example.
   	 * Hint: the data has names with hyphens and Python does not allow those as variable names. Do not modify the column names in the csv and instead use the functionality of FastAPI/Pydantic/etc to deal with this.
* Write 3 unit tests to test the API (one for the GET and two for POST, one that tests each prediction).

# API Deployment
* Create a free Heroku account (for the next steps you can either use the web GUI or download the Heroku CLI).
* Create a new app and have it deployed from your GitHub repository.
    * Enable automatic deployments that only deploy if your continuous integration passes.
    * Hint: think about how paths will differ in your local environment vs. on Heroku.
    * Hint: development in Python is fast! But how fast you can iterate slows down if you rely on your CI/CD to fail before fixing an issue. I like to run flake8 locally before I commit changes.
* Write a script that uses the requests module to do one POST on your live API.
