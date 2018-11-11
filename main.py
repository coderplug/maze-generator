import tkinter as tk
import input_frame as inf
import output_frame as outf

def main():
    root = tk.Tk()

    left = tk.Frame(root, borderwidth=2, relief="solid")
    right = tk.Frame(root, borderwidth=2, relief="solid")

    left.pack(side="left", expand=True, fill="both")
    right.pack(side="right", expand=True, fill="both")

    pic = outf.OutputFrame(master=right)

    app = inf.InputFrame(master=left, picture=pic)

    root.title("Maze Generator")
    root.update()
    root.resizable(False, False)

    root.mainloop()

main()