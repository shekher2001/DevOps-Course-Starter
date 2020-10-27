# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
```bash
$ source setup.sh
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Notes

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like developement mode (which also enables features like hot reloading when you make a file change).
* There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

When running `setup.sh`, the `.env.template` file will be copied to `.env` if the latter does not exist.

Following is the link of Trello account 

https://trello.com/b/smcVvamd/book-lib 

Details below for the trello boards details:

BOARD_ID=5f58a4a02301b638351b3bce
KEY=f16aee2c005a4d41c2e7252416e20a9a
TOKEN=0b8ca8a685ea8c7ef812f92680257233f9eabe98da53afa83762db4e86a41666
LISTDO=5f58a4a10ca5a331359ddba3
LISTDONE=5f58a4a10b7b403852fbeace

