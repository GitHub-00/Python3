import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post
from model import User, Comment, Blog, next_id

@get('/')
@asyncio.coroutine
def index(request):
    users = yield from User.findAll()
    return {
        '__template__':'test.html',
        'user':users
    }