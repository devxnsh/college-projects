from pprint import pprint
def rid_tags(mainstr,delim1="<",delim2=">"): 
	#separate function to detect and delete substring between two specific points
	#checks for delim1 (first point of entry) and starts counting indexes
    while delim1 in mainstr and delim2 in mainstr[mainstr.index(delim1):]:
        index1 = mainstr.index(delim1)
        reststr = mainstr[index1:] #rest of the string
        index2 = index1 + reststr.index(delim2) #recognizing endpoint of substring to be deleted
        deletestr = mainstr[index1:index2+1]
        mainstr = mainstr.replace(deletestr,"") #deletes recognized substring.
    return mainstr

def defile(filename):
	#creates file if it doesnt exist. clears data if it exists
	defi = open(filename,"w",encoding="utf-8")
	defi.writelines("")
	defi.close()
def preprocessLine(inputLine):
	inputLine=inputLine.replace("&amp;","&")  #changes &amp; to &
	inputLine=inputLine.replace("&quot;","\"") #changes &quot; to "
	inputLine=inputLine.replace("&apos;","'")#changes &apos; to '
	inputLine=inputLine.replace("&gt;",">")#changes &gt; to >
	inputLine=inputLine.replace("&lt;","<")#changes &lt; to <
	inputLine=inputLine.replace("&#xA;"," ")#changes &#xA; to <spacebar>
	inputLine=inputLine.replace("&#xD;"," ")#changes &#xD; to <spacebar>
	inputLine=inputLine.replace("row Id","row_id")#changes row Id; to row_id to autosplit properly
	inputLine=inputLine.replace("&amp;","&")#changes &amp; to & 
	
	return inputLine

def splitFile(inputFile, outputFile_question, outputFile_answer):
	defile(outputFile_question) #creating/clearing question output file
	defile(outputFile_answer) #creating/clearing answer output file

	fh = open(inputFile,"r", encoding="utf-8") #inputFile
	filedata = fh.readlines() #reading file data. returns a list
	pointer=5
	while pointer<len(filedata)-1: #looping filedata
		fileline = filedata[pointer] #filedata is a list where each line is an element. this selects individual line using loop
		processedfileline = preprocessLine(fileline) #processing line 
		elementList = processedfileline.split(maxsplit=3)	#splitting line into 4 elements, row_id, PostTypeID, CreationDate and Body
		elementList = cleanlist(elementList) #recleans list
		postTypeIDequals = elementList[1] #post type id element 1 : question 2: answer 3-9 : others
		
		posttypestr = (postTypeIDequals.split("=")) #splits second element (post type ID) into two elements, the second one being the ID itself
		fileelementer = (posttypestr[1]) #separates quote marks from number 
				
		PostTypeID = int(fileelementer[-2]) #typecasts string to number
		elementbody = elementList[3] #third element of list from line, 
		elementdesc = (elementbody[6:-6]) #string manipulation to make body element
			
		if PostTypeID == 1: #post type id
			
			questioner = open("question.txt","a",encoding="utf-8")
			questioner.writelines(elementdesc) #writing element into question file
			questioner.writelines("\n") #change line
		if PostTypeID == 2:
			
			answerer = open("answer.txt","a",encoding="utf-8")
			answerer.writelines(elementdesc) #writing elemeent into answer file
			answerer.writelines("\n") #change line
		pointer+=1


def cleanlist(elementList): #purpose is to clean each element of tags individually, not disturbing xml tag structure
	for element in elementList:
		indexer = elementList.index(element) #stores index
		elementList.remove(element) #removes element from list
		element = preprocessLine(element) #leftover cleanup
		element=(rid_tags(element)) #removes tags from element (mostly in body element)
		elementList.insert(indexer,element) #re-adds element into list
	return elementList

if __name__ == "__main__":
	
	f_data = "data.xml"
	f_question = "question.txt"
	f_answer = "answer.txt"

	splitFile(f_data, f_question, f_answer)

