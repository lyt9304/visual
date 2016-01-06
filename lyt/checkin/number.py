import copy

# data: 2014-6-06 08:00:16,1591741,check-in,63,99

shows=[
    [
      32,
      33
    ],
    [
      87,
      63
    ],
    [
      76,
      22
    ]
]

def getTimeArea(shour,sminute):
	h=int(shour)
	sh=str(h)
	m=int(sminute)

	# t=m/15

	# if t==0:
	# 	res=sh+":00"
	# 	return res
	# if t==1:
	# 	res=sh+":15"
	# 	return res
	# if t==2:
	# 	res=sh+":30"
	# 	return res
	# if t==3:
	# 	res=sh+":45"
	# 	return res

	t=m/30

	if t==0:
		res=0
		return res
	if t==1:
		res=1
		return res

	

fo=open("numberForFri.txt","w+")
f=open("fri.csv","r")

checkMap={

}

line=f.readline()
line=f.readline()

while line:
	stmp=line.rstrip()
	tmp=stmp.split(",")
	id=tmp[1]
	type=tmp[2]
	x=int(tmp[3])
	y=int(tmp[4])

	if type=="check-in" and [x,y] in shows:
		shour=tmp[0].split(" ")[1].split(":")[0]	
		sminute=tmp[0].split(" ")[1].split(":")[1]
		res=getTimeArea(shour,sminute)

		if shour not in checkMap:
			checkMap[shour]=[0,0]
		
		checkMap[shour][res]+=1

	line=f.readline()	
f.close()

# max=0
# maxkey=""
# for key in checkMap:
# 	if checkMap[key]>max:
# 		max=checkMap[key]
# 		maxkey=key


fo.writelines(str(checkMap))
# fo.writelines(str("\n========\n"))
# fo.writelines(maxkey+" "+str(max))
fo.close()

