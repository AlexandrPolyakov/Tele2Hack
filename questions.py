{\rtf1\ansi\ansicpg1251\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import command_system\
\
#------------------------------------\
def deals():\
   message = '\uc0\u1053 \u1086 \u1088 \u1084 \u1072 \u1083 \u1100 \u1085 \u1086 , \u1082 \u1072 \u1082  \u1091  \u1090 \u1077 \u1073 \u1103 ?'\
   return message, ''\
deals_command = command_system.Command()\
deals_command.keys = ['\uc0\u1082 \u1072 \u1082  \u1076 \u1077 \u1083 \u1072 ', '\u1082 \u1072 \u1082  \u1076 \u1077 \u1083 \u1072 ?']\
deals_command.description = '\uc0\u1086 \u1090 \u1074 \u1077 \u1095 \u1091 '\
deals_command.process = deals\
#------------------------------------\
#------------------------------------\
def ok():\
   message = '\uc0\u1054 \u1082 '\
   return message, ''\
deals_command = command_system.Command()\
deals_command.keys = ['\uc0\u1085 \u1086 \u1088 \u1084 \u1072 \u1083 \u1100 \u1085 \u1086 ', '\u1085 \u1077 \u1087 \u1083 \u1086 \u1093 \u1086 ', '\u1093 \u1086 \u1088 \u1086 \u1096 \u1086 ', '\u1089 \u1086 \u1081 \u1076 \u1077 \u1090 ', '\u1087 \u1086 \u1085 \u1103 \u1090 \u1085 \u1086 ', '\u1087 \u1083 \u1086 \u1093 \u1086 ']\
deals_command.description = '\uc0\u1082 \u1086 \u1085 \u1077 \u1094  \u1076 \u1080 \u1072 \u1083 \u1086 \u1075 \u1072 '\
deals_command.process = ok\
#------------------------------------}