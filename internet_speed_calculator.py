from tkinter import *
import speedtest

sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("600x600")

# Load the image
bg_image = PhotoImage(file="C:/Users/Muhammad suleman/Desktop/random projects/photu.png")

# Create a canvas to place the image on
canvas = Canvas(sp, width=600, height=600)
canvas.pack(fill=BOTH, expand=True)

# Place the image on the canvas
canvas.create_image(0, 0, image=bg_image, anchor=NW)

# Create the labels and buttons
lab = Label(canvas, text=" Internet Speed Test ", font=("Time New Roman",42,"bold"), bg="Black", fg="White", highlightthickness=0, highlightbackground="LightBlue")
lab.place(x=40, y=60, height=50, width=520)

lab = Label(canvas, text=" Download Speed ", font=("Time New Roman",40,"bold"), bg = "Black",fg="Red", highlightthickness=0, highlightbackground="LightBlue")
lab.place(x=40, y=150, height=50, width=520)

lab_down = Label(canvas, text="**", font=("Time New Roman",40,"bold"), highlightthickness=0, highlightbackground="LightBlue")
lab_down.place(x=40, y=220, height=50, width=520)

lab = Label(canvas, text=" Upload Speed ", font=("Time New Roman",40,"bold"), bg = "Black",fg="White", highlightthickness=0, highlightbackground="LightBlue")
lab.place(x=40, y=310, height=50, width=520)

lab_up = Label(canvas, text="**", font=("Time New Roman",40,"bold"), highlightthickness=0, highlightbackground="LightBlue")
lab_up.place(x=40, y=380, height=50, width=520)

def speedcheck():
	sp = speedtest.Speedtest()
	sp.get_servers()
	down = str(round(sp.download()/(10**6),3)) + "Mbps"
	up = str(round(sp.upload()/(10**6),3)) + "Mbps"
	lab_down.config(text = down)
	lab_up.config(text = up)

button = Button(canvas, text=" Check Speed ", font=("Time New Roman",40,"bold"), relief=RAISED, bg="RoyalBlue", command=speedcheck)
button.place(x=40, y=480, height=65, width=520)

sp.mainloop()
print("Made By Nishant And Manish Kumar")