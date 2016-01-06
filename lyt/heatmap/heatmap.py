import copy

# data: 2014-6-06 08:00:16,1591741,check-in,63,99

def getHour(data):
	res=data.split(" ")[1].split(":")[0]
	return int(res)

# print getHour("2014-6-06 08:00:16")


fo=open("res.txt","w+")

f=open("sun.csv","r")
line=f.readline()
line=f.readline()
total=0

mapDic={}
formPos={}

data=[[0 for x in range(100)] for y in range(100)]

end=24;


# 2d-array and deepcopy test
# data=[[0 for x in range(100)] for y in range(100)]
# data[0][0]=1
# mapDic["a"]=copy.deepcopy(data)
# data[0][0]=100
# mapDic["b"]=copy.deepcopy(data)
# print mapDic["a"][0][0]
# print mapDic["b"][0][0]

for i in range(8,end):
	# if i!=9:
	# 	data=copy.deepcopy(mapDic[i-1])
	while line:
		tmp=line.split(",")
		#check time
		hour=getHour(tmp[0])
		if hour<i:
			continue
		if hour>i:
			break

		#get data
		fe.writelines(tmp[0]+"\n")
		user=tmp[1]
		x=int(tmp[3])
		y=int(tmp[4])
		cordx=0
		cordy=0

		if user in formPos:
			cordx=formPos[user][0]
			cordy=formPos[user][1]
			data[cordx][cordy]-=1
		else:
			total+=1

		data[x][y]+=1
		formPos[user]=[x,y]
		
		# fo.writelines(line)
		line=f.readline()
	mapDic[i]=copy.deepcopy(data)

f.close()


res=""

# print len(mapDic[8][0])
# print total
fo.writelines("{\n");
for i in range(8,end):
	arr=mapDic[i]
	flag=False
	fo.writelines("\""+str(i+1)+"\":[")
	for j in range(0,100):
		for k in range(0,100):
			if arr[j][k]!=0:
				if flag==False:
					res="["+str(j*10)+","+str(k*10)+","+str(arr[j][k])+"]\n"
					flag=True
				else:
					res=",["+str(j*10)+","+str(k*10)+","+str(arr[j][k])+"]\n"
				fo.writelines(res)
				res=""
	fo.writelines("]");
	if i!=(end-1):
		fo.writelines(",\n")
fo.writelines("}\n");
fo.close()



