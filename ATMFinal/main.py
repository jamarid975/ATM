from gui import *



def main():
    window = Tk()
    window.title("ATM")
    window.geometry('240x250')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()