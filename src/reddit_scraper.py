"""
This module contains functions to scrape data from the Reddit API.
"""
import os
import requests
import pandas as pd

def check_response_and_convert(response: requests.models.Response) -> None:
    """Checks the response object for errors

    Args:
        response (requests.models.Response): response object from the reddit api
    """
    if response.status_code == 200:
        return convert_to_dataframe(response.json()['data']["children"])
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def convert_to_dataframe(response_json: dict) -> pd.DataFrame:
    """converts a response object to a pandas dataframe

    Args:
        response (requests.models.Response): response object from the reddit api

    Returns:
        pd.DataFrame: it's a great dataframe
    """
    # Convert response to a DataFrame
    df = pd.json_normalize(response_json)
    # Rename columns
    df = rename_columns(df)
    return df

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """convenience tool to rename columns in a pandas dataframe

    Args:
        df (pd.DataFrame): dataframe to be renamed

    Returns:
        pd.DataFrame: descriptions of the thing
    """
     # Create a dictionary to map old column names to new column names
    new_column_names = {col: col.split('.')[1] if '.' in col else col
                        for col in df.columns}
    # Rename columns
    df = df.rename(columns=new_column_names)
    return df

def get_headers()-> dict:
    """creates the request header for the reddit api

    Returns:
        _type_: _description_
    """
    # Reddit API requires a user agent to be passed in the header
    auth = requests.auth.HTTPBasicAuth(os.environ["CLIENT_ID"],
                                       os.environ["SECRET_REDDIT_KEY"])
    data = {
        "grant_type": "password",
        "username": os.environ["REDDIT_USERNAME"],
        "password": os.environ["REDDIT_PASSWORD"]
    }
    headers = {"User-Agent": "MyAPI/0.0.1"}
    res = requests.post("https://www.reddit.com/api/v1/access_token",
                        auth=auth, data=data, headers=headers, timeout=30)
    token = res.json()["access_token"]
    headers = {"User-Agent": "MyAPI/0.0.1",
           "Authorization": f"bearer {token}"}
    return headers

def get_posts(headers,
              subreddit: str = "wallstreetbets",
              post_type: str = "hot") -> dict:
    """Gets the posts from a subreddit

    Args:
        headers (_type_): headers required for the json request
        subreddit (_type_): subbreddit name 
        post_type (_type_): Type of search. We can search for hot, new, top, etc.
    Returns:
        _type_: pandas dataframe with the relevant information
    """
    res = requests.get(f"https://oauth.reddit.com/r/{subreddit}/{post_type}",
                       headers=headers,
                       params = {"limit": 100},
                       timeout=30)
    return check_response_and_convert(res)

def search_flair(headers, subreddit: str = "wallstreetbets",
                 flair: str = "Gain")-> pd.DataFrame:
    """Searches for posts with a specific flair

    Args:
        headers (_type_):   headers required for the json request
        subreddit (_type_): full name of the subreddit
        flair (_type_): flair name to search for
    Returns:
        _type_: pandas dataframe with the relevant information
    """
    url = f'https://oauth.reddit.com/r/{subreddit}/search?q=flair_name%3A"{flair}"&sort=new&restrict_sr=on'
    res = requests.get(url,
                       headers=headers,
                       params = {"limit": 100, "q": f"flair_name:{flair}"},
                       timeout=30)
    return check_response_and_convert(res)

def search_daily(headers, subreddit: str = "wallstreetbets")-> pd.DataFrame:
    """search only daily discussion threads

    Args:
        headers (_type_): headers required for the json request
        subreddit (str, optional): full name of subreddit. Defaults to "wallstreetbets".
    """
    query = 'Daily Discussion Thread'
    url = f'https://oauth.reddit.com/r/{subreddit}/search?q={query}&sort=new&restrict_sr=on'

    response = requests.get(url, headers=headers,
                            timeout=30,
                            params={"limit": 100})
    return check_response_and_convert(response)

def search_comments(headers, thread_id,
                    subreddit: str = "wallstreetbets")-> pd.DataFrame:
    """_summary_

    Args:
        headers (_type_): _description_
        thread_id (_type_): _description_
        subreddit (str, optional): _description_. Defaults to "wallstreetbets".

    Returns:
        pd.DataFrame: _description_
    """
    # Get comments from the daily discussion thread
    comments_url = \
        f'https://oauth.reddit.com/r/{subreddit}/comments/{thread_id}'
    comment_response = requests.get(comments_url, headers=headers,
                                    timeout=30)
    if comment_response.status_code == 200:
        thread_json, comment_json = comment_response.json()
        comment_json = comment_json['data']['children']

        return convert_to_dataframe(comment_json)
    else:
        print("Request failed with status code {comment_response.status_code}")
        return None

def get_daily_discussion_comments(headers,
        subreddit: str = "wallstreetbets")-> pd.DataFrame:
    """Gets the daily discussion thread and its comments

    Args:
        headers (_type_): headers required for the json request
        subreddit (_type_): full name of the subreddit
    Returns:
        _type_: pandas dataframe with the relevant information
    """
    # Get daily discussion thread
    daily_discussion = search_daily(headers, subreddit)
    thread_ids = daily_discussion['id']
    list_of_comments = []
    for tid in thread_ids:
        comments = search_comments(headers, tid)
        list_of_comments.append(comments)
    return list_of_comments

