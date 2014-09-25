import webapp2
import jinja2

import os
import json
import re


class Handler(webapp2.RequestHandler):
    def render(self, template):
        t = self.jinja_environment.get_template(template)
        self.response.write(t.render())

    @property
    def template_directory(self):
        return os.path.join(os.path.dirname(__file__), 'templates')

    @property
    def jinja_environment(self):
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(self.template_directory),
            autoescape=True)


class AjaxHandler(Handler):
    def get(self):
        self.render("ajax-prototype.html")

    def post(self):
        data = json.loads(self.request.body)
        username = data["name"]

        if not re.match(r"^[a-zA-Z0-9_-]{3,20}$", username):
            if len(username) < 3:
                message = "Your name must be at least 3 characters long."
            else:
                message = "Allowed characters are \
                           a-z, A-Z, 0-9, underscores \
                           and hyphens."
        else:
            message = "Congrats!"

        self.response.write(json.dumps({"message": message}))


application = webapp2.WSGIApplication([("/", AjaxHandler)
                                       ], debug=True)
