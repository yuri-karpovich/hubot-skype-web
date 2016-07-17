# hubot-skype-web

Hubot Skype bot running out of docker. By default this images sets up a stock,
or close to stock hubot which can be connected to Skype.

You can install apps from the Scripts Catalog ( http://hubot-script-catalog.herokuapp.com/ )
By passing in the HUBOT_SCRIPTS_URL environment variable. The URL should point to a valid hubot-scripts.json file.


##  environment variables
### HUBOT_SKYPE_USERNAME
Skype-web username

### HUBOT_SKYPE_PASSWORD
Skype-web username password

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
docker run -it  --net='host' -e "SERVICE_NAME=skype" -e HUBOT_SCRIPTS_URL="https://gist.githubusercontent.m/tfhartmann/26325695994220a26a4e/raw/d852fb4735726474c20bb4a414693837ce464596/hubot-scripts.json" -e HUBOT_SKYPE_USERNAME='user' -e HUBOT_SKYPE_PASSWORD='password' spoonest/hubot-skype-web
```

## Thanks
Thanks to @tfhartmann for https://github.com/tfhartmann/hubot-hipchat repository.
