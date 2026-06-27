import customtkinter as ctK
import subprocess
import json
import threading


class App(ctK.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Coffee Data App')
        self.geometry('1280x720')

        self.data = {}

        self.welcome_page = Welcome(master=self, app=self)
        self.name_page = Name(master=self, app=self)
        self.questions_page1 = Questions1(master=self, app=self)
        self.questions_page2 = Questions2(master=self, app=self)
        self.questions_page3 = Questions3(master=self, app =self)

        self.welcome_page.pack(expand=True)

    def show_name_page(self):
        self.welcome_page.pack_forget()
        self.name_page.pack(expand=True)

    def show_questions_page1(self):
        self.name_page.pack_forget()
        self.questions_page1.pack(expand = True)

    def show_questions_page2(self):
        self.questions_page1.pack_forget()
        self.questions_page2.pack(expand = True)

    def show_questions_page3(self):
        self.questions_page2.pack_forget()
        self.questions_page3.pack(expand = True)

    def save_to_json(self):
        with open('player_data.json', 'w') as file:
            json.dump(self.data, file)
        print('saved:', self.data)

    def handle_name(self):
        name = self.name_page.name_entry.get().strip()

        if not name:
            self.name_page.error.label.configure(text = 'Please Enter Your Name')
            return
        
        self.name_page.error_label.configure(text = '')
        self.data['name'] = name
        self.show_questions_page()
        
    def handle_questions(self):
        choice = self.questions_page.choice_var.get()

        if not choice:
            self.choice_page.error.label.configure(text = 'Please pick a choice')
            return
        
    def run_hub(self):
        subprocess.Popen(['python', 'hub.py'])

class Welcome(ctK.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.app = app

        self.welcome_label = ctK.CTkLabel(
            self,
            text='Welcome To MaceAce Human Simulations Exam',
            font=ctK.CTkFont(size=24, weight="bold")
        )
        self.welcome_label.pack(pady=50)

        self.button = ctK.CTkButton(
            self,
            text='Next',
            width=200,
            font=ctK.CTkFont(size=14),
            command=self.button_event
        )
        self.button.pack(pady=10)

    def button_event(self):
        self.app.show_name_page()

        

class Name(ctK.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.app = app

        self.name_label = ctK.CTkLabel(
            self,
            text='Enter Your Name',
            font=ctK.CTkFont(size=18, weight="bold")
        )
        self.name_label.pack(pady=(40, 5))

        self.name_entry = ctK.CTkEntry(
            self,
            placeholder_text='e.g Tommy Vercetti',
            width=300,
            font=ctK.CTkFont(size=14)
        )
        self.name_entry.pack(pady=5)

        self.button = ctK.CTkButton(
            self,
            text='Next',
            width=200,
            font=ctK.CTkFont(size=14),
            command=self.button_event
        )
        self.button.pack(pady=10)

        self.error_label = ctK.CTkLabel (self, text = '', text_color = 'red', font = ctK.CTkFont (size = 13))
        self.error_label.pack()

    def button_event(self):
        name = self.name_entry.get().strip()

        if not name:
            self.error_label.configure(text = 'Please Input Name')
        else:
            self.error_label.configure(text = '')
            self.app.data['name'] = name
            self.app.show_questions_page1()

# Question 1 Of The Application

class Questions1(ctK.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.app = app

        self.questions_label = ctK.CTkLabel(
            self,
            text='Question 1: How Cofident Are You Taking This Challenge?',
            font=ctK.CTkFont(size=18, weight="bold")
        )
        self.questions_label.pack(pady=50)

        self.answer_q1 = ctK.StringVar (value='')
        ctK.CTkRadioButton(self, text = 'Yes', variable = self.answer_q1, value = 'Yes').pack(pady = 2)
        ctK.CTkRadioButton(self, text = 'No', variable=self.answer_q1, value = 'No').pack(pady=2)

        self.next_button = ctK.CTkButton(self, text = 'Next', width = 200, command = self.next)
        self.next_button.pack(pady = 10)
        self.error_label = ctK.CTkLabel(self, text ='', text_color= 'red', font = ctK.CTkFont(size = 13))
        self.error_label.pack()

    def next(self):
        if not self.answer_q1.get():
            self.error_label.configure(text ='Please An Choose Answer')
        else:
            self.error_label.configure(text = '')
            self.app.data['q1'] = self.answer_q1.get()
            self.app.show_questions_page2()

# Question 2 Of The Application

class Questions2(ctK.CTkFrame):
    def __init__(self,master,app, **kwargs):
        super().__init__(master, fg_color='transparent', **kwargs)
        self.app = app

        self.questions2_label = ctK.CTkLabel(
            self,
            text = "Question 2: Is the presenter of this game crazy? ",
            font = ctK.CTkFont(size = 18, weight = 'bold')
        )
        self.questions2_label.pack(pady = 50)

        self.answer_q2 = ctK.StringVar (value = '')
        ctK.CTkRadioButton(self, text = 'Yes', variable = self.answer_q2, value = 'Yes').pack(pady = 2)
        ctK.CTkRadioButton(self, text = 'No', variable = self.answer_q2, value = 'No').pack(pady = 2)

        self.next_button = ctK.CTkButton(self, text = 'Next', width = 200, command = self.next)
        self.next_button.pack(pady = 10)
        self.error_label = ctK.CTkLabel(self, text = '', text_color = 'red', font = ctK.CTkFont(size = 13))
        self.error_label.pack()

    def next(self):
        if not self.answer_q2.get():
            self.error_label.configure(text = 'Please Choose An Answer')
            return
        self.error_label.configure(text = '')
        self.app.data['q2'] = self.answer_q2.get()
        self.app.show_questions_page3()

# Question 3 of The Application 

class Questions3(ctK.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, fg_color='transparent', **kwargs)
        self.app = app

        self.questions3_label = ctK.CTkLabel(
            self,
            text='Question 3: What is one drink that you will be consuming today to aid you!',
            font=ctK.CTkFont(size=18, weight='bold')
        )
        self.questions3_label.pack(pady=50)

        self.answer_q3 = ctK.CTkEntry(self, placeholder_text='Please Input Your Answer Here', width=200)
        self.answer_q3.pack(pady=5)

        self.submit_button = ctK.CTkButton(
            self,
            text='Start Session',
            width=200,
            font=ctK.CTkFont(size=14),
            command=self.submit
        )
        self.submit_button.pack(pady=30)

        self.error_label = ctK.CTkLabel(self, text='', text_color='red', font=ctK.CTkFont(size=13))
        self.error_label.pack()
    
  
    def submit(self):
        if not self.answer_q3.get():
            self.error_label.configure(text='Please type in the answer.')
            return
        self.error_label.configure(text='')
        self.app.data['q3'] = self.answer_q3.get()
        self.app.save_to_json()
        self.app.withdraw()
        process = subprocess.Popen([r'C:\Users\Mason\Desktop\projects\I Tested If Coffee Actually Makes You Better At Games\CoffeLab.exe'])
        threading.Thread(target=self.wait_for_game, args=(process,), daemon=True).start()

    def wait_for_game(self, process):
        process.wait()
        self.app.deiconify()
        self.app.run_hub()

if __name__ == "__main__":
    app = App()
    app.mainloop()