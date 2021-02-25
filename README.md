# Nickel Refineries

### Local Development

#### Installation

Note: depending on your local installation of Python you may have to replace `pip` with `pip3` in the commands below.


First install the web server [gunicorn](https://docs.gunicorn.org/en/stable/install.html). It is a Python package. 

After installing that you will need to install the additional Python libraries our app depends on. You can do this with 

```bash
pip install -r requirements.txt
```


#### Running

At the command prompt run (in this directory the same as `app.py`):

```bash
gunicorn app:server
```

If everything is installed and working correctly you should see output like:

```bash
[INFO] Starting gunicorn 20.0.4
[INFO] Listening at: http://127.0.0.1:8000 (9390)
[INFO] Using worker: sync
[INFO] Booting worker with pid: 9393
```

At this point you can view the app in your local web browser at http://localhost:8000/


#### Customization

* The `assets` folder contains a file called `favicon.ico` -- you can find and download customized favicons [here](https://www.favicon.cc/). Just replace the current favicon with a new one.
* Plotly Dash apps can only be viewed in a modern browser (like Chrome or Mozilla). They won't render in antediluvian browsers such as Microsoft.


### Deploying to Heroku

TODO
