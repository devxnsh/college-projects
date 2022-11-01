from preprocessData_studentID import cleanlist, preprocessLine, rid_tags
from pprint import pprint

class Parser:
	"""Parser class requires inputstring and processes data to return row ID, post Type, Date, Cleaned Body and Vocabulary size"""
	def __init__(self, inputString):
		self.inputString = inputString
		self.ID = self.getID()
		self.type = self.getPostType()
		self.dateQuarter = self.getDateQuarter()
		self.cleanBody = self.getCleanedBody()
		self.Vocabularysize = self.getVocabularySize()
		
	def __str__(self):
		return((self.ID,self.type,self.dateQuarter,self.cleanBody,self.Vocabularysize).format("{},{},{},{},{}"))		

	def getID(self):
		proclist = (self.inputString.split(maxsplit=4)) #splits input String

		ROWID = int(((proclist[1].split("="))[-1])[1:-1]) #string manipulation
		return ROWID

	def getPostType(self):
		proclist = self.inputString.split(maxsplit=4)
		POSTID = int(((proclist[2].split("="))[-1])[1]) #string manipulation
		#declares post type usign if else chain
		if POSTID == 1:
			posttype = "Question"
		elif POSTID == 2:
			posttype = "Answer"
		else:
			posttype = "Others"	
		return posttype


	def getDateQuarter(self):
		proclist = self.inputString.split(maxsplit=4)
		DATETIME = ((proclist[3].split("=")[1]))#string manipulation
		calendarList = (DATETIME.split("T")[0]).split("-") #string manipulation
		MONTH =int(calendarList[1])
		#declares quarter using if-else chain
		if MONTH <= 3 :
			QUARTER = "Q1"
		elif MONTH <= 6 and MONTH > 3 :
			QUARTER = "Q2"
		elif MONTH <= 9 and MONTH>6:
			QUARTER = "Q3"
		else:
			QUARTER ="Q4"
		YEAR = (calendarList[0])[1:] #string manipulation to retrieve year
		yearq = YEAR + QUARTER #fromatting return string
		return yearq

	def getCleanedBody(self):
		line = rid_tags(preprocessLine(self.inputString))
		#removes tags and preprocesses
		line = line[2:-6]
		#cleans extra whitespace
		return line
		

	def getVocabularySize(self):
		forbidden = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','','\n']
		vocabline = self.getCleanedBody() #fetches cleaned body value from previous function
		vocablist = vocabline.split(" ") #splits words
		for elements in vocablist: #to remove additional characters from end of elements
			insertindex =vocablist.index(elements)
			vocablist.remove(elements)
			
			for symbols in forbidden:
				if symbols in elements:
					elements = elements.replace(symbols,"")
			vocablist.insert(insertindex,elements)
		#lowercasing and adding to new list
		newlist = []
		for newelements in vocablist:
			newelements = newelements.lower()

			if newelements not in newlist and len(newelements)!=0:
				newlist.append(newelements)
		return(len(newlist)) #returning vocabulary size
