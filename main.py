from flask import Flask
from flask import (flash, g, redirect, render_template,
                   request, session, url_for)
from twitter import twitter

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'


@app.before_request
def before_request():
    g.user = None
    if 'twitter_oauth' in session:
        g.user = session['twitter_oauth']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    if g.user is None:
        return redirect(url_for('login', next=request.url))
    search_word = request.form['keyword']
    if not search_word:
        return redirect(url_for('index'))

    resp = twitter.request('statuses/user_timeline.json?count=200')
    found = []
    all_tweets = resp.data

    for twit in all_tweets:
        if search_word.lower() in twit["text"].lower():
            found.append(twit)

    if resp.status == 401:
        flash('Authorization error with Twitter.')

    return render_template('search.html', tweets=found)


@app.route('/delete', methods=['POST'])
def delete():
    if g.user is None:
        return redirect(url_for('login', next=request.url))
    ids = request.form.getlist('tweet_id')
    if not ids:
        return redirect(url_for('index'))
    for tweet_id in ids:
        resp = twitter.post('statuses/destroy/{0}.json'.format(tweet_id))
        if resp.status != 200:
            flash("There was an error deleting tweet!")
    return render_template('delete.html')


@app.route('/login')
def login():
    callback_url = url_for('oauthorized', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url or request.referrer or None)


@app.route('/logout')
def logout():
    session.pop('twitter_oauth', None)
    return redirect(url_for('index'))


@app.route('/oauthorized')
def oauthorized():
    resp = twitter.authorized_response()
    if resp is None:
        flash('You denied the request to sign in.')
    else:
        session['twitter_oauth'] = resp
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
