import tkinter as tk
import string


def check_password_strength():
    password = pass_entry.get()
    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digit = any([1 if c in string.digits else 0 for c in password])
    characters = [upper_case, lower_case, special, digit]

    length = len(password)

    score = 0
    with open('common.txt', 'r') as f:
        common = f.read().splitlines()

    for i in range(0, len(common)):
        if password == common[i]:
            scores.config(text='password is very common.Score: 0/7')

    if length > 8:
        score += 1

    if length > 12:
        score += 1

    if length > 17:
        score += 1

    if length > 20:
        score += 1

    if sum(characters) > 1:
        score += 1

    if sum(characters) > 2:
        score += 1

    if sum(characters) > 3:
        score += 1

    if score < 4:

        scores.config(text='pass is very weak! Score is {}/7'.format(score))
    elif score == 4:

        scores.config(text='The password is ok! Score is {}/7'.format(score))

    elif 4 < score < 6:

        scores.config(text="password is pretty good! score is: {}/7 ".format(score))
    elif score > 6:

        strong.config(text='password is strong! score is: {}/7'.format(score))


root = tk.Tk()
root.geometry('400x300')
root.title('Password Strength Checker')
password_label = tk.Label(root, text='enter password')
password_label.pack()
pass_entry = tk.Entry(root, show='*')
pass_entry.pack()
btn = tk.Button(root, text='Check Strength', command=check_password_strength)
btn.pack()
scores = tk.Label(root, text=' ', fg='black')
strong = tk.Label(root, text=' ', fg='green')
strong.pack()
scores.pack()
root.mainloop()
