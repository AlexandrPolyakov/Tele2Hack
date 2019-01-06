{\rtf1\ansi\ansicpg1251\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import vk\
import random\
\
session = vk.Session()\
api = vk.API(session, v=5.0)\
\
\
def send_message(user_id, token, message, attachment=""):\
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)\
\
def get_random_wall_picture(group_id):\
    max_num = api.photos.get(owner_id=group_id, album_id='wall', count=0)['count']\
    num = random.randint(1, max_num)\
    photo = api.photos.get(owner_id=str(group_id), album_id='wall', count=1, offset=num)['items'][0]['id']\
    attachment = 'photo' + str(group_id) + '_' + str(photo)\
    return attachment}