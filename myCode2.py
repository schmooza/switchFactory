from dataclasses import dataclass
from abc import abstractmethod, ABC

class BaseClass(ABC):
	CLASS_CONSTANT1 = 1
	
	@abstractmethod
	def __init__(self, factoryType):
		self.factoryType = factoryType
	
	@abstractmethod
	def setter(self, newVal):
		self.factoryType = newVal
	
	@abstractmethod
	def getter(self):
		print(self.factoryType)
		return self.factoryType
	
class Factory(BaseClass):
	
	def __init__(self,factoryType):
		#super lets the class reuse the init from BaseClass. Note that self is only written once.
		super().__init__(factoryType)
	
	def setter(self, newVal):
		self.factoryType = newVal
	
	def getter(self):
		print("The specific factory type is",self.factoryType)
		
		return self.factoryType
	@staticmethod
	def makeNew(typeOfFactory):
		if typeOfFactory == 1:
			return Shoes(Factory)
		
		if typeOfFactory == 2:
			return Keywords([],[],{})
	

class Shoes(Factory):

	def size(self):
		pass
	
	def testIt(self):
		print("it works")


	

		
interfaceForFactory = Factory(None)
x = interfaceForFactory.makeNew(1)
x.testIt()
x.setter("sexy shoes")
x.getter()



def testIt():

	print("it works")
	
@dataclass
class Keywords(Factory):
	
	#inherits from factory
	
	remembersFacts: list[""]
	doesHomework: list[""]
	listensToFeedback: dict
	
	def setData(self,whichDataType, *args, **kwargs):
		
		match whichDataType:
			case 1:
				blist = list(args)
				Keywords.remembersFacts = blist
			
			case 2:
				blist = list(args)
				Keywords.doesHomework = blist
			case 3:
				Keywords.listensToFeedback = kwargs
				
			case _:
				print("error")
	
	def getData(self, whichDataType):
		
		match whichDataType:
			case 1:
				print(Keywords.remembersFacts, type(Keywords.remembersFacts))
			case 2:
				print (Keywords.doesHomework)
			case 3:
				print(Keywords.listensToFeedback, type(Keywords.listensToFeedback))
				
			case _:
				print("error")
	def addData(self, newData, *args, **kwargs):
		match newData:
			case 1:
				# for some reason python likes immutable data
				# and forces lists to become tuples when using args.
				# thus I convert back to a list. might cause errors later.
				
				#tuple to list
				blist = list(args)
				
				#list to strings
				for i in blist:
					#pack back into a list
					Keywords.remembersFacts.append(i)

				
				print(Keywords.remembersFacts)


				
			case 2:
				Keywords.doesHomework.append(args)
			case 3:
				for key, value in kwargs.items():
					print("key",key )
					print("value",value)
					Keywords.listensToFeedback[key]= value
				# print(Keywords.listensToFeedback)
			
			case _:
				print("error")
		
		

		
z = interfaceForFactory.makeNew(2)
z.setter("student gradation")
z.getter()
z.setData(1,"figs")
z.getData(1)
z.setData(2,"fogs")
z.getData(2)

# with the dictionary, you have to construct it. You can't just pass in a dictionary
# thus the "key": argument is changed to key = value, like a standard variable.
# kind of makes me realise what is happening with a standard variable. lol.

z.setData(3,keyOne = 23, keyTwo = 25)

z.getData(3)
z.addData(3, test = 34)
z.getData(3)
z.addData(1,"cat piss")
z.getData(1)







	
	
	