def createYoutubeVideo(title, description, hashtags):
	vidDict = {"title": title, "description": description, "likes": 0, "dislikes":0, "comments":{}, "hashtags": hashtags}
	return vidDict

def like(youtubeVidDict):
	if "likes" in youtubeVidDict:
		youtubeVidDict["likes"] += 1
	return youtubeVidDict

def dislike(youtubeVidDict):
	if "dislikes" in youtubeVidDict:
		youtubeVidDict["likes"] += 1
	return youtubeVidDict

def addComment(youtubeVidDict, username, commentText):
	youtubeVidDict["comments"][username] = commentText
	return youtubeVidDict

def compare(num1,num2):
	if ((num1>num2) and (num1 != 0)):
		return num1
	elif (num2 != 0):
		return num2
	else:
		return 1

def percentSimiliarityToVideo(vid1, vid2):
	counter = 0
	lenVid1 = len(vid1)
	for i in vid1["hashtags"]:
		for x in vid2["hashtags"]:
			if i == x:
				counter+=1
	if ((counter>=len(vid1)) or (counter>=len(vid2))):
		return 100
	else:
		similiarityDec = counter/compare(len(vid1),len(vid2))
		similiarityPerc= similiarityDec*100
		return similiarityPerc

		


youtubeVid = createYoutubeVideo("suffering", "hell", ["#cool", "#dangerous"])
youtubeVid2 = createYoutubeVideo("suffering", "hell", ["#cool", "#dangerous", "#lame", "#trash", "#limp"])
youtubeVid = like(youtubeVid)
youtubeVid = dislike(youtubeVid)
youtubeVid = addComment(youtubeVid, "Reeman127", "best vid")
print("The videos are " + str(int(percentSimiliarityToVideo(youtubeVid, youtubeVid2))) + "% similiar")


print(youtubeVid)
