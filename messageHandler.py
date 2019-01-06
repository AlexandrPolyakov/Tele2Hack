{\rtf1\ansi\ansicpg1251\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww25400\viewh16000\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import vkapi\
import os\
import importlib\
from command_system import command_list\
from gensim import corpora, models\
\
#\uc0\u1051 \u1077 \u1084 \u1084 \u1072 \u1090 \u1080 \u1079 \u1072 \u1094 \u1080 \u1103 \
from pymystem3 import Mystem\
m = Mystem()\
\
#\uc0\u1080 \u1089 \u1087 \u1088 \u1072 \u1074 \u1083 \u1077 \u1085 \u1080 \u1077  \u1086 \u1087 \u1077 \u1095 \u1072 \u1090 \u1086 \u1082 \
import jamspell\
corrector = jamspell.TSpellCorrector()\
corrector.LoadLangModel('/Users/alexanpolyakov/Downloads/ru_small.bin')\
\
##\uc0\u1069 \u1090 \u1072  flask \u1087 \u1072 \u1087 \u1082 \u1072  \u1084 \u1086 \u1078 \u1077 \u1090  \u1076 \u1072 \u1090 \u1100  \u1082 \u1088 \u1072 \u1090 \u1082 \u1086 \u1077  \u1086 \u1087 \u1080 \u1089 \u1072 \u1085 \u1080 \u1077  \u1088 \u1077 \u1072 \u1083 \u1080 \u1079 \u1072 \u1094 \u1080 \u1080 \
\
##\uc0\u1053 \u1077 \u1086 \u1073 \u1093 \u1086 \u1076 \u1080 \u1084 \u1086  \u1079 \u1072 \u1075 \u1088 \u1091 \u1079 \u1080 \u1090 \u1100  \u1089 \u1102 \u1076 \u1072  \u1074 \u1089 \u1077  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1080  \u1086 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1082 \u1080  \u1090 \u1077 \u1082 \u1089 \u1090 \u1072 , \u1080 \u1084 \u1087 \u1086 \u1088 \u1090 \u1080 \u1088 \u1086 \u1074 \u1072 \u1090 \u1100  \u1084 \u1086 \u1076 \u1077 \u1083 \u1100  LDA\
##\uc0\u1042  \u1076 \u1072 \u1083 \u1100 \u1085 \u1077 \u1081 \u1096 \u1077 \u1084  \u1073 \u1088 \u1072 \u1090 \u1100  \u1080 \u1079  \u1073 \u1072 \u1079  \u1076 \u1072 \u1085 \u1085 \u1099 \u1077 , \u1086 \u1073 \u1088 \u1072 \u1073 \u1072 \u1090 \u1099 \u1074 \u1072 \u1090 \u1100  \u1080 \u1093  \u1074  \u1089 \u1086 \u1086 \u1090 \u1074 \u1077 \u1090 \u1089 \u1090 \u1074 \u1080 \u1080  c \u1080 \u1077 \u1088 \u1072 \u1088 \u1093 \u1080 \u1077 \u1081  \u1092 \u1072 \u1081 \u1083 \u1086 \u1074 \
##\uc0\u1079 \u1072 \u1093 \u1074 \u1072 \u1090 \u1099 \u1074 \u1072 \u1077 \u1084 \u1099 \u1081  \u1085 \u1080 \u1078 \u1077  message - \u1080 \u1089 \u1093 \u1086 \u1076 \u1085 \u1099 \u1081  \u1090 \u1077 \u1082 \u1089 \u1090  \u1076 \u1083 \u1103  \u1072 \u1085 \u1072 \u1083 \u1080 \u1079 \u1072 \
##\uc0\u1055 \u1086 \u1089 \u1082 \u1086 \u1083 \u1100 \u1082 \u1091  \u1085 \u1077 \u1090  \u1087 \u1088 \u1072 \u1074  \u1074 \u1099 \u1083 \u1086 \u1078 \u1080 \u1090 \u1100  \u1084 \u1086 \u1076 \u1077 \u1083 \u1100  \u1085 \u1072  \u1089 \u1077 \u1088 \u1074 \u1077 \u1088 , \u1086 \u1075 \u1088 \u1072 \u1085 \u1080 \u1095 \u1080 \u1084 \u1089 \u1103  \u1086 \u1087 \u1080 \u1089 \u1072 \u1085 \u1080 \u1077 \u1084  \u1087 \u1088 \u1086 \u1094 \u1077 \u1089 \u1089 \u1072 \
\
def load_modules():\
   # \uc0\u1087 \u1091 \u1090 \u1100  \u1086 \u1090  \u1088 \u1072 \u1073 \u1086 \u1095 \u1077 \u1081  \u1076 \u1080 \u1088 \u1077 \u1082 \u1090 \u1086 \u1088 \u1080 \u1080 , \u1077 \u1077  \u1084 \u1086 \u1078 \u1085 \u1086  \u1080 \u1079 \u1084 \u1077 \u1085 \u1080 \u1090 \u1100  \u1074  \u1085 \u1072 \u1089 \u1090 \u1088 \u1086 \u1081 \u1082 \u1072 \u1093  \u1087 \u1088 \u1080 \u1083 \u1086 \u1078 \u1077 \u1085 \u1080 \u1103 \
   files = os.listdir("mysite/commands")\
   modules = filter(lambda x: x.endswith('.py'), files)\
   for m in modules:\
       importlib.import_module("commands." + m[0:-3])\
\
def get_answer(body):\
   message = "\uc0\u1055 \u1088 \u1086 \u1089 \u1090 \u1080 , \u1085 \u1077  \u1087 \u1086 \u1085 \u1080 \u1084 \u1072 \u1102  \u1090 \u1077 \u1073 \u1103 . \u1053 \u1072 \u1087 \u1080 \u1096 \u1080  '\u1087 \u1086 \u1084 \u1086 \u1097 \u1100 ', \u1095 \u1090 \u1086 \u1073 \u1099  \u1091 \u1079 \u1085 \u1072 \u1090 \u1100  \u1084 \u1086 \u1080  \u1082 \u1086 \u1084 \u1072 \u1085 \u1076 \u1099 "\
   attachment = ''\
   distance = len(body)\
   command = None\
   key = ''\
   for c in command_list:\
       for k in c.keys:\
           d = damerau_levenshtein_distance(body, k)\
           if d < distance:\
               distance = d\
               command = c\
               key = k\
               if distance == 0:\
                   message, attachment = c.process()\
                   return message, attachment\
   if distance < len(body)*0.4:\
       message, attachment = command.process()\
       message = '\uc0\u1071  \u1087 \u1086 \u1085 \u1103 \u1083  \u1074 \u1072 \u1096  \u1079 \u1072 \u1087 \u1088 \u1086 \u1089  \u1082 \u1072 \u1082  "%s"\\n\\n' % key + message\
   return message, attachment\
\
def create_answer(data, token):\
   load_modules()\
   user_id = data['user_id']\
   message, attachment = get_answer(data['body'].lower())\
   vkapi.send_message(user_id, token, message, attachment)\
\
def damerau_levenshtein_distance(s1, s2):\
   d = \{\}\
   lenstr1 = len(s1)\
   lenstr2 = len(s2)\
   for i in range(-1, lenstr1 + 1):\
       d[(i, -1)] = i + 1\
   for j in range(-1, lenstr2 + 1):\
       d[(-1, j)] = j + 1\
   for i in range(lenstr1):\
       for j in range(lenstr2):\
           if s1[i] == s2[j]:\
               cost = 0\
           else:\
               cost = 1\
           d[(i, j)] = min(\
               d[(i - 1, j)] + 1,  # deletion\
               d[(i, j - 1)] + 1,  # insertion\
               d[(i - 1, j - 1)] + cost,  # substitution\
           )\
           if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:\
               d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition\
   return d[lenstr1 - 1, lenstr2 - 1]}