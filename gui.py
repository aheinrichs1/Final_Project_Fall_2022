"""
Program: gui.py
Author: Alex Heinrichs
Date Modified: 12/13/2022

Contains gui for hangman game
"""
from tkinter import *
from hangman import Hangman


def start_game():
    """Starts game of hangman"""
    clear_canvas()
    newGame.start_game()
    answer = ''
    for letters in newGame.answer:
        answer += '_ '
    hidden_answer.config(text=answer)
    message.config(text='Guess a letter!')
    a.config(state='active')
    b.config(state='active')
    c.config(state='active')
    d.config(state='active')
    e.config(state='active')
    f.config(state='active')
    g.config(state='active')
    h.config(state='active')
    i.config(state='active')
    j.config(state='active')
    k.config(state='active')
    l.config(state='active')
    m.config(state='active')
    n.config(state='active')
    o.config(state='active')
    p.config(state='active')
    q.config(state='active')
    r.config(state='active')
    s.config(state='active')
    t.config(state='active')
    u.config(state='active')
    v.config(state='active')
    w.config(state='active')
    x.config(state='active')
    y.config(state='active')
    z.config(state='active')
    start.config(state='disabled')


def guess_letter(guess):
    """Guesses a letter"""
    ans = newGame.guess_letter(guess)
    # if answer is correct
    if ans == 'correct':
        message.config(text='Correct!')
    # if answer is incorrect
    elif ans == 'incorrect':
        message.config(text='Incorrect!')
    # if answer has been chosen already
    elif ans == 'chosen':
        message.config(text="You've already chosen this letter!")
    answer = ''
    placeholder = ''
    for letter in newGame.answer:
        # resets placeholder for next letter
        placeholder = '_ '
        for guessed in newGame.guessed_letters:
            if guessed == letter:
                placeholder = guessed + ' '
        answer += placeholder
    hidden_answer.config(text=answer)
    draw_hangman()
    check_game_status(newGame.determine_game())


def check_game_status(condition):
    if condition == 'win':
        message.config(text='Congrats, you win!\nPress start game to play again')
        end_game()
    elif condition == 'lose':
        message.config(text=f'HUNG! Game Over\nPress start game to play again')
        answer = ''
        for letter in newGame.answer:
            answer += letter + ' '
        hidden_answer.config(text=answer)
        print(newGame.answer)
        end_game()


def draw_hangman():
    if newGame.misses_remaining == 5:
        # head
        canvas.create_oval(130, 60, 150, 80)
    elif newGame.misses_remaining == 4:
        # torso
        canvas.create_line(140, 80, 140, 150)
    elif newGame.misses_remaining == 3:
        # right arm
        canvas.create_line(140, 100, 115, 90)
    elif newGame.misses_remaining == 2:
        # left arm
        canvas.create_line(140, 100, 165, 90)
    elif newGame.misses_remaining == 1:
        # right leg
        canvas.create_line(140, 150, 125, 180)
    elif newGame.misses_remaining == 0:
        # left leg
        canvas.create_line(140, 150, 155, 180)


def end_game():
    a.config(state='disabled')
    b.config(state='disabled')
    c.config(state='disabled')
    d.config(state='disabled')
    e.config(state='disabled')
    f.config(state='disabled')
    g.config(state='disabled')
    h.config(state='disabled')
    i.config(state='disabled')
    j.config(state='disabled')
    k.config(state='disabled')
    l.config(state='disabled')
    m.config(state='disabled')
    n.config(state='disabled')
    o.config(state='disabled')
    p.config(state='disabled')
    q.config(state='disabled')
    r.config(state='disabled')
    s.config(state='disabled')
    t.config(state='disabled')
    u.config(state='disabled')
    v.config(state='disabled')
    w.config(state='disabled')
    x.config(state='disabled')
    y.config(state='disabled')
    z.config(state='disabled')
    start.config(state='active')


def clear_canvas():
    canvas.delete('all')
    # hangman's post
    canvas.create_line(70, 270, 70, 20)
    canvas.create_line(70, 20, 140, 20)
    canvas.create_line(140, 20, 140, 60)
    canvas.create_line(30, 270, 160, 270)


if __name__ == '__main__':
    main = Tk()
    main.title('Hangman')
    rootFrame = Frame(main, width=280, height=280, bg="white")
    rootFrame.grid(row=0, columnspan=7)
    canvas = Canvas(main, width=280, height=280, bg="white")
    canvas.grid(row=0, columnspan=7)
    # hangman's post
    canvas.create_line(70, 270, 70, 20)
    canvas.create_line(70, 20, 140, 20)
    canvas.create_line(140, 20, 140, 60)
    canvas.create_line(30, 270, 160, 270)
    newGame = Hangman()
    newGame.start_game()
    hidden_answer = Label(main, justify='center', font=30)
    hidden_answer.grid(row=1, columnspan=7)
    message = Label(main, justify='center', text='Press start game to start')
    message.grid(row=2, columnspan=7)
    a = Button(main, text='A', state='disabled', command=lambda: guess_letter('a'))
    a.grid(row=3, column=0, padx=3, pady=3, sticky=NSEW)
    b = Button(main, text='B', state='disabled', command=lambda: guess_letter('b'))
    b.grid(row=3, column=1, padx=3, pady=3, sticky=NSEW)
    c = Button(main, text='C', state='disabled', command=lambda: guess_letter('c'))
    c.grid(row=3, column=2, padx=3, pady=3, sticky=NSEW)
    d = Button(main, text='D', state='disabled', command=lambda: guess_letter('d'))
    d.grid(row=3, column=3, padx=3, pady=3, sticky=NSEW)
    e = Button(main, text='E', state='disabled', command=lambda: guess_letter('e'))
    e.grid(row=3, column=4, padx=3, pady=3, sticky=NSEW)
    f = Button(main, text='F', state='disabled', command=lambda: guess_letter('f'))
    f.grid(row=3, column=5, padx=3, pady=3, sticky=NSEW)
    g = Button(main, text='G', state='disabled', command=lambda: guess_letter('g'))
    g.grid(row=3, column=6, padx=3, pady=3, sticky=NSEW)
    h = Button(main, text='H', state='disabled', command=lambda: guess_letter('h'))
    h.grid(row=4, column=0, padx=3, pady=3, sticky=NSEW)
    i = Button(main, text='I', state='disabled', command=lambda: guess_letter('i'))
    i.grid(row=4, column=1, padx=3, pady=3, sticky=NSEW)
    j = Button(main, text='J', state='disabled', command=lambda: guess_letter('j'))
    j.grid(row=4, column=2, padx=3, pady=3, sticky=NSEW)
    k = Button(main, text='K', state='disabled', command=lambda: guess_letter('k'))
    k.grid(row=4, column=3, padx=3, pady=3, sticky=NSEW)
    l = Button(main, text='L', state='disabled', command=lambda: guess_letter('l'))
    l.grid(row=4, column=4, padx=3, pady=3, sticky=NSEW)
    m = Button(main, text='M', state='disabled', command=lambda: guess_letter('m'))
    m.grid(row=4, column=5, padx=3, pady=3, sticky=NSEW)
    n = Button(main, text='N', state='disabled', command=lambda: guess_letter('n'))
    n.grid(row=4, column=6, padx=3, pady=3, sticky=NSEW)
    o = Button(main, text='O', state='disabled', command=lambda: guess_letter('o'))
    o.grid(row=5, column=0, padx=3, pady=3, sticky=NSEW)
    p = Button(main, text='P', state='disabled', command=lambda: guess_letter('p'))
    p.grid(row=5, column=1, padx=3, pady=3, sticky=NSEW)
    q = Button(main, text='Q', state='disabled', command=lambda: guess_letter('q'))
    q.grid(row=5, column=2, padx=3, pady=3, sticky=NSEW)
    r = Button(main, text='R', state='disabled', command=lambda: guess_letter('r'))
    r.grid(row=5, column=3, padx=3, pady=3, sticky=NSEW)
    s = Button(main, text='S', state='disabled', command=lambda: guess_letter('s'))
    s.grid(row=5, column=4, padx=3, pady=3, sticky=NSEW)
    t = Button(main, text='T', state='disabled', command=lambda: guess_letter('t'))
    t.grid(row=5, column=5, padx=3, pady=3, sticky=NSEW)
    u = Button(main, text='U', state='disabled', command=lambda: guess_letter('u'))
    u.grid(row=5, column=6, padx=3, pady=3, sticky=NSEW)
    v = Button(main, text='V', state='disabled', command=lambda: guess_letter('v'))
    v.grid(row=6, column=1, padx=3, pady=3, sticky=NSEW)
    w = Button(main, text='W', state='disabled', command=lambda: guess_letter('w'))
    w.grid(row=6, column=2, padx=3, pady=3, sticky=NSEW)
    x = Button(main, text='X', state='disabled', command=lambda: guess_letter('x'))
    x.grid(row=6, column=3, padx=3, pady=3, sticky=NSEW)
    y = Button(main, text='Y', state='disabled', command=lambda: guess_letter('y'))
    y.grid(row=6, column=4, padx=3, pady=3, sticky=NSEW)
    z = Button(main, text='Z', state='disabled', command=lambda: guess_letter('z'))
    z.grid(row=6, column=5, padx=3, pady=3, sticky=NSEW)
    start = Button(main, text='Start Game', command=start_game)
    start.grid(row=7, column=0, columnspan=2, padx=3, pady=3, sticky=NSEW)
    Button(main, text='Exit Game', command=main.destroy).grid(row=7, column=5, columnspan=2, padx=3, pady=3, sticky=NSEW)

    col_count, row_count = main.grid_size()

    for col in range(col_count):
        main.grid_columnconfigure(col, minsize=40)

    for row in range(row_count):
        main.grid_rowconfigure(row, minsize=40)
    main.mainloop()
