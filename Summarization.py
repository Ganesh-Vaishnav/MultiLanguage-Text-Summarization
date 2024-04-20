# -*- coding: utf-8 -*-

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import requests

# To translate text from source language to target language
def translate_text(text, source_lang, target_lang):
        base_url = "https://api.mymemory.translated.net/get"
        results = []
        # Split text into chunks (500 each)
        for i in range(0, len(text), 500):
            chunk = text[i:i+500]
            params = {
                "q": chunk,
                "langpair": f"{source_lang}|{target_lang}"
            }
            response = requests.get(base_url, params=params)
            translation = response.json()["responseData"]["translatedText"]
            results.append(translation)
        return " ".join(results)

# To summarize text 
def summarizer(rawdoc,sel_lang,targ_lang,percent):

    text = rawdoc
    source_lang = sel_lang
    target_lang = "en"

    # translate source to English if not be default
    if source_lang  != target_lang:
        translated_text = translate_text(text, source_lang, target_lang)
    else:
        translated_text = text
 
    # print(translated_text)


    stopwords = list(STOP_WORDS)       
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(translated_text)      
    

     # Tokenization of words
    tokens = [token.text for token in doc]     
    # print(tokens)

    # Word frequency after neglecting stop words and punctuation
    word_freq={}

    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    print(word_freq)

    # Checking maximum frequency of word in doc
    max_freq = max(word_freq.values())
    # print(max_freq)

    # Dividing the max frequency with all frequency to normalize the frequency
    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    # Tokenization of sentences
    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)


    # Sentence frequency
    sent_scores = {}
    for sent in sent_tokens:
        sent_score = 0
        for word in sent:
            if word.text in word_freq.keys():
                sent_score += word_freq[word.text]
    # Calculate the average score for the sentence
        sent_score /= len(sent)
        sent_scores[sent] = sent_score



    # It decides the percentage of summarization, here it is 30% percent
    select_len = int(len(sent_tokens) * float(percent))


    # List of summarized text that is done in order of higher frequency of sentences
    summary = nlargest(select_len, sent_scores, sent_scores.get)
    # print(summary)


    # Converting summarized list into summarized para
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    
    text = summary
    source_lang = "en"
    target_lang = targ_lang

    # translate if target lang is not English
    if "en"  != target_lang:
        translated_text = translate_text(text, source_lang, target_lang)
    else:
        translated_text = text

    return translated_text


