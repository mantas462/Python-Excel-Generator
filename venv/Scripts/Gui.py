import ExcelEditor
from tkinter import *
from tkinter import messagebox, font

class ProgramInterface(Frame):
    def __init__(self):
        Frame.__init__(self)
        frame = Frame()
        self.master.title('Excel creator Romexoj')
        self.master.geometry("400x500")
        self.master.configure(bg="#FE2E2E")
        self.master.wm_attributes("-topmost", 1)
        frame.grid()
        font11 = font.Font(family="Yu Gothic", size=11, weight='bold')
        frame.configure(bg="#FE2E2E")

        # Name in Empty line
        self.labEmpty = Label(frame, text="", bg="#FE2E2E", font=font11)
        self.labEmpty.grid(row=0, column=0, columnspan=2, sticky=W)

        # Country Names in interface

        # Name in UK
        self.labUK = Label(frame, text="English title:", bg="#FE2E2E", font=font11)
        self.labUK.grid(row=1,column =1 ,columnspan=2, sticky=W)
        self.UK_title = Entry(frame, width=20, bg="white")
        self.UK_title.grid(row=1, column=3, columnspan=5, sticky=W)

        # Name in DE
        self.labDE = Label(frame, text="German title:", bg="#FE2E2E", font=font11)
        self.labDE.grid(row=2, column=1, columnspan=2, sticky=W)
        self.DE_title = Entry(frame, width=20, bg="white")
        self.DE_title.grid(row=2, column=3, columnspan=5, sticky=W)

        # Name in FR
        self.labFR = Label(frame, text="Franch title:", bg="#FE2E2E", font=font11)
        self.labFR.grid(row=3, column=1, columnspan=2, sticky=W)
        self.FR_title = Entry(frame, width=20, bg="white")
        self.FR_title.grid(row=3, column=3, columnspan=5, sticky=W)

        # Name in IT
        self.labIT = Label(frame, text="Italian title:", bg="#FE2E2E", font=font11)
        self.labIT.grid(row=4, column=1, columnspan=2, sticky=W)
        self.IT_title = Entry(frame, width=20, bg="white")
        self.IT_title.grid(row=4, column=3, columnspan=5, sticky=W)

        # Name in ES
        self.labES = Label(frame, text="Spanish title:", bg="#FE2E2E", font=font11)
        self.labES.grid(row=5, column=1, columnspan=2, sticky=W)
        self.ES_title = Entry(frame, width=20, bg="white")
        self.ES_title.grid(row=5, column=3, columnspan=5, sticky=W)

        # Name in Empty line
        self.labEmpty = Label(frame, text="", bg="#FE2E2E", font=font11)
        self.labEmpty.grid(row=6, column=0, columnspan=2, sticky=W)

        # TShirt Modes

        # MBV checkbutton
        self.MBV = IntVar()
        self.MBV.set(1)
        self.MBVbut = Checkbutton(frame, bg="#FE2E2E", text="MBV    ", variable=self.MBV, font=font11, onvalue=1,
                                  offvalue=0)
        self.MBVbut.grid(row=7, column=1, sticky=W)

        # MBM checkbutton
        self.MBM = IntVar()
        self.MBM.set(1)
        self.MBMbut = Checkbutton(frame, bg="#FE2E2E", text="MBM    ", variable=self.MBM, font=font11, onvalue=1,
                                  offvalue=0)
        self.MBMbut.grid(row=8, column=1, sticky=W)

        # MPV checkbutton
        self.MPV = IntVar()
        self.MPV.set(1)
        self.MPVbut = Checkbutton(frame, bg="#FE2E2E", text="MPV    ", variable=self.MPV, font=font11, onvalue=1,
                                  offvalue=0)
        self.MPVbut.grid(row=9, column=1, sticky=W)

        # MPM checkbutton
        self.MPM = IntVar()
        self.MPM.set(1)
        self.MPMbut = Checkbutton(frame, bg="#FE2E2E", text="MPM    ", variable=self.MPM, font=font11, onvalue=1,
                                  offvalue=0)
        self.MPMbut.grid(row=10, column=1, sticky=W)

        # MBK checkbutton
        self.MBK = IntVar()
        self.MBK.set(1)
        self.MBKbut = Checkbutton(frame, bg="#FE2E2E", text="MBK    ", variable=self.MBK, font=font11, onvalue=1,
                                  offvalue=0)
        self.MBKbut.grid(row=11, column=1, sticky=W)

        # MPK checkbutton
        self.MPK = IntVar()
        self.MPK.set(1)
        self.MPKbut = Checkbutton(frame, bg="#FE2E2E", text="MPK    ", variable=self.MPK, font=font11, onvalue=1,
                                  offvalue=0)
        self.MPKbut.grid(row=12, column=1, sticky=W)

        # MPV checkbutton
        self.SW = IntVar()
        self.SW.set(1)
        self.SWbut = Checkbutton(frame, bg="#FE2E2E", text="SW    ", variable=self.SW, font=font11, onvalue=1,
                                  offvalue=0)
        self.SWbut.grid(row=13, column=1, sticky=W)

        # MPM checkbutton
        self.HO = IntVar()
        self.HO.set(1)
        self.HObut = Checkbutton(frame, bg="#FE2E2E", text="HO    ", variable=self.HO, font=font11, onvalue=1,
                                  offvalue=0)
        self.HObut.grid(row=14, column=1, sticky=W)

        # Name in Empty line
        self.labEmpty = Label(frame, text="", bg="#FE2E2E", font=font11)
        self.labEmpty.grid(row=15, column=0, columnspan=2, sticky=W)

        # Tshirt URLs

        # MBV URL
        self.labMBV_URL = Label(frame, text="MBV URL:", bg="#FE2E2E", font=font11)
        self.labMBV_URL.grid(row=7, column=3, columnspan=2, sticky=W)
        self.MBV_URL = Entry(frame, width=25, bg="white")
        self.MBV_URL.grid(row=7, column=5, columnspan=10, sticky=E)

        # MBM URL
        self.labMBM_URL = Label(frame, text="MBM URL:", bg="#FE2E2E", font=font11)
        self.labMBM_URL.grid(row=8, column=3, columnspan=2, sticky=W)
        self.MBM_URL = Entry(frame, width=25, bg="white")
        self.MBM_URL.grid(row=8, column=5, columnspan=10, sticky=E)

        # MPV URL
        self.labMPV_URL = Label(frame, text="MPV URL:", bg="#FE2E2E", font=font11)
        self.labMPV_URL.grid(row=9, column=3, columnspan=2, sticky=W)
        self.MPV_URL = Entry(frame, width=25, bg="white")
        self.MPV_URL.grid(row=9, column=5, columnspan=10, sticky=E)

        # MPM URL
        self.labMPM_URL = Label(frame, text="MPM URL:", bg="#FE2E2E", font=font11)
        self.labMPM_URL.grid(row=10, column=3, columnspan=2, sticky=W)
        self.MPM_URL = Entry(frame, width=25, bg="white")
        self.MPM_URL.grid(row=10, column=5, columnspan=10, sticky=E)

        # MBK URL
        self.labMBK_URL = Label(frame, text="MBK URL:", bg="#FE2E2E", font=font11)
        self.labMBK_URL.grid(row=11, column=3, columnspan=2, sticky=W)
        self.MBK_URL = Entry(frame, width=25, bg="white")
        self.MBK_URL.grid(row=11, column=5, columnspan=10, sticky=E)

        # MPK URL
        self.labMPK_URL = Label(frame, text="MPK URL:", bg="#FE2E2E", font=font11)
        self.labMPK_URL.grid(row=12, column=3, columnspan=2, sticky=W)
        self.MPK_URL = Entry(frame, width=25, bg="white")
        self.MPK_URL.grid(row=12, column=5, columnspan=10, sticky=E)

        # SW URL
        self.labSW_URL = Label(frame, text="SW URL:", bg="#FE2E2E", font=font11)
        self.labSW_URL.grid(row=13, column=3, columnspan=2, sticky=W)
        self.SW_URL = Entry(frame, width=25, bg="white")
        self.SW_URL.grid(row=13, column=5, columnspan=10, sticky=E)

        # HO URL
        self.labHO_URL = Label(frame, text="HO URL:", bg="#FE2E2E", font=font11)
        self.labHO_URL.grid(row=14, column=3, columnspan=2, sticky=W)
        self.HO_URL = Entry(frame, width=25, bg="white")
        self.HO_URL.grid(row=14, column=5, columnspan=10, sticky=E)

        # ------------------------------------------------------------------

        # Name in Design number
        self.labnumber = Label(frame, text="Design number: ", bg="#FE2E2E", font=font11)
        self.labnumber.grid(row=17, column=0, columnspan=2, sticky=E)
        self.Design_number = Entry(frame, width=8, bg="white")
        self.Design_number.grid(row=17, column=1, columnspan=3, sticky=E)

        #  Buttons

        # Add button
        def clickAdd(event):
            error = 0
            MBV_URL = " "
            MBM_URL = " "
            MPV_URL = " "
            MPM_URL = " "
            MBK_URL = " "
            MPK_URL = " "
            SW_URL = " "
            HO_URL = " "
            try:
                UK = open("UK.csv","r")
                DE = open("DE.csv","r")
                FR = open("FR.csv", "r")
                IT = open("IT.csv", "r")
                ES = open("ES.csv", "r")
            except:
                messagebox.showwarning("Warning", "One or more destination file is missing, please first click Create")
                error =1
            if int(self.MBV.get()) == 1:
                MBV_URL = self.MBV_URL.get().replace('\n', '').replace('\r', '')
                if MBV_URL == "https://www.dropbox.com/s/tgol170kwehvcb5/MEN%20GUIDE.png?dl=0":
                    messagebox.showwarning("Warning", "The MBV URL is the same as secondary url.")
                    error = 1

            if int(self.MBM.get()) == 1:
                MBM_URL = self.MBM_URL.get().replace('\n', '').replace('\r', '')
                if MBM_URL == "https://www.dropbox.com/s/imtxhums5morg9y/WOMEN%20GUIDE.png?dl=0":
                    messagebox.showwarning("Warning", "The MBM URL is the same as secondary url.")
                    error = 1
                if MBV_URL == MBM_URL:
                    messagebox.showwarning("Warning", "The MBV URL is the same as MBM url.")
                    error = 1

            if int(self.MPV.get()) == 1:
                MPV_URL = self.MPV_URL.get().replace('\n', '').replace('\r', '')
                if MPV_URL == "https://www.dropbox.com/s/tgol170kwehvcb5/MEN%20GUIDE.png?dl=0":
                    messagebox.showwarning("Warning", "The MPV URL is the same as secondary url.")
                    error = 1
                if MBM_URL == MPV_URL:
                    messagebox.showwarning("Warning", "The MBM URL is the same as MPV url.")
                    error = 1

            if int(self.MPM.get()) == 1:
                MPM_URL = self.MPM_URL.get().replace('\n', '').replace('\r', '')
                if MPM_URL == "https://www.dropbox.com/s/imtxhums5morg9y/WOMEN%20GUIDE.png?dl=0":
                    messagebox.showwarning("Warning", "The MPM URL is the same as secondary url.")
                    error = 1
                if MPV_URL == MPM_URL:
                    messagebox.showwarning("Warning", "The MPV URL is the same as MPM url.")
                    error = 1

            if int(self.MBK.get()) == 1:
                MBK_URL = self.MBK_URL.get().replace('\n', '').replace('\r', '')
                if MBK_URL == "https://www.dropbox.com/s/5b498p7xbgxexr8/KIDS%20GUIDE.png?dl=0":
                    messagebox.showwarning("Warning", "The MBK URL is the same as secondary url.")
                    error = 1
                if MPM_URL == MBK_URL:
                    messagebox.showwarning("Warning", "The MPM URL is the same as MBK url.")
                    error = 1

            if int(self.MPK.get()) == 1:
                MPK_URL = self.MPK_URL.get().replace('\n', '').replace('\r', '')
                if MPK_URL == "https://www.dropbox.com/s/5b498p7xbgxexr8/KIDS%20GUIDE.png?dl=0":
                    messagebox.showwarning("Warning", "The MPK URL is the same as secondary url.")
                    error = 1
                if MBK_URL == MPK_URL:
                    messagebox.showwarning("Warning", "The MBK URL is the same as MPK url.")
                    error = 1

            if int(self.SW.get()) == 1:
                SW_URL = self.SW_URL.get().replace('\n', '').replace('\r', '')
                if SW_URL == "https://www.dropbox.com/s/4q4y98fugszfvmr/SWEAAT.png?dl=0":
                    messagebox.showwarning("Warning", "The SW URL is the same as secondary url.")
                    error = 1
                if MPK_URL == SW_URL:
                    messagebox.showwarning("Warning", "The MPK URL is the same as SW url.")
                    error = 1

            if int(self.HO.get()) == 1:
                HO_URL = self.HO_URL.get().replace('\n', '').replace('\r', '')
                if HO_URL == "https://www.dropbox.com/s/yzuboo8g879zgog/HODIE.png?dl=0":
                    messagebox.showwarning("Warning", "The HO URL is the same as secondary url.")
                    error = 1
                if SW_URL == HO_URL:
                    messagebox.showwarning("Warning", "The SW URL is the same as HO url.")
                    error = 1

            UK_title = self.UK_title.get().replace('\n', '').replace('\r', '')
            DE_title = self.DE_title.get().replace('\n', '').replace('\r', '')
            FR_title = self.FR_title.get().replace('\n', '').replace('\r', '')
            ES_title = self.ES_title.get().replace('\n', '').replace('\r', '')
            IT_title = self.IT_title.get().replace('\n', '').replace('\r', '')

            if error != 1:
                if int(self.MBV.get()) == 1:
                    number = 0
                    ExcelEditor.Add(number, UK_title, DE_title, FR_title, ES_title, IT_title, MBV_URL, self.Design_number.get())
                if int(self.MBM.get()) == 1:
                    number =1
                    ExcelEditor.Add(number, UK_title, DE_title, FR_title, ES_title, IT_title, MBM_URL, self.Design_number.get())
                if int(self.MPV.get()) == 1:
                    number = 2
                    ExcelEditor.Add(number, UK_title, DE_title, FR_title, ES_title, IT_title, MPV_URL, self.Design_number.get())
                if int(self.MPM.get()) == 1:
                    number = 3
                    ExcelEditor.Add(number, UK_title, DE_title, FR_title, ES_title, IT_title, MPM_URL, self.Design_number.get())
                if int(self.MBK.get()) == 1:
                    number = 4
                    ExcelEditor.Add(number, UK_title, DE_title, FR_title, ES_title, IT_title, MBK_URL, self.Design_number.get())
                if int(self.MPK.get()) == 1:
                    number = 5
                    ExcelEditor.Add(number, UK_title, DE_title, FR_title, ES_title, IT_title, MPK_URL, self.Design_number.get())
                if int(self.SW.get()) == 1:
                    number = 6
                    ExcelEditor.Add(number, UK_title, DE_title, FR_title, ES_title, IT_title, SW_URL, self.Design_number.get())
                if int(self.HO.get()) == 1:
                    number = 7
                    ExcelEditor.Add(number, UK_title, DE_title, FR_title, ES_title, IT_title, HO_URL, self.Design_number.get())
                print("Done")
                ExcelEditor.EndLine()
                self.master.destroy()
                gui()
            return

        self.AddButton = Button(frame, text="Add ", font=font11)
        self.AddButton.bind("<Button-1>", clickAdd,)
        self.AddButton.grid(row=2, column=8, columnspan=4, sticky=S)

        # Create button
        def clickCreate(event):
            try:
                ExcelEditor.create()
            except:
                messagebox.showwarning("Warning", "Files already exists, please remove them to create a new ones. A security meassure so you wouldn't loose all the information which was in the files. :)")
            print("Done")
            return

        self.CreateButton = Button(frame, text="Create", font=font11)
        self.CreateButton.bind("<Button-1>", clickCreate, )
        self.CreateButton.grid(row=4, column=7, columnspan=5, sticky=E)

def gui():
    ProgramInterface().mainloop()

def main():
    gui()

main()