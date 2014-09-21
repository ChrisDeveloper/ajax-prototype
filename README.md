# [Ajax-Prototype](http://ajax-prototype.appspot.com/) #

Little Google App Engine prototype to see how to handle a simple Ajax POST request with a Python back-end. Check the code and learn how to "ajaxify" your error messages in HTML form submissions with Python and Google App Engine.

## Motivation ##
There is a shortage of online material on how to handle error messages in HTML form submissions with Ajax using a Python back-end with Google App Engine. This "prototype" application is built using the Google App Engine Python web framework [webapp2](https://webapp-improved.appspot.com/) and is meant to fill this learning gap. Hopefully web developers who mix those technologies together for the first time won't get stuck too long to make them work.

## Installation ##
If you want to run the app locally and play with the code, you need both [Python 2.7](https://www.python.org/download/releases/2.7/) (the app doesn't work with Python 3 or earlier versions of Python 2) as well as the [Google App Engine SDK for Python](https://developers.google.com/appengine/downloads) installed on your machine. If that's already the case, skip step 1 and go straight to step 2.

1. Windows users, just follow the download links and make sure you add Python to your DOS `PATH` (check [this video](http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96) for instructions). On Mac OS X, the easiest and by far the cleanest way is to use the [Homebrew](http://brew.sh/) package manager

        brew install python
        brew install google-app-engine

    and if you haven't done so yet, set your `PATH` so that Homebrew-installed programs come first (run `echo export PATH="/usr/local/bin:$PATH"     >> ~/.bash_profile` and `source ~/.bash_profile`). Linux users, make sure that your sytem's default Python version is 2.7.x. Then follow the link above to download the Google App Engine SDK for Python zip file. Unzip this file and add the `google_appengine` directory to your `PATH` with

        echo export PATH=$PATH:/path_to_dir/google_appengine/ >> /home/username/.profile
        source /home/username/.profile

2. Clone the app's repository into your machine (with `git clone https://github.com/ChrisDeveloper/ajax-prototype`). Then all you need is to run

    
        cd path_to_your_repo/ajax-prototype
        dev_appserver.py .


    Don't forget to replace `path_to_your_repo` by your local repository's path. The app is now running locally on the Google App Engine server at `http://localhost:8080`. You're good to go!

## Description ##
- The HTML form call the JavaScript function `ajaxScript` in `ajax_script.js`once the `Submit Query` button is triggered. This function will makes the Ajax request to the server.
- Notice that `ajax_script.js`contains a second function, the so-called `ajaxScript2`. This function does the exact same thing as `ajaxScript`, only the Ajax request is written in "pure" JavaScript, while `ajaxScript` relies on the jQuery `.ajax()`method. Pick the function that fits your taste.
- JSON is used to send the data between the browser and the server. 
- `main.py` handles the server side of the business.
- The handy `json` module provides the two key Python ingredients. `json.loads` handles the data that the browser sends to the server, while `json.dumps` handles the data sent by the server in response to the browser's request.
- The `self.request.body` argument of `json.loads` is the only less common piece of Google App Engine that is used in the process, as it is specific to the task. As its name suggests, it gets the body from the Ajax request, which is the JSON object that `json.loads` takes as argument.
- On the client-side, the jQuery `.done()`  method will eventually handle the response that it gets from the server.

It is supposed that you know the basics of the Google App Engine/Python stack, such as [Jinja2](http://jinja.pocoo.org/) templating engine or the get/post methods of the `webapp2.RequestHandler` object, although this not necessary to grasp what's going on. If you're familiar with other Python web frameworks, that shouldn't affect your understanding. Notice that the webapp2 web framework can be used outside of Google App Engine.

## Further info ##
[This Stack Overflow answer](http://stackoverflow.com/a/22053890/3190077) is a good source of inspiration. It uses the same set of technologies to "ajaxify" vote ups/downs found on sites such as reddit. However this example is more intricate and involves a lot more code, as database models are needed in this specific case.