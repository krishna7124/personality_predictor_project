import os
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from functools import partial
from sklearn import datasets, linear_model


class train_model:
    def train(self):
        data = pd.read_csv('training_dataset.csv')
        array = data.values

        for i in range(len(array)):
            if array[i][0] == "Male":
                array[i][0] = 1
            else:
                array[i][0] = 0

        df = pd.DataFrame(array)

        maindf = df[[0, 1, 2, 3, 4, 5, 6]]
        mainarray = maindf.values

        temp = df[7]
        train_y = temp.values

        self.mul_lr = linear_model.LogisticRegression(
            multi_class='multinomial', solver='newton-cg', max_iter=1000)
        self.mul_lr.fit(mainarray, train_y)

    def test(self, test_data):
        try:
            test_predict = list()
            for i in test_data:
                test_predict.append(int(i))
            y_pred = self.mul_lr.predict([test_predict])
            return y_pred
        except:
            print("All Factors For Finding Personality Not Entered!")


def prediction_result(top, aplcnt_name, age, gender, personality_values, email, profession, company_name):
    # Remove the code related to ResumeParser and extracted data

    # Get values entered by the user from input fields
    candidate_name = aplcnt_name.get()
    age_value = age.get()
    gender_value = gender.get()
    email_value = email.get()
    profession_value = profession.get()
    company_name_value = company_name.get()

    # Use these values in the prediction process
    personality = model.test(personality_values)

    # Display the predicted personality and other information in the GUI
    print("\n############# Candidate Entered Data #############\n")
    applicant_data = {"Candidate Name": candidate_name, "Age": age_value,
                      "Gender": "Male" if gender_value == 1 else "Female"}
    print(applicant_data, personality_values)

    # You can use the candidate_name, age_value, gender_value, and personality variables here
    print("\n############# Predicted Personality #############\n")
    print(personality)

    result = Toplevel(top)
    result.geometry('700x550')
    result.configure(background='White')
    result.title("Predicted Personality")

    # Title
    titleFont = font.Font(family='Arial', size=30, weight='bold')
    Label(result, text="Result - Personality Prediction", foreground='green',
          bg='white', font=titleFont, pady=10, anchor=CENTER).pack(fill=BOTH)

    resultFont = font.Font(family='Arial', size=20)
    # Display candidate details
    Label(result, text=str('{}  {}'.format("Name:", candidate_name)
                           ).title(), foreground='black', font=resultFont, bg='white', anchor='w').pack(fill=BOTH)
    Label(result, text=str('{}  {}'.format("Age:", age_value)),
          foreground='black', font=resultFont, bg='white', anchor='w').pack(fill=BOTH)
    Label(result, text=str('{}  {}'.format("Gender:", "Male" if gender_value == 1 else "Female")),
          foreground='black', font=resultFont, bg='white', anchor='w').pack(fill=BOTH)
    Label(result, text=str('{}  {}'.format("Email:", email_value)),
          foreground='black', font=resultFont, bg='white', anchor='w').pack(fill=BOTH)
    Label(result, text=str('{}  {}'.format("Profession:", profession_value)),
          foreground='black', font=resultFont, bg='white', anchor='w').pack(fill=BOTH)
    Label(result, text=str('{}  {}'.format("Company Name:", company_name_value)),
          foreground='black', font=resultFont, bg='white', anchor='w').pack(fill=BOTH)

    # Add a label to display the predicted personality
    Label(result, text=str("Predicted Personality: " + personality).title(),
          foreground='black', font=resultFont, bg='white', anchor='w').pack(fill=BOTH)

    terms_mean = """
# Openness:
    People who like to learn new things and enjoy new experiences usually score high in openness. Openness includes traits like being insightful and imaginative and having a wide variety of interests.

# Conscientiousness:
    People that have a high degree of conscientiousness are reliable and prompt. Traits include being organised, methodic, and thorough.

# Extraversion:
    Extraversion traits include being; energetic, talkative, and assertive (sometime seen as outspoken by Introverts). Extraverts get their energy and drive from others, while introverts are self-driven get their drive from within themselves.

# Agreeableness:
    As it perhaps sounds, these individuals are warm, friendly, compassionate and cooperative and traits include being kind, affectionate, and sympathetic. In contrast, people with lower levels of agreeableness may be more distant.

# Neuroticism:
    Neuroticism or Emotional Stability relates to degree of negative emotions. People that score high on neuroticism often experience emotional instability and negative emotions. Characteristics typically include being moody and tense.    
"""

    Label(result, text=terms_mean, foreground='green',
          bg='white', anchor='w', justify=LEFT).pack(fill=BOTH)

    result.mainloop()


def perdict_person():
    """Predict Personality"""
    # Closing The Previous Window
    root.withdraw()
    # Creating new window
    top = Toplevel()
    top.geometry('700x500')
    top.configure(background='black')
    top.title("Apply For A Job")
    # Title
    titleFont = font.Font(family='Helvetica', size=20, weight='bold')
    lab = Label(top, text="Personality Prediction", foreground='red',
                bg='black', font=titleFont, pady=10).pack()
    # Job_Form
    job_list = ('Select Job', '101-Developer at TTC',
                '102-Chef at Taj', '103-Professor at MIT')
    job = StringVar(top)
    job.set(job_list[0])

    l1 = Label(top, text="Applicant Name", foreground='white',
               bg='black').place(x=70, y=130)
    l2 = Label(top, text="Age", foreground='white',
               bg='black').place(x=70, y=160)
    l3 = Label(top, text="Gender", foreground='white',
               bg='black').place(x=70, y=190)
    l4 = Label(top, text="Email", foreground='white',
               bg='black').place(x=70, y=220)
    l5 = Label(top, text="Profession", foreground='white',
               bg='black').place(x=70, y=250)
    l6 = Label(top, text="Company Name", foreground='white',
               bg='black').place(x=70, y=280)
    l7 = Label(top, text="Enjoy New Experience or thing(Openness)",
               foreground='white', bg='black').place(x=70, y=310)
    l8 = Label(top, text="How Offen You Feel Negativity(Neuroticism)",
               foreground='white', bg='black').place(x=70, y=340)
    l9 = Label(top, text="Wishing to do one's work well and thoroughly(Conscientiousness)",
               foreground='white', bg='black').place(x=70, y=370)
    l10 = Label(top, text="How much would you like work with your peers(Agreeableness)",
                foreground='white', bg='black').place(x=70, y=400)
    l11 = Label(top, text="How outgoing and social interaction you like(Extraversion)",
                foreground='white', bg='black').place(x=70, y=430)

    sName = Entry(top)
    sName.place(x=450, y=130, width=160)
    age = Entry(top)
    age.place(x=450, y=160, width=160)
    gender = IntVar()
    R1 = Radiobutton(top, text="Male", variable=gender, value=1, padx=7)
    R1.place(x=450, y=190)
    R2 = Radiobutton(top, text="Female", variable=gender, value=0, padx=3)
    R2.place(x=540, y=190)
    email = Entry(top)
    email.place(x=450, y=220, width=160)
    profession = Entry(top)
    profession.place(x=450, y=250, width=160)
    company_name = Entry(top)
    company_name.place(x=450, y=280, width=160)

    openness = Entry(top)
    openness.insert(0, '1-10')
    openness.place(x=450, y=310, width=160)
    neuroticism = Entry(top)
    neuroticism.insert(0, '1-10')
    neuroticism.place(x=450, y=340, width=160)
    conscientiousness = Entry(top)
    conscientiousness.insert(0, '1-10')
    conscientiousness.place(x=450, y=370, width=160)
    agreeableness = Entry(top)
    agreeableness.insert(0, '1-10')
    agreeableness.place(x=450, y=400, width=160)
    extraversion = Entry(top)
    extraversion.insert(0, '1-10')
    extraversion.place(x=450, y=430, width=160)

    submitBtn = Button(top, padx=2, pady=0, text="Submit",
                       bd=0, foreground='white', bg='red', font=(12))
    submitBtn.config(command=lambda: prediction_result(
        top, sName, age, gender, (gender.get(), age.get(), openness.get(), neuroticism.get(), conscientiousness.get(), agreeableness.get(), extraversion.get()), email, profession, company_name))
    submitBtn.place(x=350, y=470, width=200)

    top.mainloop()


if __name__ == "__main__":
    model = train_model()
    model.train()

    root = Tk()
    root.geometry('700x500')
    root.configure(background='white')
    root.title("Personality Prediction System")
    titleFont = font.Font(family='Helvetica', size=25, weight='bold')
    homeBtnFont = font.Font(size=12, weight='bold')
    lab = Label(root, text="Personality Prediction System",
                bg='white', font=titleFont, pady=30).pack()
    b2 = Button(root, padx=4, pady=4, width=30, text="Predict Personality", bg='black', foreground='white',
                bd=1, font=homeBtnFont, command=perdict_person).place(relx=0.5, rely=0.5, anchor=CENTER)
    root.mainloop()
