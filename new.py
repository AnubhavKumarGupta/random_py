# # # import random
# # # while True:
# # #      print(''' 1. roll the dice             2. exit     ''')
# # #      user = int(input("what you want to do\n"))
# # #      if user==1:
# # #         number = random.randint(1,6)
# # #         print(number)
# # #      else:
# # #         break

# # from contextlib import nullcontext


# # {
# #     "cells": [
# #         {
# #             "cell_type": "code",
# #             "execution_count": nullcontext,
# #             "metadata": {},
# #             "outputs": [],
# #             "source": [
# #                 "import numpy as np\n",
# #                 "import cv2\n",
# #                 "\n",
# #                 "face_cascade = cv2.CascadeClassifier('face.xml')\n",
# #                 "eye_cascade = cv2.CascadeClassifier('eye.xml')\n",
# #                 "\n",
# #                 "cap = cv2.VideoCapture(0)\n",
# #                 "\n",
# #                 "while 1:\n",
# #                 "    ret, img = cap.read()\n",
# #                 "    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
# #                 "    faces = face_cascade.detectMultiScale(gray, 1.3, 5)\n",
# #                 "\n",
# #                 "    for (x,y,w,h) in faces:\n",
# #                 "        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)\n",
# #                 "        roi_gray = gray[y:y+h, x:x+w]\n",
# #                 "        roi_color = img[y:y+h, x:x+w]\n",
# #                 "        \n",
# #                 "        eyes = eye_cascade.detectMultiScale(roi_gray)\n",
# #                 "        for (ex,ey,ew,eh) in eyes:\n",
# #                 "            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)\n",
# #                 "\n",
# #                 "    cv2.imshow('img',img)\n",
# #                 "    k = cv2.waitKey(30) & 0xff\n",
# #                 "    if k == 27:\n",
# #                 "        break\n",
# #                 "\n",
# #                 "cap.release()\n",
# #                 "cv2.destroyAllWindows()"
# #             ]
# #         }
# #     ],
# #     "metadata": {
# #         "kernelspec": {
# #             "display_name": "Python 3",
# #             "language": "python",
# #             "name": "python3"
# #         },
# #         "language_info": {
# #             "codemirror_mode": {
# #                 "name": "ipython",
# #                 "version": 3
# #             },
# #             "file_extension": ".py",
# #             "mimetype": "text/x-python",
# #             "name": "python",
# #             "nbconvert_exporter": "python",
# #             "pygments_lexer": "ipython3",
# #             "version": "3.6.5"
# #         }
# #     },
# #     "nbformat": 4,
# #     "nbformat_minor": 2
# # }


# {
#     "cells": [
#         {
#             "cell_type": "code",
#             "execution_count": 5,
#             "metadata": {},
#             "outputs": [
#                 {
#                     "name": "stdout",
#                     "output_type": "stream",
#                     "text": [
#                         "{'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}\n"
#                     ]
#                 }
#             ],
#             "source": [
#                 "#pip install googletrans\n",
#                 "import googletrans\n",
#                 "print(googletrans.LANGUAGES)"
#             ]
#         },
#         {
#             "cell_type": "code",
#             "execution_count": 10,
#             "metadata": {},
#             "outputs": [
#                 {
#                     "name": "stdout",
#                     "output_type": "stream",
#                     "text": [
#                         "Translated(src=ro, dest=en, text=hello programmers, pronunciation=hello programmers, extra_data=\"{'translat...\")\n",
#                         "Translated(src=ro, dest=en, text=hello programmers, pronunciation=hello programmers, extra_data=\"{'translat...\")\n"
#                     ]
#                 }
#             ],
#             "source": [
#                 "#The most basic use of the Google Translate API is, of course, translating words or sentences from one language into another. To do so, we have to import the Translator class from googletrans module.\n",
#                 "\n",
#                 "from googletrans import Translator\n",
#                 "translator = Translator()\n",
#                 "result = translator.translate('salut programatori ')\n",
#                 "print(result)\n",
#                 "#by default the translate() method returns the english translation of the text passed to it.\n",
#                 "\n",
#                 "result = translator.translate('salut programatori', src='ro', dest='en')\n",
#                 "print(result)"
#             ]
#         },
#         {
#             "cell_type": "code",
#             "execution_count": 11,
#             "metadata": {},
#             "outputs": [
#                 {
#                     "name": "stdout",
#                     "output_type": "stream",
#                     "text": [
#                         "Detected(lang=hi, confidence=1.0)\n",
#                         "Detected(lang=en, confidence=1.0)\n"
#                     ]
#                 }
#             ],
#             "source": [
#                 "from googletrans import Translator\n",
#                 "\n",
#                 "text1 = '''\n",
#                 "हैलो पायथन प्रोग्रामर्स\n",
#                 "'''\n",
#                 "text2 = '''\n",
#                 "how are you\n",
#                 "'''\n",
#                 "translator = Translator()\n",
#                 "\n",
#                 "lang1 = translator.detect(text1)\n",
#                 "print(lang1)\n",
#                 "lang2 = translator.detect(text2)\n",
#                 "print(lang2)"
#             ]
#         },
#         {
#             "cell_type": "code",
#             "execution_count": null,
#             "metadata": {},
#             "outputs": [],
#             "source": []
#         }
#     ],
#     "metadata": {
#         "kernelspec": {
#             "display_name": "Python 3",
#             "language": "python",
#             "name": "python3"
#         },
#         "language_info": {
#             "codemirror_mode": {
#                 "name": "ipython",
#                 "version": 3
#             },
#             "file_extension": ".py",
#             "mimetype": "text/x-python",
#             "name": "python",
#             "nbconvert_exporter": "python",
#             "pygments_lexer": "ipython3",
#             "version": "3.6.5"
#         }
#     },
#     "nbformat": 4,
#     "nbformat_minor": 2
# }

a = 10
b = 20

a = a + b   # x // 10 + 20 = 30 
b = a - b   # y // 30 - 20 = 10
a = a - b   # x // 30 - 10 = 20
print("a =", a , "\nb =", b); 

# a,b = int (input().split()) # ye multiple input in one line me samajhna prega kyu nhi aarha 
print('Input the value of a & b')
a = int (input())
b = int (input())

a = a + b   # x // 10 + 20 = 30 
b = a - b   # y // 30 - 20 = 10
a = a - b   # x // 30 - 10 = 20

print('a =', a , '\nb =', b); 

