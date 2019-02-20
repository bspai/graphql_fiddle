# graphql_fiddle
Sample application for playing with Graphql

#### Platform softwares required:
- Python and pip
- MongoDB

#### pip packages required:
flask, mongoengine, graphene, flask_graphql
- Note: Update the above list as new packages are used.

#### Steps to setup:
- Install Platform softwares listed above
- Install pip packages as listed above
- Update Mongo DB connection details in app/main.py

#### To start the application run the command:
``` python app/main.py
```

#### From Browser call below URLs to add data to mongo db (edit the URL parameter values)
- To add user: http://localhost:5000/user?firstname=James&lastname=Bond&email=james@example.com
- To add post: http://localhost:5000/post?id=5c6a8ee1b5746f5a82b2e03f&title=second_post&tags=iq
- To add comment: http://localhost:5000/comment?postid=5c6d0601b5746f0b8985c65c&content=content1&name=peter

#### URL to access GraphQL UI
http://localhost:5000/graphql
