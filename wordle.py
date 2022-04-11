import random, pygame, sys
from tkinter import *
from pygame.locals import *
from tkinter import *
import tkinter as tk
pygame.init()
white = (255,255,255)
yellow = (255,255,102)
grey = (211, 211, 211)
black = (0,0,0)
green=(0,255,0)
font1 = pygame.font.SysFont("bold", 40)
font2 = pygame.font.SysFont("Bold", 80)
youWin = font2.render("Hurray!",True, yellow)
youLose = font2.render("Try Again!",True, yellow)

def check(turns, word, Guess, window) :
    List = ["","","","",""]
    space = 0
    visited=[0,0,0,0,0]
    ColourCode = [grey,grey,grey,grey,grey]
    for x in range(0,5):
        for y in range(0,5):
            if Guess[x]==word[y] and visited[y]==0:
                ColourCode[x] = yellow
                visited[y]=1
        if word[x] == Guess[x]:
            ColourCode[x] = green
    Guess=list(Guess)
    for x in range(0,5):
        List[x] = font1.render(Guess[x], True, black)
        pygame.draw.rect(window, ColourCode[x], pygame.Rect(160+space, 50+ (turns*80), 50, 50))
        window.blit(List[x], (170+space , 60+(turns*80)) )
        space+=70
    if ColourCode == [green,green,green,green,green]:
        return True

def main():
    def dict(filename):
        file=open(filename)
        answers=file.readlines()
        file.close()
        return [answer[:5].upper() for answer in answers]
    words=dict("wordList.txt")
    word = words[random.randint(0, len(words)-1)].upper()
    height =700
    width = 700
    window = pygame.display.set_mode((width, height))
    window.fill(black)
    array=[]
    guess = ""
    Guess=font2.render(word,True,green)
    for x in range(0,5):
        for y in range(0,6):
            pygame.draw.rect(window, grey, pygame.Rect(160+(x*70), 50+(y*80), 50,50 ),5)
    pygame.display.set_caption("Wordle!")
    turns = 0
    win = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    guess = guess[:-1] 
                else:    
                    guess+=event.unicode.upper()
                    if len(guess) == 5:
                        if guess  in words and guess not in array:
                            win = check(turns, word, guess, window)
                            array.append(guess)
                            turns+=1
                            guess = ""
                        else:
                            guess=""
        window.fill(black,(0,500, 500, 200))
        Guess2=font2.render(guess,True,white)
        window.blit(Guess2,(240,550))
        if win == True:
            pygame.display.update()  
            app=Tk()
            app.configure(bg="white")
            app.title("RESULT")
            def new():
                app.destroy()
                main()
            label1 = Label(app, text=" WON ", font=14, bg="white", fg="black")
            label2 = Label(app, text="Word generated:", font=14, bg="black", fg="white")
            label1.pack()
            label2.pack()
            label1.grid(row=100, column=200, ipadx="10", ipady="10")
            label2.grid(row=103, column=200, ipadx="10", ipady="10")
            Result=Entry(app,font=14)
            Result.grid(row=103,column=201)
            Result.pack()
            button2 = Button(app,text="New Game",command=new) 
            button2.pack()
            word="            "+word
            Result.insert(0,word)
            app.mainloop()

        if turns == 6 and win != True:
            pygame.display.update()  
            app=Tk()
            app.configure(bg="white")
            app.title("RESULT")
            app.resizable(0,0)
            def new():
                app.destroy()
                main()
            label1 = Label(app, text="    ERROR ALWAYS CHASES YOU ", font=("bold",14), bg="white", fg="black")
            label2 = Label(app, text="Word generated:", font=14, bg="black", fg="White")
            label1.pack()
            label2.pack()
            Result=Entry(app,font=14,bg="black",fg="Green")
            Result.pack()
            button2 = Button(app,text="New Game",command=new) 
            button2.pack()
            word="            "+word
            Result.insert(0,word)
            app.mainloop()
        pygame.display.update()  
root=Tk()
root.title("How to play")
root.resizable(0,0)
bgimg=PhotoImage(file="picture.png")
labelPhoto=Label(root,image=bgimg)
labelPhoto.grid(row=0,column=0)
root.mainloop() 
main()