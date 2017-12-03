#!/bin/bash

 NAME="Todo"                                  # Name of the application
 DJANGODIR=/home/xavier/Prog/django/Todo             # Django project directory
 SOCKFILE=/home/xavier/Prog/django/run/gunicorn_todo.sock  # we will communicte using this unix socket
 USER=xavier                                        # the user to run as
 GROUP=xavier                                    # the group to run as
 NUM_WORKERS=2                                     # how many worker processes should Gunicorn spawn
 DJANGO_SETTINGS_MODULE=todo.settings             # which settings file should Django use
 DJANGO_WSGI_MODULE=todo.wsgi                     # WSGI module name

 echo "Starting $NAME as `whoami`"

 # Activate the virtual environment
 cd $DJANGODIR
 source ../todo_venv/bin/activate
 export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
 export PYTHONPATH=$DJANGODIR:$PYTHONPATH

 # Create the run directory if it doesn't exist
 RUNDIR=$(dirname $SOCKFILE)
 test -d $RUNDIR || mkdir -p $RUNDIR

 # Start your Django Unicorn
 # Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
  exec ./venv3/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
       --name $NAME \
       --workers $NUM_WORKERS \
       --timeout=150 \
       --user=$USER \
       --group=$GROUP \
       --bind=unix:$SOCKFILE \
       --log-level=debug \
       --log-file=-
