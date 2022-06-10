import pyfirmata
from time import sleep
import tkinter


board=pyfirmata.Arduino('COM3')
pin11=board.get_pin('d:11:p')
pin10=board.get_pin('d:10:p')
pin9=board.get_pin('d:9:p')

class mainGui():
    def __init__(self):
        pass

    def shine(self,redValue,greenValue,blueValue):
        pin11.write(redValue)
        pin10.write(greenValue)
        pin9.write(blueValue)

    def defineMainUi(self):
        mainUI=tkinter.Tk()
        mainUI.geometry("800x500")
        mainUI.configure(bg="black")

        self.main=mainUI

    def lastlyMainLoop(self):
        self.main.mainloop()
        

    def createWidgets(self):
        #defining widgets
        main_info0=tkinter.Label(self.main,fg="white",bg="black",text="Slide these sliders and configure your values."
        ,font="ubuntu",height=1)


        def updateRedChannel(self):
            pin11.write(main_redSlider.get()/100)

        main_redSlider=tkinter.Scale(self.main,fg="white",bg="black"
        ,label="A slider for Red color channel",from_=0,to=100,command=updateRedChannel
        ,orient="horizontal",length=120)

        def updateGreenChannel(self):
            pin10.write(main_greenSlider.get()/100)

        main_greenSlider=tkinter.Scale(self.main,fg="white",bg="black"
        ,label="A slider for Green color channel",from_=0,to=100,command=updateGreenChannel
        ,orient="horizontal",length=120)

        def updateBlueChannel(self):
            pin9.write(main_blueSlider.get()/100)

        main_blueSlider=tkinter.Scale(self.main,fg="white",bg="black"
        ,label="A slider for Blue color channel",from_=0,to=100,command=updateBlueChannel
        ,orient="horizontal",length=120)


        #positioning widgets

        main_info0.grid(row=0,column=1)

        main_redSlider.grid(row=1,column=0,ipadx=100)
        main_greenSlider.grid(row=2,column=0,ipadx=100)
        main_blueSlider.grid(row=3,column=0,ipadx=100)


mainUI=mainGui()
mainUI.defineMainUi()
mainUI.createWidgets()
mainUI.lastlyMainLoop()

