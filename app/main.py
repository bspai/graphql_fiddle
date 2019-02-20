
###################################################################
#   Description: Sample Application using Flask, GraphQL, MongoDB.
#
#    Install through pip:
#           flask, mongoengine, graphene, flask_graphql
#
#    Update the above list as new packages are used.
#
#    Make sure mongo db is running in localhost
#
#    To start the application run the command:
#       python app/main.py
#
#    Use http://localhost:5000/graphql for accessing GraphQL UI.
###################################################################

from flask import Flask, request
from mongoengine import connect, Document, StringField
from module.graphql import schema
from module.model import User, Post, Comment
from flask_graphql import GraphQLView

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"

def configure_mongodb():
    """Configure MongoDB database"""
    # import models that are not referenced directly
    # todo: remove when this is added in mutation
    connect('admin',host='mongodb://root:example@localhost:27017')    # Update with Mongo DB connection details

configure_mongodb()

#From Browser call URL http://localhost:5000/user?firstname=James&lastname=Bond&email=james@example.com
@app.route("/user")
def save():
    firstname = request.args.get('firstname', '')
    lastname = request.args.get('lastname', '')
    email = request.args.get('email', '')
    User.objects.create(email=email,first_name=firstname,last_name=lastname)
    return "User Data Saved"

#From Browser call URL http://localhost:5000/post?id=5c6a8ee1b5746f5a82b2e03f&title=second_post&tags=iq
@app.route("/post")
def savePost():
    userId = request.args.get('id', '')
    title = request.args.get('title', '')
    tags = [request.args.get('tags', '')]
    user = User.objects.get(id=userId)
    Post.objects.create(title=title,author=user,tags=tags)
    return "Post Detail Saved"

#From Browser call URL http://localhost:5000/comment?postid=5c6d0601b5746f0b8985c65c&content=content1&name=peter
@app.route("/comment")
def saveComment():
    postId = request.args.get('postid', '')
    content = request.args.get('content', '')
    name = request.args.get('name', '')
    post = Post.objects.get(id=postId)
    post.comments.append(Comment(content=content, name=name))
    post.save()
    return "Comment Saved"


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


users = User.objects()
for user in users:
    print(user.email)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True)



