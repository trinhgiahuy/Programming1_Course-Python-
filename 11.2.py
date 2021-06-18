# # class ClassName(object):
	
# # def __init__(self, arg):
# # 		super(ClassName, self).__init__()
# # 		self.arg = arg
# # 		

# # class Song(object):
# # 	def __init__(self,lyrics):
# # 		self.lyrics=lyrics
# # 	def sing_me_a_song(self):
# # 		for line in self.lyrics:
# # 	 		print(line)


#_________________________________________________________________
# # happy_bday = Song(["Happy birthday to you",
# # 	 	"I don't want to get sued",
# # 	 	"So I'll stop right there"])

# # bulls_on_parade = Song(["They rally around the family",
# # 	 	"With pockets full of shells"])

# # happy_bday.sing_me_a_song()

# # bulls_on_parade.sing_me_a_song()
# class ConCho:
# 	def __init__(self,ten):
# 		self.ten=ten
# 	def sua(self):
# 		print("Gâu gâu %s"%(self.ten))

# A=ConCho("Huy")
# print(A.sua)

#__________________________________________________________________
class SoPhuc:

	def __init__(self,r,i):
    	self.phanthuc=r
    	self.phanao=i

     def getData(self):
        print("{}+{}j".format(self.phanthuc,self.phanao))

c1=SoPhuc(2,3)
c1.getData()

