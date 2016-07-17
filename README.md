# hubot-hipchat

Hubot Hipchat bot running out of docker. By default this images sets up a stock,
or close to stock hubot which can be connected to Hipchat.

You can install apps from the Scripts Catalog ( http://hubot-script-catalog.herokuapp.com/ )
By passing in the HUBOT_SCRIPTS_URL environment variable. The URL should point to a valid hubot-scripts.json file.

```Shell
docker run -it -d -e "SERVICE_NAME=hipchat" -e HUBOT_HIPCHAT_JID=<JID>@chat.hipchat.com -e HUBOT_HIPCHAT_PASSWORD='<PW>' -e HUBOT_AUTH_ADMIN="Your Name" -e HUBOT_SCRIPTS_URL="https://gist.githubusercontent.com/tfhartmann/26325695994220a26a4e/raw/d852fb4735726474c20bb4a414693837ce464596/hubot-scripts.json" tfhartmann/hubot-hipchat
```

##  environment variables
### HUBOT_HIPCHAT_JID
HipChat Jabber ID For your hubot users. It should look something like this `123456_123456@chat.hipchat.com`

### HUBOT_HIPCHAT_PASSWORD
Password for the above Jabber ID

### HUBOT_SCRIPTS_URL
URL to a valid JSON Array with the names of coffee scripts that exist in [hubot-scripts](https://github.com/github/hubot-scripts/tree/master/src/scripts).
At it's most basic this just updates the hubot-scripts.json file, loading any scripts thata already exist on the disk into the running bot.

Example:
`[ "uptime.coffee", "redis-brain.coffee", "shipit.coffee" ]`


### HUBOT_PACKAGE_URL
URL to a valid JSON array with the names of node hubot script packages.  This is an attempt to allow users to install packages that are deployed via a [script package](https://github.com/hubot-scripts) at its most basic this will loop through all the packages listed in the array, install them on your hubot with `npm install <package> --save` and then update the external-scripts.json file.  

## Examples

### `Basic Example`
Run a basic hubot

```Shell
docker run -it -d -e "SERVICE_NAME=hipchat" -e HUBOT_HIPCHAT_JID=<JID>@chat.hipchat.com -e HUBOT_HIPCHAT_PASSWORD='<PW>' -e HUBOT_AUTH_ADMIN="Your Name" -e HUBOT_SCRIPTS_URL="https://gist.githubusercontent.com/tfhartmann/26325695994220a26a4e/raw/d852fb4735726474c20bb4a414693837ce464596/hubot-scripts.json" tfhartmann/hubot-hipchat
```


### `Install with Packages`
Run a puppet server and mount your own /etc/puppet directory for testing. Keeping in mind this will
overwrite any config file in /etc/puppet with (puppet.conf, auth.conf, and fileserver.conf etc) with
whatever you have in your local directory.

```Shell
docker run -it -d -e HUBOT_HIPCHAT_JID=<JID>@chat.hipchat.com -e HUBOT_HIPCHAT_PASSWORD='<PW>' -e HUBOT_SCRIPTS_URL='https://raw.githubusercontent.com/tfhartmann/hubot-packages/master/hubot-scripts.json'  -e HUBOT_PACKAGE_URL='https://raw.githubusercontent.com/tfhartmann/hubot-packages/master/external-scripts.json'  tfhartmann/hubot-hipchat
```
