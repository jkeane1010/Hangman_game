from PIL import Image,ImageTk

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