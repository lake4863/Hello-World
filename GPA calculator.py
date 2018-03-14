# This program is Chane's first program which
#  planned to be used by CAPS 128 classmate two days later.
#  So this is a brief version to solve the problem.
 
import tkinter
import tkinter.messagebox

class MyGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		self.radio_var = tkinter.IntVar()
		
		self.radio_var.set(1)
		self.rb1 = tkinter.Radiobutton(self.top_frame, \
			text='A: 4.0', variable=self.radio_var, value=1)
		self.rb2 = tkinter.Radiobutton(self.top_frame, \
			text='B: 3.0', variable=self.radio_var, value=2)
		self.rb3 = tkinter.Radiobutton(self.top_frame, \
			text='C: 2.0', variable=self.radio_var, value=3)
		self.rb4 = tkinter.Radiobutton(self.top_frame, \
			text='D: 1.0', variable=self.radio_var, value=4)		
		self.rb5 = tkinter.Radiobutton(self.top_frame, \
			text='F: 0.0', variable=self.radio_var, value=5)

		self.rb1.pack()
		self.rb2.pack()
		self.rb3.pack()
		self.rb4.pack()
		self.rb5.pack()

		self.ok_button = tkinter.Button(self.bottom_frame, \
			text='OK', command=self.show_choice)
		self.quit_button = tkinter.Button(self.bottom_frame, \
			text='Quit', command=self.main_window.destroy)

		self.ok_button.pack(side='left')
		self.quit_button.pack(side='left')

		self.top_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()


	def show_choice(self):
		tkinter.messagebox.showinfo('Selection', 'You selected option '+\
			str(self.radio_var.get()))


my_gui = MyGUI()
