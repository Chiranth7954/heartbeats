import json

#bpm = input("Input beats per minute: ")
#genre = input("Input Genre: ")
#workoutLength = input("Input workout length: ")

userBPM = 140
genre = "rock"
userLength = 15 * 60
type = "ramping"


with open('song.json') as songData:
	data = json.load(songData)

length = 0.0
songBPM = 0
i = 1

with open('songlist.txt', 'w+') as songList:

	if type == "linear":
	
		for i in [1,len(data)]:	
		
			if abs(float(data["song" + str(i)]["bpm"]) - userBPM) < 5 and length < userLength and data["song" + str(i)]["genre"] == genre:
			
					songName = data["song" + str(i)]["song"]
					songArtist = data["song" + str(i)]["artist"]
					songLength = data["song" + str(i)]["time"]
					songLength = songLength.split(":")
					songLength = float(songLength[0]) + (float(songLength[1]) / 60.0)
					songList.write("%s, %s\n" % (songArtist, songName))
				
			elif length > userLength:
				break

	elif type == "ramping":
	
		while i <= len(data):
					
			#print(length, userLength / 2.0)
			#print(i)
			#print(abs(float(data["song" + str(i)]["bpm"])) - userBPM < 5)
			
			if (abs(float(data["song" + str(i)]["bpm"]) - userBPM) < 5) and (length < (userLength / 2.0)) and data["song" + str(i)]["genre"] == genre:
			
				songName = data["song" + str(i)]["song"]
				songArtist = data["song" + str(i)]["artist"]
				songLength = float(data["song" + str(i)]["time"])
				songBPM = float(data["song" + str(i)]["bpm"])
				length += songLength
				songList.write("%s %s\n" % (songName, songArtist))

				userBPM += 10
				
				#print("Next bpm range = %d to %d" % (userBPM - 5, userBPM + 5))
				#print("Current length = %.3f" % length)
				#print("increasing ", length)
			
			elif (abs(float(data["song" + str(i)]["bpm"]) - userBPM) < 5) and (length > (userLength / 2.0)) and (length < userLength) and data["song" + str(i)]["genre"] == genre:
					
				songName = data["song" + str(i)]["song"]
				songArtist = data["song" + str(i)]["artist"]
				songBPM = float(data["song" + str(i)]["bpm"])
				songLength = float(data["song" + str(i)]["time"])
				length += songLength
				songList.write("%s %s\n" % (songName, songArtist))
				
				userBPM -= 10
				
				#print("Next bpm range = %d to %d" % (userBPM - 5, userBPM + 5))
				#print("Current length = %.3f" % length)
				#print("decreasing")

			elif length > userLength:
				#print("too long")
				break
			
			i += 1
			
				

