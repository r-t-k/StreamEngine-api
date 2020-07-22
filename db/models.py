from datetime import date
from datetime import time
import uuid
from db import *




class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    status = Optional(str)
    username = Required(str, unique=True)
    email = Required(str)
    password = Required(str)
    firstname = Optional(str)
    lastname = Optional(str)
    channeladmins = Set('ChannelAdmin')
    trackers = Set('Track')
    user_activity = Optional('UserActivity')
    user_notifications = Set('UserNotification')
    meta = Optional(Json)
    chat_messages = Set('ChatMessage')
    date_joined = Optional(date)


class Channel(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str, unique=True)
    channel_meta = Optional('ChannelMeta')
    channeladmin = Optional('ChannelAdmin')
    library = Optional('Library')
    trackers = Set('Track')
    live_status = Optional(bool)
    streams = Set('Stream')
    streamkey = Required(uuid.UUID, default=uuid.uuid4, unique=True)
    stream_server_urls = Optional(Json)
    vod_server_urls = Optional(Json)
    chats = Set('Chat')
    channelactivity = Optional('ChannelActivity')


class Video(db.Entity):
    id = PrimaryKey(int, auto=True)
    stream = Optional('Stream')
    library = Required('Library')
    vod_urls = Optional(Json)


class Stream(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Optional(str)
    channel = Required(Channel)
    video = Required(Video)
    playlist_url = Optional(str)


class Chat(db.Entity):
    id = PrimaryKey(int, auto=True)
    channel = Required(Channel)
    chat_messages = Set('ChatMessage')
    date = Optional(date)


class ChannelAdmin(db.Entity):
    id = PrimaryKey(int, auto=True)
    channel = Required(Channel)
    user = Required(User)


class UserNotification(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    content = Optional(Json)
    meta = Optional(Json)


class ChannelActivity(db.Entity):
    id = PrimaryKey(int, auto=True)
    channel = Required(Channel)
    actions = Optional(Json)


class Community(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    config = Optional(Json)
    directories = Set('Directory')


class Directory(db.Entity):
    id = PrimaryKey(int, auto=True)
    libraries = Set('Library')
    community = Required(Community)
    category = Optional(str)


class Library(db.Entity):
    id = PrimaryKey(int, auto=True)
    videos = Set(Video)
    channel = Required(Channel)
    directories = Set(Directory)
    tags = Optional(Json)


class Track(db.Entity):
    id = PrimaryKey(int, auto=True)
    channel = Required(Channel)
    user = Required(User)


class UserActivity(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    actions = Optional(Json)


class ChannelMeta(db.Entity):
    id = PrimaryKey(int, auto=True)
    channel = Required(Channel)
    tags = Optional(Json)
    config = Optional(Json)


class ChatMessage(db.Entity):
    id = PrimaryKey(int, auto=True)
    chat = Required(Chat)
    content = Optional(str)
    user = Required(User)
    time = Optional(time)



db.generate_mapping(create_tables=True)