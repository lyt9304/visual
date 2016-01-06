import copy

initCnt={
	"Thrill Rides":0,
	"Kiddie Rides":0,
	"Rides For Everyone":0,
	"Shows & Entertainment":0,
	"Information & Assistance":0,
	"Shopping":0,
	"Entrance":0,
	"Total":0
}

entrance=[
    [
      0,
      67
    ],
    [
      99,
      77
    ],
    [
      63,
      99
    ]
]

facility={
  "Thrill Rides": [
    [
      16,
      66
    ],
    [
      47,
      11
    ],
    [
      86,
      44
    ],
    [
      45,
      24
    ],
    [
      38,
      90
    ],
    [
      27,
      15
    ],
    [
      69,
      44
    ],
    [
      17,
      43
    ],
    [
      78,
      48
    ]
  ],
  "Kiddie Rides": [
    [
      82,
      80
    ],
    [
      79,
      89
    ],
    [
      87,
      81
    ],
    [
      81,
      77
    ],
    [
      76,
      88
    ],
    [
      73,
      79
    ],
    [
      79,
      87
    ],
    [
      83,
      88
    ],
    [
      85,
      86
    ],
    [
      73,
      84
    ],
    [
      92,
      81
    ]
  ],
  "Rides For Everyone": [
    [
      17,
      67
    ],
    [
      23,
      54
    ],
    [
      48,
      87
    ],
    [
      60,
      37
    ],
    [
      43,
      56
    ],
    [
      28,
      66
    ],
    [
      34,
      68
    ],
    [
      26,
      59
    ],
    [
      87,
      48
    ],
    [
      43,
      78
    ],
    [
      78,
      37
    ],
    [
      67,
      37
    ],
    [
      42,
      37
    ],
    [
      6,
      43
    ]
  ],
  "Shows & Entertainment": [
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
  ],
  "Information & Assistance": [
    [
      50,
      57
    ]
  ],
  "Shopping": [
    [
      16,
      49
    ]
  ]
  # "Restrooms": [],
  # "Beer Gardens": [],
  # "Food": [],
  
}


userMap={}
initMap={
	"Thrill Rides":0,
	"Kiddie Rides":0,
	"Rides For Everyone":0,
	"Shows & Entertainment":0,
	"Information & Assistance":0,
	"Shopping":0,
	"tcheck":0,
	"etime":0,#entertainment time
	"ttime":0,#total time
	"lasttype":False,#check-in:True movement:False
	"firsttime":0,#firsttime
	"lasttime":0#lasttime
}

def getTime(stime):
	tmp=stime.split(" ")[1].split(":")
	res=int(tmp[0])*3600+int(tmp[1])*60+int(tmp[2])
	return res


fo=open("timetypeForFri.txt","w+")
f=open("fri.csv","r")

line=f.readline()
line=f.readline()

# for i in range(0,50000):
while line:
	stmp=line.rstrip()
	tmp=stmp.split(",")
	stime=tmp[0]
	id=tmp[1]
	type=tmp[2]
	x=int(tmp[3])
	y=int(tmp[4])
	time=getTime(stime)

	if id not in userMap:
		userMap[id]=copy.copy(initMap)
		userMap[id]["firsttime"]=time

	if type == "check-in":
		userMap[id]["tcheck"]+=1
		initCnt["Total"]+=1
		userMap[id]["lasttime"]=time
		if [x,y] in entrance:
			userMap[id]["lasttype"]=False
			initCnt["Entrance"]+=1
			line=f.readline()
			continue
		if [x,y] in facility["Thrill Rides"]:
			userMap[id]["lasttype"]=True
			userMap[id]["Thrill Rides"]+=1
			initCnt["Thrill Rides"]+=1
			line=f.readline()
			continue
		if [x,y] in facility["Kiddie Rides"]:
			userMap[id]["lasttype"]=True
			userMap[id]["Kiddie Rides"]+=1
			initCnt["Kiddie Rides"]+=1
			line=f.readline()
			continue
		if [x,y] in facility["Rides For Everyone"]:
			userMap[id]["lasttype"]=True
			userMap[id]["Rides For Everyone"]+=1
			initCnt["Rides For Everyone"]+=1
			line=f.readline()
			continue
		if [x,y] in facility["Shows & Entertainment"]:
			userMap[id]["lasttype"]=True
			userMap[id]["Shows & Entertainment"]+=1
			initCnt["Shows & Entertainment"]+=1
			line=f.readline()
			continue
		if [x,y] in facility["Information & Assistance"]:
			userMap[id]["lasttype"]=True
			userMap[id]["Information & Assistance"]+=1
			initCnt["Information & Assistance"]+=1
			line=f.readline()
			continue
		if [x,y] in facility["Shopping"]:
			userMap[id]["lasttype"]=True
			userMap[id]["Shopping"]+=1
			initCnt["Shopping"]+=1
			line=f.readline()
			continue
	else:
		if userMap[id]["lasttype"]==True:
			#count entertainment time
			userMap[id]["etime"]+=(time-userMap[id]["lasttime"])
		userMap[id]["lasttype"]=False
		userMap[id]["lasttime"]=time
		line=f.readline()	
f.close()

params={
	"avgTtime":0,
	"avgEtime":0,
	"totalPeople":0,
	"maxTtime":0,
	"minTtime":100000,
	"maxEtime":0,
	"minEtime":100000,
	"totalPeople":0,
	"avgET":0,
	"maxET":0,
	"minET":100000,
	"thrill":0,
	"kiddie":0,
	"normal":0,
	"other":0,
	"nothing":0,
	"TtimeArr":[0,0,0,0,0,0,0,0,0],
	"EtimeArr":[0,0,0,0,0,0,0],
	"ETArr":[0,0,0,0,0,0,0,0,0]
}


for key in userMap:
	ttime=(userMap[key]["lasttime"]-userMap[key]["firsttime"])/60.0
	etime=userMap[key]["etime"]/60.0

	userMap[key]["ttime"]=ttime
# 	# if ttime!=0:
	etrate=etime/ttime
# 	# else:
# 	# 	etrate=
# 	userMap[key]["etrate"]=etrate
	params["avgTtime"]+=ttime
	params["avgEtime"]+=etime
	params["totalPeople"]+=1
	params["avgET"]+=etrate
	params["TtimeArr"][int(ttime/100)]+=1
	params["EtimeArr"][int(etime/100)]+=1
	params["ETArr"][int(etrate*10)]+=1

	if ttime>params["maxTtime"]:
		params["maxTtime"]=ttime
	if ttime<params["minTtime"]:
		params["minTtime"]=ttime
	if etime>params["maxEtime"]:
		params["maxEtime"]=etime
	if etime<params["minEtime"]:
		params["minEtime"]=etime
	if etrate>params["maxET"]:
		params["maxET"]=etrate
	if etrate<params["minET"]:
		params["minET"]=etrate

	#which type
	# "Thrill Rides":0,
	# "Kiddie Rides":0,
	# "Rides For Everyone":0,
	# "Shows & Entertainment":0,
	# "Information & Assistance":0,
	# "Shopping":0,

	if etime==0:
		userMap[key]["type"]="nothing"
		params["nothing"]+=1
	else:
		thrillCnt=userMap[key]["Thrill Rides"]
		kiddieCnt=userMap[key]["Kiddie Rides"]
		normalCnt=userMap[key]["Rides For Everyone"]
		otherCnt=userMap[key]["Shows & Entertainment"]+userMap[key]["Information & Assistance"]+userMap[key]["Shopping"]

		cnt=max(thrillCnt,kiddieCnt,normalCnt,otherCnt)

		if cnt==thrillCnt:
			userMap[key]["type"]="thrill"
			params["thrill"]+=1
		if cnt==kiddieCnt:
			userMap[key]["type"]="kiddie"
			params["kiddie"]+=1
		if cnt==normalCnt:
			userMap[key]["type"]="normal"
			params["normal"]+=1
		if cnt==otherCnt:
			userMap[key]["type"]="other"
			params["other"]+=1

params["avgTtime"]=params["avgTtime"]/params["totalPeople"]
params["avgEtime"]=params["avgEtime"]/params["totalPeople"]
params["avgET"]=params["avgET"]/params["totalPeople"]
	

fo.writelines(str(userMap))
fo.writelines("\n=============\n")
fo.writelines(str(initCnt))
fo.writelines("\n=============\n")
fo.writelines(str(params))

fo.close()
