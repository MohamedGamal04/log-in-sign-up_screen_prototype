from tkinter import *
from customtkinter import *
import time
from random import *
import re
import datetime
from validate_email_address import validate_email


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("EXTRA")
        self.color = "#e31448"
        self.config(background=self.color)

    def show_hide_pass():
        if on_off_pass.get() == "on":
            main_Login_m_pass_entry.configure(show="")
        elif on_off_pass.get() == "off":
            main_Login_m_pass_entry.configure(show="*")

    def year_foc_in(event):
        main_Sign_up_m_birth_date_year_entry.configure(textvariable=Year)

    def country_foc_in(event):
        main_Sign_up_m_country_entry.configure(textvariable=Country)

    def password_foc_in(event):
        main_Sign_up_m_password_entry.configure(textvariable=Sign_up_password)


def submit_Sign_in_C():
    # confirm_year():
    for i in range(int(time.asctime()[20:24]), 1940, -1):
        if Year.get() == str(i):
            age = int(time.asctime()[20:24]) - int(Year.get())
            comfirm_birth_date = 1
            if int(months.get(month.get())) > datetime.datetime.now().month:
                age -= 1
            elif int(months.get(month.get())) == datetime.datetime.now().month:
                if int(day.get()) > datetime.datetime.now().day:
                    age -= 1

    # gender_event():
    if gender_var.get() == "Male":
        sex = "Male"
        comfirm_sex = 1
    elif gender_var.get() == "Female":
        sex = "Female"
        comfirm_sex = 1
    # country_check():
    for i in countres.keys():
        if Country.get().upper() == i:
            country = countres.get(i)
            comfirm_country = 1

    # password_check():
    if (
        len(Sign_up_password.get()) >= 6
        and re.findall("[A-Z]", Sign_up_password.get())
        and re.findall("[a-z]", Sign_up_password.get())
        and re.findall("[0-9]", Sign_up_password.get())
        and re.findall("[_+=*&^%$#@!~/-]", Sign_up_password.get())
        and Sign_up_password.get().find(" ") == -1
        and Sign_up_password.get() == com_password.get()
    ):
        password = Sign_up_password.get()
        comfirm_password = 1

    # reCaptcha
    if recapthca_number == recapthca.get():
        comfirm_recapthca = 1
    else:
        pass
    # email
    if validate_email(Sign_up_m_email.get()):
        email = Sign_up_m_email.get()
        comfirm_email = 1
    else:
        pass
    # names
    if len(Sign_up_m_First_name.get()) > 1:
        first_name = Sign_up_m_First_name.get()
        comfirm_first_name = 1
    else:
        pass
    if len(Sign_up_m_Last_name.get()) > 1:
        last_name = Sign_up_m_Last_name.get()
        comfirm_last_name = 1
    else:
        pass
    if len(Sign_up_m_username.get()) > 1:
        username = Sign_up_m_username.get()
        comfirm_sign_up_username = 1
    else:
        pass
    # address
    address = Address.get()
    comfirm_address = 1
    # class
    if (
        comfirm_sign_up_username == 1
        and comfirm_first_name == 1
        and comfirm_last_name == 1
        and comfirm_email == 1
        and comfirm_country == 1
        and comfirm_birth_date == 1
        and comfirm_sex == 1
        and comfirm_address == 1
        and comfirm_country == 1
        and comfirm_password == 1
        and comfirm_recapthca == 1
    ):
        user.append(
            User(
                first_name,
                last_name,
                username,
                email,
                password,
                address,
                country,
                sex,
                age,
            )
        )


class User:
    num_of_users = 0

    def __init__(
        self,
        first_name,
        last_name,
        username,
        email,
        password,
        address,
        country,
        sex,
        age,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.address = address
        self.country = country
        self.sex = sex
        self.age = age
        User.num_of_users += 1

    def Display(self):
        print(
            self.first_name,
            self.last_name,
            self.username,
            self.address,
            self.password,
            self.email,
            self.country,
            self.sex,
            self.age,
            sep="\n",
        )


def submit_login():
    for i in range(User.num_of_users):
        if log_in_pass.get()==user[i].password and log_in_user==user[i].username:
            user[i].Display()


app = App()
# variables
user = []
Sign_up_m_First_name = StringVar()
log_in_pass= StringVar()
log_in_user= StringVar()
Sign_up_m_Last_name = StringVar()
Sign_up_m_username = StringVar()
Sign_up_m_email = StringVar()
day = StringVar()
on_off_pass = StringVar()
Country = StringVar()
com_password = StringVar()
Sign_up_password = StringVar()
comfirm_sign_up_username = 0
comfirm_first_name = 0
comfirm_last_name = 0
comfirm_email = 0
comfirm_country = 0
comfirm_birth_date = 0
comfirm_sex = 0
comfirm_address = 0
comfirm_country = 0
comfirm_password = 0
comfirm_recapthca = 0
recapthca = StringVar()
recapthca_number = str(randint(10000, 99999))
days = [str(i) for i in range(1, 31)]
months = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12",
}
month = StringVar()
Year = StringVar()
Address = StringVar()
gender_var = StringVar()
countres = {
    "AF": "Afghanistan",
    "AX": "Aland Islands",
    "AL": "Albania",
    "DZ": "Algeria",
    "AS": "American Samoa",
    "AD": "Andorra",
    "AO": "Angola",
    "AI": "Anguilla",
    "AQ": "Antarctica",
    "AG": "Antigua and Barbuda",
    "AR": "Argentina",
    "AM": "Armenia",
    "AW": "Aruba",
    "AU": "Australia",
    "AT": "Austria",
    "AZ": "Azerbaijan",
    "BS": "Bahamas",
    "BH": "Bahrain",
    "BD": "Bangladesh",
    "BB": "Barbados",
    "BY": "Belarus",
    "BE": "Belgium",
    "BZ": "Belize",
    "BJ": "Benin",
    "BM": "Bermuda",
    "BT": "Bhutan",
    "BO": "Bolivia, Plurinational State of",
    "BQ": "Bonaire, Sint Eustatius and Saba",
    "BA": "Bosnia and Herzegovina",
    "BW": "Botswana",
    "BV": "Bouvet Island",
    "BR": "Brazil",
    "IO": "British Indian Ocean Territory",
    "BN": "Brunei Darussalam",
    "BG": "Bulgaria",
    "BF": "Burkina Faso",
    "BI": "Burundi",
    "KH": "Cambodia",
    "CM": "Cameroon",
    "CA": "Canada",
    "CV": "Cape Verde",
    "KY": "Cayman Islands",
    "CF": "Central African Republic",
    "TD": "Chad",
    "CL": "Chile",
    "CN": "China",
    "CX": "Christmas Island",
    "CC": "Cocos (Keeling) Islands",
    "CO": "Colombia",
    "KM": "Comoros",
    "CG": "Congo",
    "CD": "Congo, The Democratic Republic of the",
    "CK": "Cook Islands",
    "CR": "Costa Rica",
    "CI": "Côte d'Ivoire",
    "HR": "Croatia",
    "CU": "Cuba",
    "CW": "Curaçao",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DK": "Denmark",
    "DJ": "Djibouti",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "EC": "Ecuador",
    "EG": "Egypt",
    "SV": "El Salvador",
    "GQ": "Equatorial Guinea",
    "ER": "Eritrea",
    "EE": "Estonia",
    "ET": "Ethiopia",
    "FK": "Falkland Islands (Malvinas)",
    "FO": "Faroe Islands",
    "FJ": "Fiji",
    "FI": "Finland",
    "FR": "France",
    "GF": "French Guiana",
    "PF": "French Polynesia",
    "TF": "French Southern Territories",
    "GA": "Gabon",
    "GM": "Gambia",
    "GE": "Georgia",
    "DE": "Germany",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GR": "Greece",
    "GL": "Greenland",
    "GD": "Grenada",
    "GP": "Guadeloupe",
    "GU": "Guam",
    "GT": "Guatemala",
    "GG": "Guernsey",
    "GN": "Guinea",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HT": "Haiti",
    "HM": "Heard Island and McDonald Islands",
    "VA": "Holy See (Vatican City State)",
    "HN": "Honduras",
    "HK": "Hong Kong",
    "HU": "Hungary",
    "IS": "Iceland",
    "IN": "India",
    "ID": "Indonesia",
    "IR": "Iran, Islamic Republic of",
    "IQ": "Iraq",
    "IE": "Ireland",
    "IM": "Isle of Man",
    "IL": "Israel",
    "IT": "Italy",
    "JM": "Jamaica",
    "JP": "Japan",
    "JE": "Jersey",
    "JO": "Jordan",
    "KZ": "Kazakhstan",
    "KE": "Kenya",
    "KI": "Kiribati",
    "KP": "Korea, Democratic People's Republic of",
    "KR": "Korea, Republic of",
    "KW": "Kuwait",
    "KG": "Kyrgyzstan",
    "LA": "Lao People's Democratic Republic",
    "LV": "Latvia",
    "LB": "Lebanon",
    "LS": "Lesotho",
    "LR": "Liberia",
    "LY": "Libya",
    "LI": "Liechtenstein",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "MO": "Macao",
    "MK": "Macedonia, Republic of",
    "MG": "Madagascar",
    "MW": "Malawi",
    "MY": "Malaysia",
    "MV": "Maldives",
    "ML": "Mali",
    "MT": "Malta",
    "MH": "Marshall Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MU": "Mauritius",
    "YT": "Mayotte",
    "MX": "Mexico",
    "FM": "Micronesia, Federated States of",
    "MD": "Moldova, Republic of",
    "MC": "Monaco",
    "MN": "Mongolia",
    "ME": "Montenegro",
    "MS": "Montserrat",
    "MA": "Morocco",
    "MZ": "Mozambique",
    "MM": "Myanmar",
    "NA": "Namibia",
    "NR": "Nauru",
    "NP": "Nepal",
    "NL": "Netherlands",
    "NC": "New Caledonia",
    "NZ": "New Zealand",
    "NI": "Nicaragua",
    "NE": "Niger",
    "NG": "Nigeria",
    "NU": "Niue",
    "NF": "Norfolk Island",
    "MP": "Northern Mariana Islands",
    "NO": "Norway",
    "OM": "Oman",
    "PK": "Pakistan",
    "PW": "Palau",
    "PS": "Palestinian Territory, Occupied",
    "PA": "Panama",
    "PG": "Papua New Guinea",
    "PY": "Paraguay",
    "PE": "Peru",
    "PH": "Philippines",
    "PN": "Pitcairn",
    "PL": "Poland",
    "PT": "Portugal",
    "PR": "Puerto Rico",
    "QA": "Qatar",
    "RE": "Réunion",
    "RO": "Romania",
    "RU": "Russian Federation",
    "RW": "Rwanda",
    "BL": "Saint Barthélemy",
    "SH": "Saint Helena, Ascension and Tristan da Cunha",
    "KN": "Saint Kitts and Nevis",
    "LC": "Saint Lucia",
    "MF": "Saint Martin (French part)",
    "PM": "Saint Pierre and Miquelon",
    "VC": "Saint Vincent and the Grenadines",
    "WS": "Samoa",
    "SM": "San Marino",
    "ST": "Sao Tome and Principe",
    "SA": "Saudi Arabia",
    "SN": "Senegal",
    "RS": "Serbia",
    "SC": "Seychelles",
    "SL": "Sierra Leone",
    "SG": "Singapore",
    "SX": "Sint Maarten (Dutch part)",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "SB": "Solomon Islands",
    "SO": "Somalia",
    "ZA": "South Africa",
    "GS": "South Georgia and the South Sandwich Islands",
    "ES": "Spain",
    "LK": "Sri Lanka",
    "SD": "Sudan",
    "SR": "Suriname",
    "SS": "South Sudan",
    "SJ": "Svalbard and Jan Mayen",
    "SZ": "Swaziland",
    "SE": "Sweden",
    "CH": "Switzerland",
    "SY": "Syrian Arab Republic",
    "TW": "Taiwan, Province of China",
    "TJ": "Tajikistan",
    "TZ": "Tanzania, United Republic of",
    "TH": "Thailand",
    "TL": "Timor-Leste",
    "TG": "Togo",
    "TK": "Tokelau",
    "TO": "Tonga",
    "TT": "Trinidad and Tobago",
    "TN": "Tunisia",
    "TR": "Turkey",
    "TM": "Turkmenistan",
    "TC": "Turks and Caicos Islands",
    "TV": "Tuvalu",
    "UG": "Uganda",
    "UA": "Ukraine",
    "AE": "United Arab Emirates",
    "GB": "United Kingdom",
    "US": "United States",
    "UM": "United States Minor Outlying Islands",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VU": "Vanuatu",
    "VE": "Venezuela, Bolivarian Republic of",
    "VN": "Viet Nam",
    "VG": "Virgin Islands, British",
    "VI": "Virgin Islands, U.S.",
    "WF": "Wallis and Futuna",
    "YE": "Yemen",
    "ZM": "Zambia",
    "ZW": "Zimbabwe",
}
# tabs
tabs = CTkTabview(
    master=app, bg_color=app.color, border_color=app.color, width=440, height=580
)
tabs.add("Login")
tabs.add("Sign up")
# frame
main_Login_m = CTkFrame(
    master=tabs.tab("Login"), bg_color=app.color, width=440, height=580, corner_radius=0
)
main_Sign_up_m = CTkFrame(
    master=tabs.tab("Sign up"),
    bg_color=app.color,
    width=440,
    height=580,
    corner_radius=0,
)
# labels
main_Login_m_username_label = CTkLabel(
    corner_radius=50,
    master=main_Login_m,
    text="Username: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Login_m_pass_label = CTkLabel(
    corner_radius=50,
    master=main_Login_m,
    text="Password: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_First_name_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="First name: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_last_name_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="Last name: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_username_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="Username: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_birth_date_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="birth date: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_email_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="Email: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_country_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="Country: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_address_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="Address: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_sex_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="Gender: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_password_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="Password: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_con_password_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="Confirm password: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_recaptcha_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="reCAPTCHA: ",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_D_M_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="/",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_M_Y_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text="/",
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="transparent",
)
main_Sign_up_m_recaptcha_number_label = CTkLabel(
    corner_radius=50,
    master=main_Sign_up_m,
    text=recapthca_number,
    bg_color="transparent",
    fg_color="transparent",
    text_color=app.color,
    font=("Arial", 30, "bold"),
)
# entries
main_Login_m_username_entry = CTkEntry(
    corner_radius=50,
    master=main_Login_m,
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="#565b5e",
    width=280,
    textvariable=log_in_user
)
main_Login_m_pass_entry = CTkEntry(
    corner_radius=50,
    master=main_Login_m,
    font=("Arial", 20, "bold"),
    bg_color="transparent",
    fg_color="#565b5e",
    show="*",
    width=280,
    textvariable=log_in_pass
)
main_Sign_up_m_First_name_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=290,
    border_width=0.6,
    textvariable=Sign_up_m_First_name,
)
main_Sign_up_m_Last_name_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=290,
    border_width=0.6,
    textvariable=Sign_up_m_Last_name,
)
main_Sign_up_m_username_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=290,
    border_width=0.6,
    textvariable=Sign_up_m_username,
)
main_Sign_up_m_email_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=340,
    border_width=0.6,
    textvariable=Sign_up_m_email,
)
main_Sign_up_m_birth_date_year_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=70,
    border_width=0.6,
    justify="center",
    placeholder_text="Y",
    placeholder_text_color="white",
)
main_Sign_up_m_birth_date_year_entry.bind("<FocusIn>", App.year_foc_in)
main_Sign_up_m_country_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=315,
    border_width=0.6,
    justify="center",
    placeholder_text="US,RU,etc...",
    placeholder_text_color="white",
)
main_Sign_up_m_country_entry.bind("<FocusIn>", App.country_foc_in)
main_Sign_up_m_Address_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=315,
    border_width=0.6,
    justify="center",
    textvariable=Address,
)
main_Sign_up_m_password_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=300,
    border_width=0.6,
    justify="center",
    placeholder_text="At least 6 character ABC/abc/$_!/123..",
    placeholder_text_color="white",
)
main_Sign_up_m_password_entry.bind("<FocusIn>", App.password_foc_in)
main_Sign_up_m_com_password_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=220,
    border_width=0.6,
    justify="center",
    textvariable=com_password,
    show="*",
)
main_Sign_up_m_recaptcha_entry = CTkEntry(
    corner_radius=70,
    master=main_Sign_up_m,
    bg_color="transparent",
    fg_color="#565b5e",
    width=170,
    border_width=0.6,
    justify="center",
    textvariable=recapthca,
)
# combo boxes
main_Sign_up_m_birth_date_day_box = CTkComboBox(
    master=main_Sign_up_m,
    justify="center",
    values=days,
    state="readonly",
    width=60,
    border_width=0.6,
    button_color="#e31448",
    variable=day,
)
main_Sign_up_m_birth_date_day_box.set("D")
main_Sign_up_m_birth_date_day_box._entry.configure(readonlybackground="#333333")
main_Sign_up_m_birth_date_month_box = CTkComboBox(
    master=main_Sign_up_m,
    justify="center",
    values=months.keys(),
    state="readonly",
    width=100,
    border_width=0.6,
    button_color="#e31448",
    variable=month,
)
main_Sign_up_m_birth_date_month_box.set("M")
main_Sign_up_m_birth_date_month_box._entry.configure(readonlybackground="#333333")

# buttons
main_Login_m_submit_btn = CTkButton(
    master=main_Login_m,
    width=140,
    height=80,
    text="Login",
    fg_color="#02db06",
    font=("Arial", 30, "bold"),
    hover_color="#067d08",
    text_color="white",
    corner_radius=50,
    command=submit_login,
)
main_Sign_up_m_submit_btn = CTkButton(
    master=main_Sign_up_m,
    width=140,
    height=80,
    text="Sign up",
    fg_color="#02db06",
    font=("Arial", 30, "bold"),
    hover_color="#067d08",
    text_color="white",
    corner_radius=50,
    command=submit_Sign_in_C,
)
# switches
main_Login_m_pass_show = CTkSwitch(
    master=main_Login_m,
    text="show password",
    variable=on_off_pass,
    onvalue="on",
    font=("Arial", 20, "bold"),
    offvalue="off",
    command=App.show_hide_pass,
)
# Radio buttons
male = CTkRadioButton(
    master=main_Sign_up_m,
    text="Male",
    variable=gender_var,
    value="Male",
    font=("Arial", 15, "bold"),
)
female = CTkRadioButton(
    master=main_Sign_up_m,
    text="Female",
    variable=gender_var,
    value="Female",
    font=("Arial", 15, "bold"),
)
# Place
tabs.pack_configure(pady=30, padx=50, anchor="center")
main_Login_m.pack_configure(anchor="center")
main_Sign_up_m.pack_configure(anchor="center")
main_Login_m_username_label.place(x=10, y=20)
main_Login_m_username_entry.place(x=140, y=20)
main_Login_m_pass_label.place(x=10, y=80)
main_Login_m_pass_entry.place(x=140, y=80)
main_Login_m_pass_show.place(x=230, y=140 - 6)
main_Login_m_submit_btn.place(x=138, y=340)
main_Sign_up_m_First_name_label.place(x=10, y=20)
main_Sign_up_m_last_name_label.place(x=10, y=55)
main_Sign_up_m_username_label.place(x=10, y=90)
main_Sign_up_m_email_label.place(x=10, y=110 + 15)
main_Sign_up_m_birth_date_label.place(x=10, y=160)
main_Sign_up_m_country_label.place(x=10, y=170 + 25)
main_Sign_up_m_address_label.place(x=10, y=200 + 28)
main_Sign_up_m_sex_label.place(x=10, y=230 + 32)
main_Sign_up_m_password_label.place(x=10, y=260 + 34)
main_Sign_up_m_con_password_label.place(x=10, y=290 + 38)
main_Sign_up_m_recaptcha_label.place(x=10, y=350 + 32)
main_Sign_up_m_First_name_entry.place(x=140, y=20)
main_Sign_up_m_Last_name_entry.place(x=140, y=55)
main_Sign_up_m_username_entry.place(x=140, y=90)
main_Sign_up_m_email_entry.place(x=90, y=110 + 15)
main_Sign_up_m_birth_date_day_box.place(x=360, y=160)
main_Sign_up_m_D_M_label.place(x=195, y=160)
main_Sign_up_m_birth_date_month_box.place(x=225, y=160)
main_Sign_up_m_M_Y_label.place(x=325, y=160)
main_Sign_up_m_birth_date_year_entry.place(x=130, y=160)
main_Sign_up_m_country_entry.place(x=115, y=195)
main_Sign_up_m_Address_entry.place(x=115, y=230)
male.place(x=115, y=265)
female.place(x=190, y=265)
main_Sign_up_m_password_entry.place(x=130, y=294)
main_Sign_up_m_com_password_entry.place(x=210, y=330)
main_Sign_up_m_recaptcha_number_label.place(x=150, y=376)
main_Sign_up_m_recaptcha_entry.place(x=260, y=379)
main_Sign_up_m_submit_btn.place(x=125, y=450)
# main
if __name__ == "__main__":
    app.mainloop()