from tkinter import *
from pytube import YouTube
from tkinter import ttk
from tkinter import messagebox
import threading
from PIL import Image,ImageTk
from tkinter import filedialog
import time

background = "#ADF2CD"

font = ("ariel",10,"bold")

count =0

condition = True

#################################            Start Function            #############################


def waiting():
    while condition:
        l1 = Label(root,text="Your Work is under Progress",font=("Adobe Gothic Std B",15,"bold"),bg="#ADF2CD")
        l1.place(x= 110 , y = 340)
        time.sleep(0.5)
        l1.place_forget()
        time.sleep(0.5)


def on_progress(stream, chunk, bytes_remaining):
    global bar,download_starting

    try:
        download_starting.place_forget()
    except:
        pass

    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100

    download_starting = Label(root,text="Downloading Video",font=("Catamaran Medium",10,"bold"))
    download_starting.place(x=150,y=520)

    bar = ttk.Progressbar(root, length=220, style='black.Horizontal.TProgressbar')
    bar.place(x=150,y=560)
    bar['value'] = percentage_of_completion
    print(percentage_of_completion)


def main(qua):
    global download_starting
    global bar
    chunk_size = 1024
    url = link_enter.get()

    print("Here1")
    try:
        yt = YouTube(url)
        video = yt.streams.filter(res=qua,mime_type="video/mp4",progressive=True).first()
    except:
        print("stream problem")


    print("Here 2")

    try:
        yt.register_on_progress_callback(on_progress)
    except:
        print("first line")
    try:
        file = filedialog.askdirectory(title="Select The Folder")
        video.download(file)
    except:
        print("second line")


    download_starting.config(text="Downloading Sucessfully Completed")
    bar['value'] = 0
    print("here 3")






def check_1080():
    youtube_1 = YouTube(link_enter.get())

    if youtube_1.streams.filter(res="1080p",mime_type="video/mp4",progressive=True).first():
        pass
    else:
        button1080["state"] = "disable"
        

def check_720():

    youtube_1 = YouTube(link_enter.get())

    if youtube_1.streams.filter(res="720p",mime_type="video/mp4",progressive=True).first():
        pass
    else:
        button_720["state"] = "disable"
        

def check_480():
    youtube_1 = YouTube(link_enter.get())

    if youtube_1.streams.filter(res="480p",mime_type="video/mp4",progressive=True).first():
        pass
    else:
        button_480["state"] = "disable"

def check_360():
    youtube_1 = YouTube(link_enter.get())

    if youtube_1.streams.filter(res="360p",mime_type="video/mp4",progressive=True).first():
        pass
    else:
        button_360["state"] = "disable"


def check_240():
    youtube_1 = YouTube(link_enter.get())

    if youtube_1.streams.filter(res="240p",mime_type="video/mp4",progressive=True).first():
        print("exist")
    else:
        button_240["state"] = "disable"




def check_144():
    youtube_1 = YouTube(link_enter.get())

    if youtube_1.streams.filter(res="144p",mime_type="video/mp4",progressive=True).first():
        pass
    else:
        button_144["state"] = "disable"




def ok():
    global link
    global condition
    global count


    try:
        option_frame.pack_forget()
    except:
        print("Not forgetting")

    start_button.config(command = threading.Thread(target=ok).start)

    if link_enter.get() == "":

        messagebox.showerror("Invaild Link","Please Paste the link")

        return False
    



##########################################################################################################



############################      Cheaking The Link is Valid or Not       ################################


    try:
        link = link_enter.get()

        youtube_1 = YouTube(link)

    except:

        messagebox.showerror("Invalid","Invalid Link")

        return False


    while count !=250:
        link_paste.place_configure(x = 150, y =320-count)
        link_enter.place_configure(x = 28, y = 370-count)
        start_button.place_configure(x= 190 , y = 400-count)
        count+=1

    threading.Thread(target=waiting).start()

    start_button['state'] = 'disable'

    threading.Thread(target=check_1080()).start
    threading.Thread(target=check_720()).start
    threading.Thread(target=check_480()).start
    threading.Thread(target=check_360()).start
    threading.Thread(target=check_240()).start
    threading.Thread(target=check_144()).start

    condition = False




##########################################################################################################
      

    option_frame.place(x=40,y=200)



    title_label = Label(mp4_frame,text = f"Video Title : {youtube_1.title}",bg="yellow")
    title_label.pack(fill = BOTH)

    title_label = Label(mp3_frame,text = f"Video Title : {youtube_1.title}",bg="yellow")
    title_label.pack(fill = BOTH)

    

###################################             Download Function            ######################################






def down_720():
    global bar,download_starting
    
    try:
        download_starting.place_forget()
    except:
        pass

    button_720.config(command=threading.Thread(target=down_720).start)
    
    try:
        main('720p')
        start_button["state"] = 'normal'

    except:
        messagebox.showerror("Not Available","This quality is not available in This video")


def down_1080():
    global bar,download_starting
    
    try:
        download_starting.place_forget()
    except:
        pass

    button1080.config(command=threading.Thread(target=down_1080).start)
    
    try:
        main('1080p')
        start_button["state"] = 'normal'

    except:
        messagebox.showerror("Not Available","This quality is not available in This video")




def down_audio1():
    global download_starting

    try:
        download_starting.place_forget()
    except:
        pass

    try:
        youtube_1 = YouTube(link_enter.get())

        youtube_1.streams.filter(only_audio=True).first().download()

        finish_label = Label(mp3_frame,text = "Download Succesful")
        finish_label.place(x=150,y=300)
    except:
        messagebox.showerror("Error","Not Able to Download")




def down_480():
    global bar,download_starting
    try:
        download_starting.place_forget()
    except:
        pass
    
    button_480.config(command=threading.Thread(target=down_480).start)
    
    try:
        main('480p')
        start_button["state"] = 'normal'

    except:
        messagebox.showerror("Not Available","This quality is not available in This video")



def down_360():
    global bar,download_starting
    try:
        download_starting.place_forget()
    except:
        pass
    
    button_360.config(command=threading.Thread(target=down_360).start)
    
    try:
        main('360p')
        start_button["state"] = 'normal'

    except:
        messagebox.showerror("Not Available","This quality is not available in This video")



def down_240():
    global bar,download_starting
    try:
        download_starting.place_forget()
    except:
        pass
    
    button_240.config(command=threading.Thread(target=down_240).start)
    
    try:
        main('240p')
        start_button["state"] = 'normal'

    except:
        messagebox.showerror("Not Available","This quality is not available in This video")



def down_144():
    global bar,download_starting
    try:
        download_starting.place_forget()
    except:
        pass
    
    button_144.config(command=threading.Thread(target=down_144).start)
    
    try:
        main('144p')
        start_button["state"] = 'normal'

    except:
        messagebox.showerror("Not Available","This quality is not available in This video")






#################################           This Function Check The Condition Of The Streams   ##############################






##################################           Graphical Section             ###########################################


root = Tk()
root.geometry('500x600')
root.resizable(0,0)
root.title("Youtube video downloader")
root["bg"] = background






start = PhotoImage(file = "start.png")

down = PhotoImage(file="download.png")
img= Image.open("Youtube.png")

resized_image= img.resize((250,50))
header= ImageTk.PhotoImage(resized_image)


Label(root,bg=background,image=header).place(x=130,y=10)


link_paste = Label(root, text = 'Paste Link Here:', font = ('Forte', 25,'bold'),bg=background)
link_paste.place(x = 150, y = 320)

link_enter = Entry(root, width = 50 ,highlightbackground="white",font=("Arial Bold",13))
link_enter.place(x = 28, y = 370)


start_button = Button(root,image = start,border=0,bg=background,command=threading.Thread(target=ok).start)
start_button.place(x= 190 , y = 400)


option_frame = Frame(root,width=320,height=400,bg = "blue")


notebook =ttk.Notebook(option_frame,width=350,height=400)
notebook.pack(expand=YES,fill=BOTH)

mp4_frame = ttk.Frame(notebook, width=200, height=280)
mp3_frame = ttk.Frame(notebook, width=200, height=280)

mp4_frame.pack(fill='both', expand=True)
mp3_frame.pack(fill='both', expand=True)




##################################       Add frames to notebook      ######################################


notebook.add(mp4_frame, text='                              MP4                            ')
notebook.add(mp3_frame, text='                              MP3                            ')


#############################################################################################################



##################################           Mp4 Section             #########################################




mp4_label = Label(mp4_frame,text="Here You Can Download MP4 Video",bg="#8D92D7")
mp4_label.pack(fill=BOTH)



##############    1080p Section ######################


label_1080p = Label(mp4_frame,text = "1080p" ,font = font).place(x=110,y=22+40)

button1080 = Button(mp4_frame,text="Download",command=threading.Thread(target=down_1080).start,image=down,border=0)
button1080.place(x=200,y=22+40)



##############    720p Section ######################


label_720p = Label(mp4_frame,text = "720p" ,font = font).place(x=110,y=60+40)

button_720 = Button(mp4_frame,text="Download",command=threading.Thread(target=down_720).start,image=down,border=0)
button_720.place(x=200,y=60+40)



##############    480p Section ######################


label_480p = Label(mp4_frame,text = "480p" ,font = font).place(x=110,y=100+40)

button_480 = Button(mp4_frame,text="Download",command=threading.Thread(target=down_480).start,image=down,border=0)
button_480.place(x=200,y=100+40)



##############    360p Section ######################

label_360p = Label(mp4_frame,text = "360p" ,font = font).place(x=110,y=140+40)

button_360 = Button(mp4_frame,text="Download",command=threading.Thread(target=down_360).start,image=down,border=0)
button_360.place(x=200,y=140+40)



##############    240p Section ######################


label_240p = Label(mp4_frame,text = "240p" ,font = font).place(x=110,y=180+40)

button_240 = Button(mp4_frame,text="Download",command=threading.Thread(target=down_240).start,image=down,border=0)
button_240.place(x=200,y=180+40)



##############    144p Section ######################


label_144p = Label(mp4_frame,text = "144p" ,font = font).place(x=110,y=220+40)

button_144 = Button(mp4_frame,text="Download",command=threading.Thread(target=down_144).start,image=down,border=0)
button_144.place(x=200,y=220+40)



#############################################################################################################



###########################################      Audio Section      ##########################################




mp4_label = Label(mp3_frame,text="Here You Can Download MP3 Audio",bg="#7B9689")
mp4_label.pack(fill=BOTH)


label_ = Label(mp3_frame,text="160kb/s" , font=font).place(x=110,y=22+40)

high_quality_audio = Button(mp3_frame,text="Download",image=down,border=0,command=threading.Thread(target=down_audio1).start)
high_quality_audio.place(x=200,y=22+40)



root.mainloop()