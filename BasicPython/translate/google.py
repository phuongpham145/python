import googletrans
from googletrans import  Translator
print(googletrans.LANGUAGES) 
t = Translator()
a = t.translate("em dep qua", src="vi", dest="en")
b = a.text
print(b)
