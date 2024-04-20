# -*- coding: utf-8 -*-

from Summarization import translate_text

text = """Wikipedia[note 3] is a multilingual free online encyclopedia written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and using a wiki-based editing system called MediaWiki. Wikipedia is the largest and most-read reference work in history.[3] It is consistently one of the 10 most popular websites ranked by Similarweb and formerly Alexa; as of 2023, Wikipedia was ranked the 5th most popular site in the world according to Semrush.[4] It is hosted by the Wikimedia Foundation, an American non-profit organization funded mainly through donations.

Wikipedia was launched by Jimmy Wales and Larry Sanger on January 15, 2001. Sanger coined its name as a blend of wiki and encyclopedia. Wales was influenced by the "spontaneous order" ideas associated with Friedrich Hayek and the Austrian School of economics after being exposed to these ideas by the libertarian economist Mark Thornton.[5] Initially available only in English, versions in other languages were quickly developed. Its combined editions comprise more than 60 million articles, attracting around 2 billion unique device visits per month and more than 15 million edits per month (about 5.7 edits per second on average) as of January 2023.[6][7] In 2006, Time magazine stated that the policy of allowing anyone to edit had made Wikipedia the "biggest (and perhaps best) encyclopedia in the world".[8]"""

hinditext = """ भारत दक्षिण एशिया में स्थित एक विशाल और विविध देश है। 1.3 बिलियन से अधिक लोगों की आबादी के साथ, यह दुनिया का दूसरा सबसे अधिक आबादी वाला देश है, और यह भूमि क्षेत्र के हिसाब से सातवां सबसे बड़ा देश भी है। भारत अपने समृद्ध इतिहास, विविध संस्कृति और आश्चर्यजनक प्राकृतिक सुंदरता के लिए जाना जाता है।
भारत का एक लंबा और जटिल इतिहास है जो हजारों साल पहले का है। देश पर सदियों से कई अलग-अलग साम्राज्यों और साम्राज्यों का शासन रहा है, प्रत्येक ने देश की संस्कृति और परंपराओं पर अपनी अनूठी छाप छोड़ी है। भारत का इतिहास ब्रिटिश औपनिवेशिक शासन से स्वतंत्रता के लिए उसके संघर्ष की विशेषता भी है, जिसे 1947 में हासिल किया गया था।
।आज, भारत सरकार की एक संघीय प्रणाली के साथ एक लोकतांत्रिक देश है। यह 2,000 से अधिक जातीय समूहों और 1,600 से अधिक भाषाओं का घर है, जो इसे दुनिया के सबसे विविध देशों में से एक बनाता है। भारत में हिंदू धर्म सबसे बड़ा धर्म है, लेकिन यह देश मुसलमानों, ईसाइयों, सिखों, बौद्धों और जैनियों की बड़ी आबादी का भी घर है।
"""

source_lang = "hi"
target_lang = "en"
translated_text = translate_text(hinditext, source_lang, target_lang)

print(translated_text)