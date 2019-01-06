{\rtf1\ansi\ansicpg1251\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import command_system\
\
def info():\
   message = ''\
   for c in command_system.command_list:\
        message += c.keys[0] + ' - ' + c.description + '\\n'\
   return message, ''\
\
info_command = command_system.Command()\
\
info_command.keys = ['\uc0\u1087 \u1086 \u1084 \u1086 \u1097 \u1100 ', '\u1087 \u1086 \u1084 \u1086 \u1075 \u1080 ', 'help']\
info_command.desciption = '\uc0\u1055 \u1086 \u1082 \u1072 \u1078 \u1091  \u1089 \u1087 \u1080 \u1089 \u1086 \u1082  \u1082 \u1086 \u1084 \u1072 \u1085 \u1076 '\
info_command.process = info}