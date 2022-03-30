from pytube import YouTube
import traceback
import time

#def progress_check(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
 #   percent = (100*(file_size-remaining))/file_size
 #   print("{:00.0f}% downloaded".format(percent))


def Download_Video(link,quality,save_path):
	try:
		yt = YouTube(link)
		title  = yt.title
		print("Downloading : ",yt.title)
		video_type = yt.streams.filter(file_extension = "mp4" ,progressive = True) # Extension and quality(Adaptive or Progressive)

		


		if(quality == "360p"):
			stream  = yt.streams.get_by_itag(18) # Selecting Quality

		elif(quality == "720p"):
			stream  = yt.streams.get_by_itag(22) # Selecting Quality

		elif(quality == "1080p"):
			stream  = yt.streams.get_by_itag(137) # Selecting Quality

		elif(quality == "160kbps"):
			stream  = yt.streams.get_by_itag(251) # Selecting Quality

		else:
			print("Choose Correct Option")
			exit()

		#global file_size
		#file_size = stream.filesize
		
		stream.download(save_path) #Downloading to the specified path

	except:
		print("Error Occured")
		traceback.print_exc()
		exit()

	return 1


def main():
	Save_Path  = "C:\\Users\\Prati\\Desktop\\Music" 

	print("Enter/Paste Youtube video Link")
	try:
		link = input()
	except:
		print("input Error")

	print("-"*80)
	print("Choose Quality from below")
	print("480p")
	print("360p")
	print("720p")
	print("1080p")
	print("For Audio only")
	print("160kbps")
	print("-"*80)

	Quality = input()

	starttime  = time.time()

	sucess  = Download_Video(link,Quality,Save_Path)

	endtime  = time.time()

	if(sucess  == 1):
		print("Downloaded SuccessFully")
		print("Time Required to donwload: {:.2f} Minutes".format((endtime-starttime)/60))

	while(True):
		print("Enter 'Exit' to close the Application")
		str = input()
		str = str.lower()
		if(str=="exit"):
			exit()
	

if __name__ == "__main__":
	main()
