# Tweet Search and Destroy
A Flask application with Twitter integration to search for a particular keyword in your tweets and delete it.

## Requirements
1. Install [Python 3.x](https://www.python.org/downloads/)
2. Install dependencies using `pip install -r requirements.txt` to install all required packages in one go. Main packages are:

  - Flask
  - Flask-OAuthlib
  - gunicorn

3. Collect your Twitter consumer key and consumer secret from [here](https://twitter.com/apps) by creating a new app with `Read` and `Write` access level(already set by default).


## Setup
Set the following environment variables and you are good to go:

  - CONSUMER_KEY = *consumer key from Twitter*
  - CONSUMER_SECRET = *consumer secret from Twitter*

## To Do
- [ ] Currently only checks last 200 tweets, so add support using `page` parameter in the `user_timeline.json` query.  
- [ ] Search tweets within dates, having images, or links.  
- [ ] Write tests.  
- [ ] Add logging.  
- [ ] Handle all exceptions.  
- [ ] Redesign pages.  


### License
 See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT)
