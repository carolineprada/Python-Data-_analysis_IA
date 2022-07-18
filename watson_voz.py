# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 21:01:02 2021

@author: Caroline
"""

from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/e84182a3-f63f-4ac4-91af-327bf1965161"
iam_apikey_s2t = "Vd9r787k7TtXoNmsGOYijQm4x3-nPT--whOITtMyasOP"


authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

#prub = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3"

filename='PolynomialRegressionandPipelines.mp3'

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
    
response.result()

from pandas.io.json import json_normalize

json_normalize(response.result['results'],"alternatives")
response

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)


url_lt="https://api.us-south.language-translator.watson.cloud.ibm.com/instances/b6ac2065-fe67-4cee-a47b-a4facca88781"
apikey_lt='Zk3pcFAU2ypICddyo6yeHZ6fIt8zU5n3Da2LV6f_gYnq'

version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

from pandas.io.json import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")


translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response


translation=translation_response.get_result()
translation

spanish_translation =translation['translations'][0]['translation']
spanish_translation 

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
translation_eng

French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()

French_translation['translations'][0]['translation']
    