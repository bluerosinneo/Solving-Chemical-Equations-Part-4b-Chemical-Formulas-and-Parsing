# This code follows the following post.
# http://cramerexplainsmath.com/2018/01/07/solving-chemical-equations-part-4b-chemical-formulas-and-parsing/
# @desc This class is used to read and store a chemical formula
# into a dictionary.  A detailed description can be found in the post
# @author Cramer Grimes cramergrimes@gmail.com


class chemicalFormula:

	def __init__ (self):
		self.elementDict = {}
		self.formulaCoef = 1
		self.origFormula = ""

	def addElement(self,elementSym,numElement):
		if (elementSym in self.elementDict):
			self.elementDict[elementSym] = self.elementDict[elementSym] + numElement
		else:
			self.elementDict[elementSym] = numElement

	def lookNum(self,formulaText,loc):
		numElement = ""
		while(loc['i']<len(formulaText) and formulaText[loc['i']].isdigit()):
			numElement = numElement + formulaText[loc['i']]
			loc['i']=loc['i']+1
		if(len(numElement)>0):
			return int(numElement)
		else:
			return 1

	def lookNextElement(self,formulaText,loc,formulaSubscript):
		if(formulaText[loc['i']].isupper()):
			if((loc['i']+1)<len(formulaText) and formulaText[loc['i']+1].islower()):
				elSym = formulaText[loc['i']]+formulaText[loc['i']+1]
				loc['i']=loc['i']+2
				numElement=self.lookNum(formulaText,loc)
				self.addElement(elSym,(numElement*formulaSubscript))
				return
			else:
				elSym = formulaText[loc['i']]
				loc['i']=loc['i']+1
				numElement=self.lookNum(formulaText,loc)
				self.addElement(elSym,(numElement*formulaSubscript))
				return
		loc['i']=loc['i']+1

	def readFormula(self,formulaText,formulaSubscript):
		if(self.origFormula == ""):
			self.origFormula = formulaText
		if(self.findDot(formulaText)!=False):
			formulaText=self.breakDot(formulaText,formulaSubscript)
		if(self.findBrackOrPeren(formulaText)!=False):
			formulaText=self.breakInnerOuter(formulaText,formulaSubscript)
		loc = {'i' : 0}
		while (loc['i']<len(formulaText)):
			self.lookNextElement(formulaText,loc,formulaSubscript)

	def findBrackOrPeren(self,formulaText):
		if(('[' in formulaText) and (']' in formulaText)):
			return True
		elif(('(' in formulaText) and (')' in formulaText)):
			return True
		else:
			return False

	def breakInnerOuter(self,formulaText,formulaSubscript):
		formulaText=formulaText.replace('[','(')
		formulaText=formulaText.replace(']',')')
		start=formulaText.find('(')
		end=formulaText.rfind(')')
		loc = {'i': (end +1)}
		innerSubscript = self.lookNum(formulaText,loc)
		self.readFormula(formulaText[start+1:end],(formulaSubscript*innerSubscript))		
		beforeText = formulaText[:start]
		if(loc['i']<len(formulaText)):
			afterText = formulaText[loc['i']:]
		else:
			afterText = ""
		return beforeText + afterText

	def findDot(self,formulaText):
		if('.' in formulaText):
			return True
		else:
			return False

	def breakDot(self,formulaText,formulaSubscript):
		dotLocation = formulaText.find('.')
		loc = {'i': (dotLocation+1)}
		dotCoef = self.lookNum(formulaText,loc)
		if(loc['i']<len(formulaText)):
			self.readFormula(formulaText[loc['i']:],(formulaSubscript*dotCoef))
		return formulaText[:dotLocation]