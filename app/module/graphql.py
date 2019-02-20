from graphene import ObjectType, String, List, Schema, Field
from model import User, Post


#========================================Fields======================================
class CommentField(ObjectType):
	content = String()
	name = String()

class PostField(ObjectType):
	#post = Field(PostField,id=String())
	id = String()
	title = String()
	tags = List(String)
	comments = List(CommentField)

	def resolve_comments(self, info):
		return self.comments

class UserField(ObjectType):
	id = String()
	first_name = String()
	last_name = String()
	email = String()
	fullname = String()	
	posts = List(PostField)

	def resolve_fullname(self, info):
		return self.first_name + ' ' + self.last_name

	def resolve_posts(self, info):
		user = User.objects.get(id=self.id)
		posts = []
		for post in Post.objects(author=user):
			posts.append(post)
		return posts



#========================================Top Level Queries======================================


class TesQuery(ObjectType):
    hello = String(argument=String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        return 'Hello ' + argument

class UserQuery(ObjectType):
	user = Field(UserField,id=String())
	userlist = List(UserField)
	
	def resolve_user(self, info, id):
		return User.objects.get(id=id)

	def resolve_userlist(self, info):
		return User.objects()		 



#========================================Schema creation======================================

class Query(TesQuery,UserQuery):
	pass

schema = Schema(query=Query)
