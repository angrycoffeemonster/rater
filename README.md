rater
=====

An app for rating things like New York restaurants.


# Basics

## Getting the repo

To clone the repo, do the following:

```
  git clone git@github.com:jonroberts/rater.git
```
I've set both of you up as users, so that should work. If you want to set up an ssh key (so you don't have to provide a password for every pull/push request) then [follow this](https://help.github.com/articles/generating-ssh-keys) and send me the public key. I'll get that added in.

## Setting up virtualenv

```
virtualenv venv
```

Then activate the virtualenv python:

```
. venv/bin/activate
```

Once you've done that, install the packages:

```
pip install django -upgrade
pip install numpy
pip install django-tastypie
pip install south
```

The last two are optional at the moment, but they'll probably come in handy. We can, and should, install a bunch of pre-build django libraries for things like user-login etc when we get round to that being relevant.

I'm using Django 1.6.2 here.

## Setting up the app

I followed the core tutorial [here](https://docs.djangoproject.com/en/1.6/intro/tutorial01/) to set up the basic app.

If you've cloned the app locally, you'll need to create a settingLocal.py. Ping me and I'll send over the format. It's the file that has the database name and passwords in it. This is not uploaded to github, and is also different for each place the app is installed. I'm running the dev version against a mysql backend, but it can just as easily be run using a local sqlite database.

Set up the database (follow the tutorial, and set up the database settings)

Then run:
```
  python manage.py syncdb
```

This will set you up with a super-user and a few other things. This will give you a login user for the app.

