import pyttsx3 as ts
from PIL import Image
from time import sleep
import tkinter as tk

#img=Image.open('sharingan.png').show()

root=tk.Tk()
root.geometry('550x520')
root.minsize(485,485)
root.title('Naruto Series Dialouges')
dialouges=ts.init()
voices = dialouges.getProperty('voices')
dialouges.setProperty('voice', 'english+f11')
newVoiceRate = 145
dialouges.setProperty('rate',newVoiceRate)
name=tk.Label(text="Naruto Shippuden",font=('arial',18,'bold'),padx=10,pady=20).grid(row=1,column=2)
def naruto():
    dialouges.say('Hardwork is worthless for those that dont believe in themselves')
    waitloop()
def sasuke():
    dialouges.say('I shut my eyes a long time ago... the things I seek... now lies only in the darkness')
    waitloop()
def itachi():
    img=Image.open('ita.jpg').show()
    dialouges.say("Dont be so quick..., to judge me. After all you only see what i choose to show you")
    waitloop()
def madara():
	dialouges.say("Wake up to reality... nothing ever goes as planned in this accursed world... the longer you live the more you realize the only thing that truly exist in this reality is nearly pain, suffering and futility.")
	img=Image.open('madara.jpg').show()
	waitloop()
def orochimaru():
	dialouges.say("Its the human nature not to realize the true value of something unless they lose it")
	waitloop()
def obito():
	dialouges.say('In shinobi world those who break rules are scum... but those who aboundant their friends are worst than scum')
	waitloop()
def jiraiya():
	dialouges.say('A place where someone still thinks about you is a place you can call home')
	waitloop()
def kakashi():
	dialouges.say("In society those who don't have many abilities, tend to complain more.")
	waitloop()
def pain():
	dialouges.say('Pain is the only way to teach, pain. It is the only solution to peace. if you want to know pain, you need to understand pain.')
	waitloop()
def nagato():
	dialouges.say('Those who do not understand true pain, can never understand true peace')
	waitloop()
def guy():
	dialouges.say('Hardwork is the path to succedd')
	waitloop()
def lee():
	dialouges.say('I am a Taijutsu user')
	waitloop()
def waitloop():
	dialouges.runAndWait()


naruto=tk.Button(root,text='Naruto Uzumaki',command=naruto,pady=10,fg='blue').grid(row=3,column=1)
sasuke=tk.Button(root,text='Sasuke Uchiha',command=sasuke,pady=10,fg='blue').grid(row=4,column=1)
itachi=tk.Button(root,text='Itachi Uchiha',command=itachi,pady=10,fg='blue').grid(row=5,column=1)
madara=tk.Button(root,text='Madara Uchiha',command=madara,pady=10,fg='blue').grid(row=6,column=1)
orochimaru=tk.Button(root,text='Orochimaru',command=orochimaru,pady=10,fg='blue').grid(row=7,column=1)
obito=tk.Button(root,text='Obito Uchiha',command=obito,pady=10,fg='blue').grid(row=8,column=1)
jiraiya=tk.Button(root,text='Pervy Sage',command=jiraiya,pady=10,fg='blue').grid(row=3, column=3)
kakashi=tk.Button(root,text='Kakashi Hatake',command=kakashi,pady=10,fg='blue').grid(row=4, column=3)
pain=tk.Button(root,text='Pain',command=pain,pady=10,fg='blue').grid(row=5, column=3)
nagato=tk.Button(root,text='Nagato Uzumaki',command=nagato,pady=10,fg='blue').grid(row=6, column=3)
guy=tk.Button(root,text='Might Guy',command=guy,pady=10,fg='blue').grid(row=7, column=3)
lee=tk.Button(root,text='Rock Lee',command=lee,pady=10,fg='blue').grid(row=8,column=3)
root.mainloop()
