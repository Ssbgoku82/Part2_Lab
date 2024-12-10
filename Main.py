from gui import *

def main():
    window = Tk()
    window.title('Learning Python')
    window.geometry('600x400')
    window.resizable(True, True)

    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()




