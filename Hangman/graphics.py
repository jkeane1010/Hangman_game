from word_picker import word_length, word
from tkinter import *
from PIL import Image,ImageTk

global final
final = word

global z
z = 0

global guess
guess = 0
window = Tk()
window.title('Hangman')
window.geometry("600x600")

c = Canvas(window, bg="white", height=600, width=600)
c.place(x=0, y=0)

line1 = (Image.open(r"C:\Users\jadam\OneDrive\Desktop\python\Hangman\Pictures\line.GIF"))
resized_image = line1.resize((50,10), Image.ANTIALIAS)
line = ImageTk.PhotoImage(resized_image)

stage11 = (Image.open(r"C:\Users\jadam\OneDrive\Desktop\python\Hangman\Pictures\stage1.GIF"))
resized_image1 = stage11.resize((100,200), Image.ANTIALIAS)
stage1 = ImageTk.PhotoImage(resized_image1)

stage21 = (Image.open(r"C:\Users\jadam\OneDrive\Desktop\python\Hangman\Pictures\stage2.GIF"))
resized_image2 = stage21.resize((100,200), Image.ANTIALIAS)
stage2 = ImageTk.PhotoImage(resized_image2)

stage31 = (Image.open(r"C:\Users\jadam\OneDrive\Desktop\python\Hangman\Pictures\stage3.GIF"))
resized_image3 = stage31.resize((100,200), Image.ANTIALIAS)
stage3 = ImageTk.PhotoImage(resized_image3)

stage41 = (Image.open(r"C:\Users\jadam\OneDrive\Desktop\python\Hangman\Pictures\stage4.GIF"))
resized_image4 = stage41.resize((100,200), Image.ANTIALIAS)
stage4 = ImageTk.PhotoImage(resized_image4)

stage51 = (Image.open(r"C:\Users\jadam\OneDrive\Desktop\python\Hangman\Pictures\stage5.GIF"))
resized_image5 = stage51.resize((100,200), Image.ANTIALIAS)
stage5 = ImageTk.PhotoImage(resized_image5)

stage61 = (Image.open(r"C:\Users\jadam\OneDrive\Desktop\python\Hangman\Pictures\stage6.GIF"))
resized_image6 = stage61.resize((100,200), Image.ANTIALIAS)
stage6 = ImageTk.PhotoImage(resized_image6)

stage71 = (Image.open(r"C:\Users\jadam\OneDrive\Desktop\python\Hangman\Pictures\stage1.GIF"))
resized_image7 = stage71.resize((100,200), Image.ANTIALIAS)
stage7 = ImageTk.PhotoImage(resized_image7)

stage81 = (Image.open(r"C:\Users\jadam\OneDrive\Desktop\python\Hangman\Pictures\stage8.GIF"))
resized_image8 = stage81.resize((100,200), Image.ANTIALIAS)
stage8 = ImageTk.PhotoImage(resized_image8)


def confirmed_guess():
    global z
    letter = str(letter1.get())[0]
    print(letter, word)
    if letter in word:
        word1 = word
        y = 0
        while letter in word1:
            position = word1.find(letter)
            letter1.delete(0, END)
            new_guess()
            filler = Label(text = letter, bg = 'white',)
            filler.config(font = ('Helvatical bold',20))
            filler.place(x= (90+(50*(position+y))), y=460)
            if len(word1) > position:
                word1 = word1[0: position:] + word1[position + 1::]
                global final
            if len(final) > position:
                final = final[0: position:] + final[position + 1::]
            y += 1
            print(word_length, z)
            z += 1
        check_if_done()


    else:
        global guess
        guess += 1
        letter1.delete(0, END)
        new_guess()




welcome_label = Label(window, text = 'Hangman', bg = 'white')
welcome_label.config(font = ('Helvetica bold', 15))
welcome_label.place(x= 250, y = 20)

letter1 = Entry(window)
c.create_window(350, 540, window=letter1)

your_guess = Label(text = 'Your Guess:')
your_guess.config(font = ('Helvetica bold', 12), bg = 'white')
your_guess.place(x= 180, y = 527)

confirm = Button(text = 'Confirm Guess', command = confirmed_guess)
confirm.config(font = ('Helvetica bold', 12), bg = 'white')
confirm.place(x= 200, y = 557)


x = 0
while x < word_length:
    c.create_image((100+(x*50)), 500, image = line)
    x += 1

if guess == 0:
    c.create_image(250, 250, image=stage1)

def new_guess():
    if guess == 1:
        c.create_image(250, 250, image=stage2)
    elif guess == 2:
        c.create_image(250, 250, image=stage3)
    elif guess == 3:
        c.create_image(250, 250, image=stage4)
    elif guess == 4:
        c.create_image(250, 250, image=stage5)
    elif guess == 5:
        c.create_image(250, 250, image=stage6)
    elif guess == 6:
        c.create_image(250, 250, image=stage7)
    elif guess == 7:
        c.create_image(250, 250, image=stage8)

def check_if_done():
    if z == word_length:
        d = Canvas(window, bg="white", height=600, width=600)
        d.place(x=0, y=0)
        win_label = Label(text = 'Well Done you Win')
        win_label.config(fg = 'red', font=('Helvetica bold', 12))
        win_label.place(x=250, y=300)






















window.mainloop()

