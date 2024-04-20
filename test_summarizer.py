from Summarization import summarizer

raw_text = """Wikipedia[note 3] is a multilingual free online encyclopedia written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and using a wiki-based editing system called MediaWiki. Wikipedia is the largest and most-read reference work in history.[3] It is consistently one of the 10 most popular websites ranked by Similarweb and formerly Alexa; as of 2023, Wikipedia was ranked the 5th most popular site in the world according to Semrush.[4] It is hosted by the Wikimedia Foundation, an American non-profit organization funded mainly through donations.

Wikipedia was launched by Jimmy Wales and Larry Sanger on January 15, 2001. Sanger coined its name as a blend of wiki and encyclopedia. Wales was influenced by the "spontaneous order" ideas associated with Friedrich Hayek and the Austrian School of economics after being exposed to these ideas by the libertarian economist Mark Thornton.[5] Initially available only in English, versions in other languages were quickly developed. Its combined editions comprise more than 60 million articles, attracting around 2 billion unique device visits per month and more than 15 million edits per month (about 5.7 edits per second on average) as of January 2023.[6][7] In 2006, Time magazine stated that the policy of allowing anyone to edit had made Wikipedia the "biggest (and perhaps best) encyclopedia in the world".[8]"""


source_lang = "en"  # Assuming the sample text is in English
target_lang = "hi"  # Assuming you want to translate to Hindi
percent = 0.3  # For example, to generate a summary that retains 30% of the original text

translated_text = summarizer(raw_text, source_lang, target_lang, percent)
print(translated_text)
