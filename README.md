# twitter-stock-analysis

Function that uses twitter data to evaluate the stock of certain companies

## Installation
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

you can get your own reddit script details by doing the following:
1. Create a username and password on reddit
2. going to the [reddit apps page](https://www.reddit.com/prefs/apps)
3. and clicking "Create Another App"
4. fill out the general information and any required fields.
it really doesn't matter which ones you select or what you fill in.
5. Copy the api key that is shown.

```
SECRET_REDDIT_KEY = 'secret key for a reddit script application'
CLIENT_ID = 'personal use script for a reddit script application'
REDDIT_USERNAME = 'username for a valid reddit account'
REDDIT_PASSWORD = 'password to a valid reddit account'
OPEN_AI_KEY = 'openai secret key'
```
## Execution
The analysis can be run from the file `analysis.ipynb`

the overall flow should be as follows
![the flow diagram](flow.png)    