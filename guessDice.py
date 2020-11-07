from tkinter import *
from random import randint
from PIL import ImageTk, Image


# Available Functions
def reset_dice():
    reset_btn.destroy()
    img_label.config(image=dice_img)
    roll_btn.config(state='normal')
    label3.config(text='')


def guess_result(ans):
    global reset_btn
    reset_btn = Button(frame, image=reset_image, font=10, command=reset_dice,
                       borderwidth=0, cursor='hand2')
    reset_btn.grid(row=4, column=0, sticky='n')
    roll_btn.config(state='disabled')
    randNum = randint(1, 6)
    imageNum = dice_dic[randNum]
    img_label.config(image=imageNum)
    guess = "You guessed it correctly!" if int(ans) == randNum else "Incorrect guess!"
    label3['text'] = f"Rolled Number: {randNum}" + '\n' + guess


# Set dice numbers
dice_options = [i for i in range(1, 7)]

# Creating main window
root = Tk()
root.title("Guess the Dice")
root.iconbitmap('Dice-Icon.ico')

app_width = 800
app_height = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

# Creating 2 background colors
bg1 = '#e6ffee'
bg2 = '#0099ff'

# Importing images
roll_image = ImageTk.PhotoImage(Image.open('RollButton.png'))
reset_image = ImageTk.PhotoImage(Image.open('Reset-button.jpg'))
dice_img = ImageTk.PhotoImage(Image.open('dice.png'))
dice_1 = ImageTk.PhotoImage(Image.open('dice-1.jpg'))
dice_2 = ImageTk.PhotoImage(Image.open('dice-2.jpg'))
dice_3 = ImageTk.PhotoImage(Image.open('dice-3.jpg'))
dice_4 = ImageTk.PhotoImage(Image.open('dice-4.jpg'))
dice_5 = ImageTk.PhotoImage(Image.open('dice-5.jpg'))
dice_6 = ImageTk.PhotoImage(Image.open('dice-6.jpg'))
dice_dic = {
    1: dice_1,
    2: dice_2,
    3: dice_3,
    4: dice_4,
    5: dice_5,
    6: dice_6
}

main_title = Label(root, text='Dice Game', bg=bg1, font=('Helvetica', 30, 'bold'))
main_title.grid(row=0, column=0, sticky='nsew')

frame = Frame(root, bg=bg2)
frame.grid(row=1, column=0, sticky='nsew')
frame.rowconfigure([i for i in range(5)], weight=1)
frame.columnconfigure(0, weight=1)

label1 = Label(frame, text="Make a guess on the rolled dice number", bg=bg2,
               font=('Helvetica', 16, 'bold', 'underline', 'italic'))
label1.grid(row=0, column=0, sticky='n', pady=5)

variable = StringVar(root)
variable.set(dice_options[0])
opt = OptionMenu(frame, variable, *dice_options)
opt.config(bg=bg2, font=('Arial', 12, 'bold'), fg='white', cursor='pencil')
opt.grid(row=1, column=0, sticky='n', pady=5)

img_label = Label(frame, image=dice_img)
img_label.grid(row=2, column=0, sticky='n', pady=5)

roll_btn = Button(frame, image=roll_image, font=10, command=lambda: guess_result(variable.get()),
                  borderwidth=0, cursor='hand2')
roll_btn.grid(row=4, column=0, sticky='n', pady=5)

label3 = Label(frame, font=('Times', 15, 'bold'), bg=bg2)
label3.grid(row=5, column=0, sticky='n', pady=5)

quitButton = Button(root, text="Exit Program", font=('Times', 20), cursor='hand2', command=root.quit)
quitButton.grid(row=2, column=0, sticky='nsew')

root.rowconfigure([i for i in range(3)], weight=1)
root.columnconfigure(0, weight=1)
root.resizable(False, False)

root.mainloop()
