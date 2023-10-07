from tkinter import *
import math


def calculatorMain():
    mainWindow = Tk()
    mainWindow.config(bg="#0c0c0c")
    mainWindow.title("Calculator",)
    mainWindow.resizable(False, False)
    mainWindow.geometry("330x500")

    global calcText
    calcText = ""
    global calcLabel
    calcLabel = StringVar()
    calcScreen = Label(mainWindow,
                       textvariable=calcLabel,
                       font=("Consolas", 40),
                       bg="#0c0c0c",
                       fg="white",
                       pady=20,
                       wraplength=300,
                       justify=RIGHT,

                       )
    calcScreen.place(x=15, y=40, width=300, height=80)
    calcLabel.set("0")

    def button_press(num):
        global calcText
        if calcText == "0":
            calcText = str(num)
        else:
            calcText = calcText+str(num)
        calcLabel.set(calcText)
        if len(calcText) >= 0 and len(calcText) <= 10:
            calcScreen.config(font=("Consolas", 40))
        elif len(calcText) > 10 and len(calcText) <= 20:
            calcScreen.config(font=("Consolas", 30))
        elif len(calcText) > 20 and len(calcText) <= 40:
            calcScreen.config(font=("Consolas", 20))
        elif len(calcText) > 40 and len(calcText) < 210:
            calcScreen.config(font=("Consolas", 10))
        else:
            calcText = calcText[:-1]
            return

    def equals():
        global calcText
        try:
            if calcText == "":
                calcText = "0"
                
            calculatedText = str(eval(calcText))
            calcText = calculatedText
            calcLabel.set(calcText)
            if len(calcText) >= 0 and len(calcText) <= 10:
                calcScreen.config(font=("Consolas", 40))
            elif len(calcText) > 10 and len(calcText) <= 20:
                calcScreen.config(font=("Consolas", 30))
            elif len(calcText) > 20 and len(calcText) <= 40:
                calcScreen.config(font=("Consolas", 20))
            elif len(calcText) > 40 and len(calcText) < 210:
                calcScreen.config(font=("Consolas", 10))
            else:
                calcText = calcText[:-1]
                return

        except ZeroDivisionError:
            calcLabel.set("Math Error!")
            calcText = ""
            calcScreen.config(font=("Consolas", 20, "bold"), fg="red")

        except SyntaxError:
            calcLabel.set("Syntax Error!")
            calcText = ""
            calcScreen.config(font=("Consolas", 20, "bold"), fg="red")



    def initialButtonPressBack():
        global calcText
        calcScreen.config(fg="white")
        calcText = calcText[:-1]

        if not calcText:
            calcText = "0"

        calcLabel.set(calcText)

        if len(calcText) >= 0 and len(calcText) <= 10:
            calcScreen.config(font=("Consolas", 40))
        elif len(calcText) > 10 and len(calcText) <= 20:
            calcScreen.config(font=("Consolas", 30))
        elif len(calcText) > 20 and len(calcText) <= 40:
            calcScreen.config(font=("Consolas", 20))
        elif len(calcText) > 40 and len(calcText) < 210:
            calcScreen.config(font=("Consolas", 10))
        else:
            calcText = calcText[:-1]
            return

    def initialButtonPressClear():
        global calcText
        calcText = ""
        calcLabel.set("0")
        calcScreen.config(font=("Consolas", 40), fg="white")

    def rootCalc():
        global calcText
        if calcText == "":
            calcText = "0"
        try:
            calcText = str(math.sqrt(float(calcText)))
            calcLabel.set(calcText)
            if len(calcText) >= 0 and len(calcText) <= 10:
                calcScreen.config(font=("Consolas", 40))
            elif len(calcText) > 10 and len(calcText) <= 20:
                calcScreen.config(font=("Consolas", 30))
            elif len(calcText) > 20 and len(calcText) <= 40:
                calcScreen.config(font=("Consolas", 20))
            elif len(calcText) > 40 and len(calcText) < 210:
                calcScreen.config(font=("Consolas", 10))
            else:
                calcText = calcText[:-1]
                return
        except ValueError:
            calcLabel.set("Math Error!")
            calcText = ""
            calcScreen.config(font=("Consolas", 20, "bold"), fg="red")
            
            
    buttonHolder = Frame(mainWindow,
                         bg="#0c0c0c",
                         )
    buttonHolder.pack(side=BOTTOM, pady=5)            
            


    buttonRoot = Button(buttonHolder,
                        text="√",
                        font=("Consolas", 18, "bold"),
                        width=5,
                        relief=SOLID,
                        command=rootCalc,
                        bg="#545454",
                        fg="#26a599",
                        # cursor="hand2"
                        )
    buttonRoot.grid(row=0, column=0, padx=2, pady=2)

    buttonMod = Button(buttonHolder,
                       text="%",
                       font=("Consolas", 18, "bold"),
                       width=5,
                       relief=SOLID,
                       command=lambda: button_press("%"),
                       bg="#545454",
                       fg="#26a599",
                      #  cursor="hand2"
                       )
    buttonMod.grid(row=0, column=1, padx=2, pady=2)

    buttonC = Button(buttonHolder,
                     text="C",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                     bg="#545454",
                     fg="#26a599",
                     command=initialButtonPressClear,
                    #  cursor="hand2"
                     )
    buttonC.grid(row=0, column=2, padx=2, pady=2)

    buttonDiv = Button(buttonHolder,
                       text="÷",
                       font=("Consolas", 18, "bold"),
                       width=5,
                       relief=SOLID,
                       command=lambda: button_press("/"),
                       bg="#26a599",
                       fg="white",
                      #  cursor="hand2"
                       )
    buttonDiv.grid(row=0, column=3, padx=2, pady=2)

    button7 = Button(buttonHolder,
                     text="7",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(7),
                    #  cursor="hand2"
                     )

    button7.grid(row=1, column=0, padx=2, pady=2)

    button8 = Button(buttonHolder,
                     text="8",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(8),
                    #  cursor="hand2"
                     )
    button8.grid(row=1, column=1, padx=2, pady=2)

    button9 = Button(buttonHolder,
                     text="9",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(9),
                    #  cursor="hand2"
                     )
    button9.grid(row=1, column=2, padx=2, pady=2)

    buttonMul = Button(buttonHolder,
                       text="×",
                       font=("Consolas", 18, "bold"),
                       width=5,
                       relief=SOLID,
                       command=lambda: button_press('*'),
                       bg="#26a599",
                       fg="white",
                      #  cursor="hand2"

                       )
    buttonMul.grid(row=1, column=3, padx=2, pady=2)

    button4 = Button(buttonHolder,
                     text="4",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(4),
                    #  cursor="hand2"
                     )
    button4.grid(row=2, column=0, padx=2, pady=2)

    button5 = Button(buttonHolder,
                     text="5",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(5),
                    #  cursor="hand2"

                     )
    button5.grid(row=2, column=1, padx=2, pady=2)

    button6 = Button(buttonHolder,
                     text="6",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,

                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(6),
                    #  cursor="hand2"
                     )
    button6.grid(row=2, column=2, padx=2, pady=2)

    buttonSub = Button(buttonHolder,
                       text="-",
                       font=("Consolas", 18, "bold"),
                       width=5,
                       relief=SOLID,
                       command=lambda: button_press("-"),
                       bg="#26a599",
                       fg="white",
                      #  cursor="hand2"
                       )
    buttonSub.grid(row=2, column=3, padx=2, pady=2)

    button1 = Button(buttonHolder,
                     text="1",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(1),
                    #  cursor="hand2"

                     )
    button1.grid(row=3, column=0, padx=2, pady=2)

    button2 = Button(buttonHolder,
                     text="2",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(2),
                    #  cursor="hand2"

                     )
    button2.grid(row=3, column=1, padx=2, pady=2)

    button3 = Button(buttonHolder,
                     text="3",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                    #  cursor="hand2",
                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(3)
                     )
    button3.grid(row=3, column=2, padx=2, pady=2)

    buttonAdd = Button(buttonHolder,
                       text="+",
                       font=("Consolas", 18, "bold"),
                       width=5,
                       relief=SOLID,
                       command=lambda: button_press("+"),
                       bg="#26a599",
                       fg="white",
                      #  cursor="hand2"
                       )
    buttonAdd.grid(row=3, column=3, padx=2, pady=2)

    button0 = Button(buttonHolder,
                     text="0",
                     font=("Consolas", 18, "bold"),
                     width=5,
                     relief=SOLID,
                     bg="#545454",
                     fg="white",
                     command=lambda: button_press(0),
                    #  cursor="hand2"
                     )
    button0.grid(row=4, column=0, padx=2, pady=2)

    buttonDecimal = Button(buttonHolder,
                           text=".",
                           font=("Consolas", 18, "bold"),
                           width=5,
                           relief=SOLID,
                           bg="#545454",
                           fg="white",
                           command=lambda: button_press("."),
                          #  cursor="hand2"
                           )
    buttonDecimal.grid(row=4, column=1, padx=2, pady=2)

    buttonBack = Button(buttonHolder,
                        text="⌫",
                        font=("Consolas", 18, "bold"),
                        width=5,
                        relief=SOLID,
                        bg="#545454",
                        fg="white",
                        command=initialButtonPressBack,
                        # cursor="hand2"
                        )
    buttonBack.grid(row=4, column=2, padx=2, pady=2)

    buttonEquals = Button(buttonHolder,
                          text="=",
                          font=("Consolas", 18, "bold"),
                          width=5,
                          relief=SOLID,
                          bg="#26a599",
                          fg="white",
                          command=equals,
                          # cursor="hand2"
                          )
    buttonEquals.grid(row=4, column=3, padx=2, pady=2)

    mainWindow.mainloop()

calculatorMain()