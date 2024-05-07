# twitter-stock-analysis

Function that uses twitter data to evaluate the stock of certain companies

## Installantion
Use pip to install the required packages

```bash
pip install -r requirements.txt
```

Use conda to install the required packages

```bash
conda install --file requirements.txt
```
## Runbook
To run this you need a file inside of `./src` called `.env`

you can get your own reddit script details by going to the [reddit apps page](https://www.reddit.com/prefs/apps)
and clicking "Create Another App"

```
SECRET_REDDIT_KEY = 'secret key for a reddit script application'
CLIENT_ID = 'personal use script for a reddit script application'
REDDIT_USERNAME = 'username for a valid reddit account'
REDDIT_PASSWORD = 'password to a valid reddit account'
```
## Execution
The analysis can be run from the file `analysis.ipynb`

```bash