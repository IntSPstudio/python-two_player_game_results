#|==============================================================|#
# Made by IntSPstudio
# Two Player Game Results
# Thank you for using this software!
# Version: 0.0.3.20170105
# ID: 980005010
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c
#SETTINGS
fileNameI ="sample.csv"
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
#START
if __name__ == "__main__":
	if it8c.fileTextExists(fileNameI) == 1:
		#INPUT
		rawArrayContent = it8c.csvReadFile(fileNameI,";")
		#CLASSES
		classRawContent = extractContentLine(rawArrayContent,2)
		classRefContent = it8c.dataExtractArrayColumn(it8c.dataCheckListObjects(it8c.dataChangeListContentFormat(it8c.dataChangeListContentFormat(classRawContent,1),3)),2)
		classRounds = len(classRawContent)
		classCounter = len(classRefContent)
		#PLAYER 1
		player1Name = str.upper(getPlayerName(rawArrayContent,0))
		player1Content = extractContentLine(rawArrayContent,0)
		player1Total = it8c.dataCalcSumList(player1Content)
		player1Avarage = it8c.dataCalcAvgList(player1Content)
		player1Rounds = len(player1Content)
		#PLAYER 2
		player2Name = str.upper(getPlayerName(rawArrayContent,1))
		player2Content = extractContentLine(rawArrayContent,1)
		player2Total = it8c.dataCalcSumList(player2Content)
		player2Avarage = it8c.dataCalcAvgList(player2Content)
		player2Rounds = len(player2Content)
		#PRINT
		print(it8c.vslTerminalLine(0,""))
		print(player1Name)
		print("Total:", player1Total)
		print("Avarage:", player1Avarage)
		print()
		print(player2Name)
		print("Total:", player2Total)
		print("Avarage:", player2Avarage)
		print()
		if classRounds == classCounter:
			print("Rounds:", classRounds)
		else:
			print("Rounds:", classRounds)
			print("Classes:", classCounter)