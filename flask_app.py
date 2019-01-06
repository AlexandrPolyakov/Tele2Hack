{\rtf1\ansi\ansicpg1251\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
# A very simple Flask Hello World app for you to get started with...\
\
from flask import Flask, request, json\
import vk\
from settings import *\
import messageHandler\
\
app = Flask(__name__)\
\
@app.route('/')\
def hello_world():\
    return 'Hello from Flask!'\
\
@app.route('/', methods=['POST'])\
def processing():\
    data = json.loads(request.data)\
    if 'type' not in data.keys():\
        return 'not vk'\
    if data['type'] == 'confirmation':\
        return confirmation_token\
    elif data['type'] == 'message_new':\
        messageHandler.create_answer(data['object'], token)\
        return 'ok'\
\
}