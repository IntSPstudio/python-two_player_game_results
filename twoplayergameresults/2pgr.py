#|==============================================================|#
# Made by IntSPstudio
# Two Player Game Results
# Thank you for using this software!
# Version: 0.0.7.20170309
# ID: 980005010
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import sys
import it8c
import datetime
#MAIN CONTENT CHECK
def getContentCheck(array1Content):
	#LIMITS
	array1Height = len(array1Content)
	array1Width =  len(array1Content[0])
	array2Height =1
	array2Width =3
	#CONTENT
	ypb =1
	if array1Width > 2:
		for i in range(0, 2):
			if i == 1:
				if array2Height > 1:
					array2Content = it8c.dataCreateArray(array2Height,array2Width,"")
			for ypa in range(0, array1Height):
				if ypa == 0:
					if i == 1:
						checka = it8c.lettersdigits(array1Content[0][0],"")
						checkb = it8c.lettersdigits(array1Content[0][1],"")
						if checka !="":
							array2Content[0][0] = array1Content[0][0]
						if checkb !="":
							array2Content[0][1] = array1Content[0][1]
				else:
					checka = it8c.lettersdigits(array1Content[ypa][0],"")
					checkb = it8c.lettersdigits(array1Content[ypa][1],"")
					checkc = it8c.lettersdigits(array1Content[ypa][2],"")
					if checkc =="":
						array1Content[ypa][2] = "Class "+ str(ypa)
					if checka !="" and checkb !="":
						if i == 0:
							array2Height +=1
						if i == 1:
							array2Content[ypb][0] = int(array1Content[ypa][0])
							array2Content[ypb][1] = int(array1Content[ypa][1])
							array2Content[ypb][2] = array1Content[ypa][2]
							ypb +=1
		return array2Content
#GET PLAYER NAME
def getPlayerName(array1Content,array1Line):
	point = array1Content[0][array1Line]
	output ="player "+ str(array1Line)
	if point != "":
		output = point
	return output
#EXTRACT CONTENT LINE
def extractContentLine(array1Content,array1Line):
	#LIMITS
	array1Height = len(array1Content)
	array1Width =  len(array1Content[0])
	array2Width = array1Height -1
	array2Content = it8c.dataCreateList(array2Width,"")
	#CONTENT
	for yp in range(1, array1Height):
		for xp in range(0, array1Width):
			if xp == array1Line:
				array2Content[yp -1] = array1Content[yp][xp]
	return array2Content
#ROUNDS WIN RATE
def getRoundsWinRate(array1Content):
	#LIMITS
	array1Height = len(array1Content)
	array1Width =  len(array1Content[0])
	array2Width = 2
	array2Content = it8c.dataCreateList(array2Width,0)
	#CONTENT
	for yp in range(0, array1Height):
		if yp > 0:
			pointa = int(array1Content[yp][0])
			pointb = int(array1Content[yp][1])
			checka = it8c.checkIfItIsNumber(pointa)
			checkb = it8c.checkIfItIsNumber(pointb)
			if checka == 1 and checkb == 1:
				if pointa > pointb:
					array2Content[0] +=1
				elif pointb > pointa:
					array2Content[1] +=1
	return array2Content
#START
if __name__ == "__main__":
	#INPUT
	scrFile = sys.argv[0]
	scrArg =""
	scrRuleTest = len(sys.argv)
	fileDefSep = ";"
	#OUTPUT
	fileSaveResults =0
	fileNameO =""
	fileDefFormat =".csv"
	if scrRuleTest > 1:
		scrArg = str(sys.argv[1])
		if scrArg !="":
			fileNameI = scrArg
			clDate = datetime.datetime.now()
			if scrRuleTest > 2:
				scrArg = str(sys.argv[2])
				if scrArg !="":
					fileSaveResults =1
					if scrArg == "default":
						fileNameO = str(clDate.year) + str(clDate.month) + str(clDate.day) + str(clDate.hour) + str(clDate.minute) + str(clDate.second) + fileDefFormat
					else:
						fileNameO = str.lower(scrArg)
			if it8c.fileTextExists(fileNameI) == 1:
				#INPUT
				rawArrayContent = it8c.csvReadFile(fileNameI, fileDefSep)
				mainArrayContent = getContentCheck(rawArrayContent)
				#CLASSES
				classRawContent = extractContentLine(mainArrayContent,2)
				classRefContent = it8c.dataExtractArrayColumn(it8c.dataCheckListObjects(it8c.dataChangeListContentFormat(it8c.dataChangeListContentFormat(classRawContent,1),3)),2)
				classRounds = len(classRawContent)
				classCounter = len(classRefContent)
				classWinRate = getRoundsWinRate(mainArrayContent)
				#CONTENT ARRAY
				printContent = it8c.dataCreateArray(7,5,"")
				#TITLE
				printContent[0][0] ="Name"
				printContent[1][0] ="Total"
				printContent[2][0] ="Avarage"
				printContent[3][0] ="Rounds won"
				posa =1
				for i in range(0,2):
					#CONTENT
					playerContent = extractContentLine(mainArrayContent,i)
					#NAME
					printContent[0][posa] = getPlayerName(mainArrayContent,i)
					#TOTAL
					printContent[1][posa] = int(it8c.dataCalcSumList(playerContent))
					#AVARAGE
					printContent[2][posa] = int(it8c.dataCalcAvgList(playerContent))
					#WIN RATE
					printContent[3][posa] = classWinRate[i]
					printContent[3][posa +1] = str(int(classWinRate[i] / classRounds *100)) +"%"
					posa +=2
				#OTHER
				printContent[5][0] ="Rounds"
				printContent[5][1] = classRounds
				if classRounds != classCounter:
					printContent[6][0] ="Classes"
					printContent[6][1] = classCounter
				print(it8c.vslTerminalLine(0,""))
				print(it8c.dataSmrPrintArray(printContent," ","",0))
				if fileSaveResults == 1:
					it8c.csvWriteFile(printContent,fileNameO,";","")
			else:
				print("File doesn't exists")
	else:
		print("Give a filename")