import tkinter
from customtkinter import *
from data import *
import ToDataBase
class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x800")
        self.title("CTk example")
        self.color = "#e31448"
        self.config(background=self.color)
        self.minsize(440, 580)


app = App()


class Tabs():
    tabs = CTkTabview(app, bg_color=app.color, width=440,
                      height=580, corner_radius=10)
    tabs.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
    tabs.add("Login")
    tabs.add("Sign-up")


class LoginFrame(CTkFrame):
    logInPass = StringVar()
    logInUser = StringVar()
    show_pass = StringVar()

    def __init__(self, container):
        super().__init__(container, width=440, height=580)
# --------------labels
        self.username = CTkLabel(
            master=self,
            text="Username: ",
            font=Setting.label_font,
            bg_color=Setting.fg_color,
            fg_color=Setting.fg_color,
        )
        self.password = CTkLabel(
            master=self,
            text="Password: ",
            font=Setting.label_font,
            bg_color=Setting.fg_color,
            fg_color=Setting.fg_color,
        )
        self.username.place(x=20, y=40)
        self.password.place(x=20, y=100)
# ----------------entry
        self.username_entry = CTkEntry(
            corner_radius=Setting.corner_radius,
            master=self,
            font=Setting.entry_font,
            bg_color="transparent",
            fg_color="#565b5e",
            width=300,
            textvariable=LoginFrame.logInUser
        )
        self.password_entry = CTkEntry(
            corner_radius=Setting.corner_radius,
            master=self,
            font=Setting.entry_font,
            bg_color="transparent",
            fg_color="#565b5e",
            show="*",
            width=300,
            textvariable=LoginFrame.logInPass
        )
        self.username_entry.place(x=120, y=40)
        self.password_entry.place(x=120, y=100)
# ----------------Button
        self.button = CTkButton(
            master=self,
            width=160,
            height=80,
            text="Login",
            fg_color="#02db06",
            font=("Arial", 30, "bold"),
            hover_color="#067d08",
            text_color="white",
            corner_radius=Setting.corner_radius,
            command=self.submit_login,
        )
        self.button.place(x=135, y=350)
# ---------------switch
        self.pass_show = CTkSwitch(
            master=self,
            text="show password",
            variable=self.show_pass,
            onvalue="on",
            font=Setting.label_font,
            offvalue="off",
            command=self.show_hide_pass,
        )
        self.pass_show.place(x=230, y=140)
        # show the frame on the container
        self.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)

    def submit_login(self):
        pass

    def show_hide_pass(self):
        if self.show_pass.get() == "on":
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")


class Sign_upFrame(CTkFrame):
    confirm_username = 0
    confirm_first_name = 0
    confirm_last_name = 0
    confirm_email = 0
    confirm_country = 0
    confirm_birth_date = 0
    confirm_sex = 0
    confirm_address = 0
    confirm_password = 0
    confirm_recapthca = 0
    First_name = StringVar()
    Address = StringVar()
    recapthca = StringVar()
    County = StringVar()
    Last_name = StringVar()
    Year = StringVar()
    County = StringVar()
    con_password = StringVar()
    username = StringVar()
    email = StringVar()
    day = StringVar()
    month = StringVar()
    year = StringVar()
    gender_var = StringVar()
    Country = StringVar()
    password = StringVar()

    def __init__(self, container):
        super().__init__(container, width=440, height=580)
        self.labels()

    def labels(self):
        self.First_name = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="First name: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.last_name = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="Last name: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.username = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="Username: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.birth_date = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="birth date: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.email = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="Email: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.country = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="Country: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.address = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="Address: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.sex = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="Gender: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.password = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="Password: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.con_password = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="Confirm password: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.recaptcha = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="reCAPTCHA: ",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.D_M = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="/",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.M_Y = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text="/",
            font=Setting.label_font,
            bg_color="transparent",
            fg_color="transparent",
        )
        self.recaptcha_number = CTkLabel(
            corner_radius=Setting.corner_radius,
            master=self,
            text=recapthca_number,
            bg_color="transparent",
            fg_color="transparent",
            text_color=app.color,
            font=("Arial", 30, "bold"),
        )
#------------------------------entry
        self.First_name_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=290,
            border_width=0.6,
            textvariable=Sign_upFrame.First_name,
        )
        self.Last_name_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=290,
            border_width=0.6,
            textvariable=Sign_upFrame.Last_name,
        )
        self.username_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=290,
            border_width=0.6,
            textvariable=Sign_upFrame.username,
        )
        self.email_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=340,
            border_width=0.6,
            textvariable=Sign_upFrame.email,
        )
        self.year_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=70,
            border_width=0.6,
            justify="center",
            placeholder_text="Y",
            placeholder_text_color="white",
            
        )
        self.year_entry.bind("<FocusIn>", self.year_foc_in)
        self.country_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=315,
            border_width=0.6,
            justify="center",
            placeholder_text="US,RU,etc...",
            placeholder_text_color="white",
        )
        self.country_entry.bind("<FocusIn>", self.country_foc_in)
        self.Address_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=315,
            border_width=0.6,
            justify="center",
            textvariable=Sign_upFrame.Address,
        )
        self.password_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=300,
            border_width=0.6,
            justify="center",
            placeholder_text="At least 6 character ABC/abc/$_!/123..",
            placeholder_text_color="white",
        )
        self.password_entry.bind("<FocusIn>", self.password_foc_in)
        self.con_password_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=220,
            border_width=0.6,
            justify="center",
            textvariable=Sign_upFrame.con_password,
            show="*",
        )
        self.recaptcha_entry = CTkEntry(
            corner_radius=70,
            master=self,
            bg_color="transparent",
            fg_color="#565b5e",
            width=170,
            border_width=0.6,
            justify="center",
            textvariable=Sign_upFrame.recapthca,
        )
        self.day_box = CTkComboBox(
            master=self,
            justify="center",
            values=Days,
            state="readonly",
            width=60,
            border_width=0.6,
            button_color="#e31448",
            variable=Sign_upFrame.day,
        )
        self.day_box.set("D")
        self.day_box._entry.configure(readonlybackground="#333333")
        self.month_box = CTkComboBox(
            master=self,
            justify="center",
            values=Months.keys(),
            state="readonly",
            width=100,
            border_width=0.6,
            button_color="#e31448",
            variable=Sign_upFrame.month,

        )
        self.month_box.set("M")
        self.month_box._entry.configure(readonlybackground="#333333")
        self.male = CTkRadioButton(
            master=self,
            text="Male",
            variable=Sign_upFrame.gender_var,
            value="Male",
            font=Setting.entry_font,
        )
        self.female = CTkRadioButton(
            master=self,
            text="Female",
            variable=Sign_upFrame.gender_var,
            value="Female",
            font=Setting.entry_font,
        )
        self.btn = CTkButton(
            master=self,
            width=140,
            height=80,
            text="Sign up",
            fg_color="#02db06",
            font=("Arial", 30, "bold"),
            hover_color="#067d08",
            text_color="white",
            corner_radius=Setting.corner_radius,
            command=self.submit_Sign_in_C,
        )
        self.First_name.place(x=10, y=40)
        self.last_name.place(x=10, y=75)
        self.username.place(x=10, y=110)
        self.email.place(x=10, y=145)
        self.birth_date.place(x=10, y=180)
        self.country.place(x=10, y=215)
        self.address.place(x=10, y=248)
        self.sex.place(x=10, y=282)
        self.password.place(x=10, y=314)
        self.con_password.place(x=10, y=348)
        self.recaptcha.place(x=10, y=402)
        self.D_M.place(x=195, y=180)
        self.M_Y.place(x=325, y=180)
        self.recaptcha_number.place(x=140, y=400)
        self.First_name_entry.place(x=130, y=40)
        self.Last_name_entry.place(x=130, y=75)
        self.username_entry.place(x=130, y=110)
        self.email_entry.place(x=80, y=145)
        self.year_entry.place(x=120, y=180)
        self.country_entry.place(x=105, y=215)
        self.Address_entry.place(x=105, y=250)
        self.password_entry.place(x=120, y=314)
        self.con_password_entry.place(x=200, y=350)
        self.recaptcha_entry.place(x=250, y=399)
        self.day_box.place(x=360, y=180)
        self.month_box.place(x=225, y=180)
        self.male.place(x=125, y=285)
        self.female.place(x=300, y=285)
        self.btn.place(x=125, y=450)
        self.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)

    def year_foc_in(self, event):
        self.year_entry.configure(textvariable=Sign_upFrame.Year)

    def country_foc_in(self, event):
        self.country_entry.configure(textvariable=Sign_upFrame.Country)

    def password_foc_in(self, event):
        self.password_entry.configure(textvariable=Sign_upFrame.password)

    def submit_Sign_in_C(self):
        for i in range(int(time.asctime()[20:24]), 1940, -1):
            if Sign_upFrame.Year.get() == str(i):
                age = int(time.asctime()[20:24]) - int(Sign_upFrame.Year.get())
                Sign_upFrame.confirm_birth_date = 1
                if int(Months.get(Sign_upFrame.month.get())) > datetime.datetime.now().month:
                    age -= 1
                elif int(Months.get(Sign_upFrame.month.get())) == datetime.datetime.now().month:
                    if int(Sign_upFrame.day.get()) > datetime.datetime.now().day:
                        age -= 1
            else:tkinter.messagebox.Message()
        if Sign_upFrame.gender_var.get() == "Male":
            sex = "M"
            Sign_upFrame.confirm_sex = 1
        elif Sign_upFrame.gender_var.get() == "Female":
            sex = "F"
            Sign_upFrame.confirm_sex = 1
        for i in Countries.keys():
            if Sign_upFrame.Country.get().upper() == i:
                country = Countries.get(i)
                confirm_country = 1
            else:tkinter.messagebox.Message()
        if (
            len(Sign_upFrame.con_password.get()) >= 6
            and re.findall("[A-Z]", Sign_upFrame.password.get())
            and re.findall("[a-z]", Sign_upFrame.password.get())
            and re.findall("[0-9]", Sign_upFrame.password.get())
            and re.findall("[_+=*&^%$#@!~/-]", Sign_upFrame.password.get())
            and Sign_upFrame.password.get().find(" ") == -1
            and Sign_upFrame.password.get() == Sign_upFrame.con_password.get()
        ):
            password = Sign_upFrame.password.get()
            Sign_upFrame.confirm_password = 1
        else:tkinter.messagebox.Message()
        # reCaptcha
        if recapthca_number == Sign_upFrame.recapthca.get():
            Sign_upFrame.confirm_recapthca = 1
        else:
            tkinter.messagebox.Message()
        # email
        if validate_email(Sign_upFrame.email.get()):
            email = Sign_upFrame.email.get()
            Sign_upFrame.confirm_email = 1
        else:
            tkinter.messagebox.Message()
        # names
        if len(Sign_upFrame.First_name.get()) > 1:
            first_name = Sign_upFrame.First_name.get()
            Sign_upFrame.confirm_first_name = 1
        else:
            pass
        if len(Sign_upFrame.Last_name.get()) > 1:
            last_name = Sign_upFrame.Last_name.get()
            Sign_upFrame.confirm_last_name = 1
        else:
            pass
        if len(Sign_upFrame.username.get()) > 1:
            username = Sign_upFrame.username.get()
            Sign_upFrame.confirm_username = 1
        else:
            pass
        address = Sign_upFrame.Address.get()
        Sign_upFrame.confirm_address = 1
        if (
            Sign_upFrame.confirm_username == 1
            and Sign_upFrame.confirm_first_name == 1
            and Sign_upFrame.confirm_last_name == 1
            and Sign_upFrame.confirm_email == 1
            and Sign_upFrame.confirm_country == 1
            and Sign_upFrame.confirm_birth_date == 1
            and Sign_upFrame.confirm_sex == 1
            and Sign_upFrame.confirm_address == 1
            and Sign_upFrame.confirm_country == 1
            and Sign_upFrame.confirm_password == 1
            and Sign_upFrame.confirm_recapthca == 1
        ):
            ToDataBase.Main(first_name ,last_name,username,sex,email,password,country,address,age)



def Main():
    LoginFrame(Tabs.tabs.tab("Login"))
    Sign_upFrame(Tabs.tabs.tab("Sign-up"))
    
    app.mainloop()


if __name__ == "__main__":
    Main()
