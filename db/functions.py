from db import *

@db_session
def add_user(username, email,password):
    User(username=username, email=email, password=password)

@db_session
def add_channel(title):
    Channel(title=title)


@db_session
def channel_set_admin(username, channel_title):
   user = User.get(username=username)
   channel = Channel.get(title=channel_title)

   newAdmin = ChannelAdmin(channel=channel, user=user)

   user.channeladmins += newAdmin

   channel.channeladmin = newAdmin

@db_session
def channel_get_admin(channel_title):
    channel = Channel.get(title=channel_title)

    admin = ChannelAdmin.get(channel=channel)

    user = admin.user
   
    return  user.username