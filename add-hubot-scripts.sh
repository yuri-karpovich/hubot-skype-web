#!/bin/bash

if [[ $HUBOT_SCRIPTS_URL ]] ; then
  curl -s $HUBOT_SCRIPTS_URL > /opt/hubot/hubot-scripts.json
fi
