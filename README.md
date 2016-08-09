disciplinereport
=============

## Dependencies

To work with this project locally you will need the following software:

**[Homebrew](http://brew.sh/)**

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    #Verify installation:
    brew --version

**[PIP](https://pip.pypa.io/en/latest/installing.html)**    

    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
    #Verify installation:
    pip --version

**[Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)**    

    pip install virtualenv
    #Verify installation:
    virtualenv --version

**libmemcached**

    brew install libmemcached

**postgresql**
    
    #Note -- this is only needed if you're connecting to the production database. 
    #You should be be able to use sqlite to work locally. 
    #See disciplinereport/settings/local.py for local settings.
    brew install postgresql

# Quickstart

### Installation

The first time you set up the project, run the following commands:
    
    git clone git@github.com:ninapavlich/disciplinereport.git
    cd disciplinereport
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate

    python manage.py loaddata disciplinereport/fixtures/core.json #Note this may take several minutes to complete...
    
    python manage.py runserver

To connect to the Heroku project:
    
    #Ensure you have access to the Heroku project

    #Install the heroku toolbelt: https://toolbelt.heroku.com/
    #Once installed, log in to your Heroku account
    heroku login

    #Link disciplinereport folder with heroku project:
    heroku git:remote -a disciplinereport
    
    #To push to heroku
	#Production:    
    git push heroku master

    #Staging:    
    git push heroku staging:master

The next time you return to the project:
    
    cd disciplinereport
    source venv/bin/activate

    #{{branch}} is whatever branch you're working on; probably staging
    git pull origin {{branch}}
    
    #If you see changes to requirements.txt
    source venv/bin/activate
    pip install -r requirements.txt

    #If you see new migrations
    python manage.py migrate

    python manage.py runserver
    

To commit changes and push them to bitbucket:
    
    #{{branch}} is whatever branch you're working on; probably staging
    git commit -am 'Message about what has changed'
    git push origin {{dev}}


Dump a database fixture:

	python manage.py dumpdata --natural-foreign --indent=4 -e sessions -e admin -e contenttypes -e auth.Permission > disciplinereport/fixtures/backup.json

    
Dump the a configuration file fixture:

	python manage.py dumpdata core form -e form.formentry -e form.fieldentry -e core.menuitem --natural-foreign --indent=4 > disciplinereport/fixtures/configuration.json

Load a database fixture:

    python manage.py loaddata disciplinereport/fixtures/backup.json

Dump a data file fixture:

    python manage.py dumpdata data.schooldistrict data.schooldistrictdatum --natural-foreign --indent=4 > disciplinereport/fixtures/data.json

