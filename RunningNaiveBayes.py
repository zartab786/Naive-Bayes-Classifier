import glob,re,pickle,math
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




def task1(k,text):

	text=re.sub(r"\d+"," ",str(text))
	punctuated=punctuator(text)
	tokenized=tokenize(punctuated)
	filtered=removestopwords(tokenized)
	dict_text={}
	for word in filtered:
		if word not in dict_text:
			dict_text[word]=1
		else:
			dict_text[word]=dict_text[word]+1	

	#print(dict_text)		
	fp=open("E:\\Assignments\\NLP\\pickle\\rec.motorcycles_freq","rb")
	dictclass1=pickle.load(fp)
	fp.close()
	fp=open("E:\\Assignments\\NLP\\pickle\\rec.motorcycles_docscount","rb")
	doccount1=pickle.load(fp)
	fp.close()

	dictsum={}
	#print(len(dictclass1))


	for word in dictclass1.keys():
		if word not in dictsum:
			dictsum[word]=1
		else:
			dictsum[word]=dictsum[word]+1	


	
	fp=open("E:\\Assignments\\NLP\\pickle\\rec.sport.baseball_freq","rb")
	dictclass2=pickle.load(fp)
	fp.close()
	fp=open("E:\\Assignments\\NLP\\pickle\\rec.sport.baseball_docscount","rb")
	doccount2=pickle.load(fp)
	fp.close()
	#print(len(dictclass2))


	for word in dictclass2.keys():
		if word not in dictsum:
			dictsum[word]=1
		else:
			dictsum[word]=dictsum[word]+1	

	#print(dictsum)


	prob_class1=math.log((doccount1/(doccount1+doccount2)),10)
	prob_class2=math.log((doccount2/(doccount2+doccount1)),10)

	
	vocab=len(dictsum)
	#print("Vocabulary size ",end=" ")
	#print(vocab)

	prob_text_class1=0
	prob_text_class2=0
	count=0
	sum_of_words1=0
	for word in dictclass1.keys():
		sum_of_words1+=dictclass1[word]

	sum_of_words2=0	

	for word in dictclass2.keys():
		sum_of_words2+=dictclass2[word]


		
	for word in dict_text.keys():
		if word in dictclass1.keys():
			count=dictclass1[word]*dict_text[word]
		else:
			count=0

		prob_text_class1+=math.log((count+k)/(k*(vocab+1)+sum_of_words1),10)

	prob_text_class1+=prob_class1

	for word in dict_text.keys():
		if word in dictclass2.keys():
			count=dictclass2[word]*dict_text[word]
		else:
			count=0

		prob_text_class2+=math.log((count+k)/(k*vocab+sum_of_words2),10)




	prob_text_class2+=prob_class2

	print("The probability for text to be in class 1 is ",end=" ")
	print(prob_text_class1)
	print("The probability for text to be in class 2 is ",end=" ")
	print(prob_text_class2)

	if(prob_text_class1>prob_text_class2):
		print("The class of document is",end=" ")
		print("rec.motorcycles")
	else:
		print("The class of document is",end=" ")
		print("rec.sport.baseball")



def task2(k,text):
	text=re.sub(r"\d+"," ",str(text))
	punctuated=punctuator(text)
	tokenized=tokenize(punctuated)
	filtered=removestopwords(tokenized)
	dict_text={}
	for word in filtered:
		if word not in dict_text:
			dict_text[word]=1
		else:
			dict_text[word]=dict_text[word]+1

	list_of_dictionary=[]
	fp=open("E:\\Assignments\\NLP\\pickle\\TotalDocsSum","rb")
	totaldocs=pickle.load(fp)
	fp.close()

	fp=open("E:\\Assignments\\NLP\\pickle\\DocsCountlist","rb")
	Doclist=pickle.load(fp)
	fp.close()

	fp=open("E:\\Assignments\\NLP\\pickle\\ListofDictionaryfreqListOfWordsEach","rb")
	ListofDictionary=pickle.load(fp)
	fp.close()

	fp=open("E:\\Assignments\\NLP\\pickle\\GlobalDictionary","rb")
	global_dict=pickle.load(fp)
	fp.close()

	vocab=len(global_dict)

	class_prob=[]

	for docs in Doclist:
		doc_of_class=docs
		prob_of_class=math.log((doc_of_class/totaldocs),10)
		class_prob.append(prob_of_class)

	
	tota_sum_of_words=0 
	total_words_class=[]

	for dict in ListofDictionary:
		sum=0
		for word in dict.keys():
			tota_sum_of_words+=dict[word]
			sum=sum+dict[word]
		total_words_class.append(sum)	

	
	wordcount=0
	prob=0
	prob_text_class=[]
	i=0
	for dict in ListofDictionary:
		for word in dict.keys():
			prob=0
			if word in dict_text.keys():
				wordcount=dict[word]*dict_text[word]
			else:
				wordcount=0	
			prob+=math.log((wordcount+k)/(total_words_class[i]+k*(vocab+1)),10)

		prob+=class_prob[i]
		prob_text_class.append(prob)
		i=i+1

	

	min=prob_text_class[0]
	pos=1
	print("Probability of text to be in  class 1",end=" ")	
	print(prob_text_class[0])

	for i in range (1,20):
		print("Probability of text to be in class ",end=" ")
		print(i+1,end=" ")
		print(prob_text_class[i])
		if prob_text_class[i] < min:
			min=prob_text_class[i]
			pos=i+1

	
	print("The classification of text is class ",end=" ")
	print(pos)		

			



				


	




			

	
    

fp=open("E:\\Assignments\\NLP\\20_newsgroups\\rec.sport.baseball\\102587","r")
text=fp.read()
fp.close()
#print(text)
print("Task1---")
print("Enter the value of k for task 1")
k=int(input())
task1(k,text)

print("Task2---")
print("Enter the value of k for task 2")
k=int(input())
task2(k,text)
