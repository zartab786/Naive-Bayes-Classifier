import glob,re,pickle
import string
def punctuator(text):
	text=text.lower()
	text=text.split()
	#result=(text.translate(str.maketrans("","",string.punctuation)))
	result=[word.strip(string.punctuation) for word in text]
	#print(result)
	return result


#print(category)


def tokenize(category):
	#category=category.lower()
	#Tokenization
	category2=[]
	from nltk.tokenize import word_tokenize
	from nltk.tokenize import RegexpTokenizer
	#category2=word_tokenize(str(category))
	tokenizer=RegexpTokenizer(r"\w+")
	#print(tokenizer)
	category2=tokenizer.tokenize(str(category))
	#category2=re.sub(r"\d+"," ",str(category2))
	return category2
#print(category2)

def removestopwords(category2):
	from nltk.corpus import stopwords
	stop=set(stopwords.words('english'))

	filtered_category=[w for w in category2 if not w in stop]
	return filtered_category

	#print(filtered_category)

"""category=punctuator(str(category))
tokens=tokenize(category)
filtered=removestopwords(tokens)"""


#print(tokens)

  
g_dict={}
def frequency(tokens):
	dict={}

	for word in tokens:
		if word not in dict:
			dict[word]=1
			if word not in g_dict:
				g_dict[word]=1
			else:
				g_dict[word]=g_dict[word]+1
			 	
		else:
		  dict[word]=dict[word]+1
		  g_dict[word]=g_dict[word]+1

	#print(dict)
	return dict	  


#Pickling of motor cycles
"""freq_dict=frequency(filtered)
filename="frequencymotorcycles"
fp=open("filename","wb")
pickle.dump(freq_dict,fp)
fp.close()
fp=open("filename","rb")
#readfile=pickle.load(fp)
#print(readfile)"""

filelist1=glob.glob(r"E:\\Assignments\\NLP\\20_newsgroups\\*")



freq_list=[]
no_of_folders=[]
class_probability=[]
probability=[]
totalsum_of_docs=0
i=0
sum=0

for files in filelist1:
	filename=files[36:]
	print(filename)
	category=[]
	filelist2=glob.glob(r"E:\\Assignments\\NLP\\20_newsgroups\\"+filename+r"\\*")
	count=len(filelist2)
	no_of_folders.append(count)
	totalsum_of_docs=totalsum_of_docs+count
	for doc in filelist2:
		print(doc)
		fp=open(doc,"r")
		category.append(fp.read())


		
	category=re.sub(r"\d+"," ",str(category))
	category=punctuator(str(category))
	tokens=tokenize(category)
	filtered=removestopwords(tokens)
	print(filtered)
	freq_dict={}
	freq_dict=frequency(filtered)
	print(freq_dict)
	freq_list.append(freq_dict)
	fp2=open(r"E:\\Assignments\\NLP\\pickle\\"+filename+r"_freq","wb")
	pickle.dump(freq_dict,fp2)
	fp2.close()
	fp2=open(r"E:\\Assignments\\NLP\\pickle\\"+filename+r"_docscount","wb")
	pickle.dump(count,fp2)
	fp2.close()
	i=i+1
   


fp2=open(r"E:\\Assignments\\NLP\\pickle\\ListofDictionaryfreqListOfWordsEach","wb")
pickle.dump(freq_list,fp2)
fp2.close()

fp2=open(r"E:\\Assignments\\NLP\\pickle\\TotalDocsSum","wb")
pickle.dump(totalsum_of_docs,fp2)
fp2.close()

fp2=open(r"E:\\Assignments\\NLP\\pickle\\DocsCountlist","wb")
pickle.dump(no_of_folders,fp2)
fp2.close()

fp2=open(r"E:\\Assignments\\NLP\\pickle\\GlobalDictionary","wb")
pickle.dump(g_dict,fp2)
fp2.close()
	
		

	

		

#category=re.sub(r"\d+"," ",str(category))


