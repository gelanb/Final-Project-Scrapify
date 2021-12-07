from TikTokApi import TikTokApi #https://www.youtube.com/watch?v=zwLmLfVI-VQ 
from datetime import datetime

verifyFp = "verify_kw059zgm_J3QMpD65_PdDu_4PSK_9AuZ_5tpjUziA23u9" #went to tiktoks website, lockicon, www.tiktok.com, cookies, web Id, content. 

api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

hashtaginput = input("Enter a hashtag: ") #Videos that contain this hashtag
countinput = int(input("How many videos do you want to see? ")) #how many videos to show
likes = int(input("What is the least amount of likes it should have? "))  
tiktoks = api.by_hashtag(hashtag=hashtaginput, count=countinput)
myDict = {}
for tiktok in tiktoks:
    url = tiktok['video']['playAddr'] #The Url of the video
    videoLikes = tiktok['stats']['diggCount'] #The number of views it has.
    post_time = tiktok['createTime']
    if videoLikes >= likes: #If the video has this at least this many views
        data = {tiktok['video']['playAddr']:tiktok['stats']['diggCount']} #This creates a dictionary in the order of video and how many likes it has.
        for key, val in data.items(): #This iterates through the keys and value and sets them in the dictionary.
            myDict[key]= val

myDict = sorted(myDict.items(), key=lambda x: x[1], reverse=True)#This sorts the dictionary from highest views to lowest because it's reversed.
print(myDict)

#Up to now: Gets hashtag, gets how many likes it has to have, and shows it the order from highest to lowest.


#Trying to iterate through the html and add videos from the python myDict.
""" 
with open("website.html", "r") as html_file:
    html_file = html_file.readlines()
    lines = []
    for line in html_file:
        if line.startswith('src='):
            line.insert(4,"TEST")
            lines.append(''.join(line) + '\n')
        else:
            lines.append(line)
with open("website.html", "w") as html_file:
    for line in lines:
        html_file.write(line)
print(html_file)
"""

# A way to integrate time into the app, enabling the tiktoks to show in most recently posted.

"""
today = datetime.datetime.today()
createTime = int('1587512910') #https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
timeStamp = (datetime.utcfromtimestamp(createTime).strftime('%Y-%m-%d'))#converts the tiktoktime to readable time.
find all the time from the tiktoks, turn them to a timestamp, add them as a value to the dictionary, sort them in order of most liked recent time 
"""