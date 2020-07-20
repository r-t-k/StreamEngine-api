from db import *


#user functions

#create
@db_session
def user_create(username, email,password):
    User(username=username, email=email, password=password)

    user = User.get(username=username)
    return user.username + ' created'
#get
@db_session
def user_get(username = None, id = None):
    user = "no match found"

    if(username != None):
        user = User.get(username=username)

    if(id != None):
        user = User.get(id=id)

    return user

#delete
@db_session
def user_delete(username = None, id = None):
    user = "no match found"

    if(username != None):
        user = User.get(username=username)
        user.delete()

    if(id != None):
        user = User.get(id=id)
        user.delete()

    return user.username + ' ID:' + str(user.id) + ' deleted'


#channel functions

#create
@db_session
def channel_create(title):
    Channel(title=title)



#get
@db_session
def channel_get(title=None, id=None):
    channel = 'no match found' 

    if(title != None):
        channel = Channel.get(title=title)

    if(id != None):
        channel = Channel.get(id=id)

    return channel


#delete
@db_session
def channel_delete(title=None, id=None):
    channel = 'no match found' 

    if(title != None):
        channel = Channel.get(title=title)
        channel.delete()
    if(id != None):
        channel = Channel.get(id=id)
        channel.delete()
    return channel.title + ' ID:' + str(channel.id) + ' deleted'

#set admin
@db_session
def channel_set_admin(username, channel_title):
   user = User.get(username=username)
   channel = Channel.get(title=channel_title)

   newAdmin = ChannelAdmin(channel=channel, user=user)

   user.channeladmins += newAdmin

   channel.channeladmin = newAdmin

#get admin
@db_session
def channel_get_admin(channel_title):
    channel = Channel.get(title=channel_title)

    admin = ChannelAdmin.get(channel=channel)

    user = admin.user
   
    return  user.username



#stream functions