{\rtf1\ansi\ansicpg1251\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import command_system\
\
def hello():\
   message = '\uc0\u1055 \u1088 \u1080 \u1074 \u1077 \u1090 \\n\u1071  \u1095 \u1072 \u1090 -\u1073 \u1086 \u1090  \u1076 \u1083 \u1103  \u1093 \u1072 \u1082 \u1072 \u1090 \u1086 \u1085 \u1072 , \u1085 \u1086  \u1087 \u1086 \u1082 \u1072  \u1103  \u1089 \u1083 \u1072 \u1073 '\
   return message, ''\
\
hello_command = command_system.Command()\
\
hello_command.keys = ['\uc0\u1087 \u1088 \u1080 \u1074 \u1077 \u1090 ', 'hello', '\u1076 \u1088 \u1072 \u1090 \u1091 \u1090 \u1080 ', '\u1079 \u1076 \u1088 \u1072 \u1074 \u1089 \u1090 \u1074 \u1091 \u1081 ', '\u1079 \u1076 \u1088 \u1072 \u1074 \u1089 \u1090 \u1074 \u1091 \u1081 \u1090 \u1077 ']\
hello_command.description = '\uc0\u1055 \u1086 \u1087 \u1088 \u1080 \u1074 \u1077 \u1090 \u1089 \u1090 \u1074 \u1091 \u1102  \u1090 \u1077 \u1073 \u1103 '\
hello_command.process = hello}