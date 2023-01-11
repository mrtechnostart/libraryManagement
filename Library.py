import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
import datetime
conn = sqlite3.connect('library.db')
c=conn.cursor()
c.execute("create table if not exists libTab(CollegeID varchar(20),Course varchar(20),BookCode varchar(20),StudentName varchar(20),DateOfIssue varchar(20))")
# c.execute(")
# conn.commit()

def displayRec():
    c.execute("Select * from libTab")
    data = pd.DataFrame(c.fetchall(),columns=["CollegeID","Course","BookCode","StudentName","DateOfIssue"])
    return data
def issueBook():
    CollegeID = st.text_input("Collge ID Here: ")
    Course = st.text_input("Enter Course")
    BookCode = st.text_input("Book Code")
    StudentName = st.text_input("Student Name Here: ")
    DateOfIssue = str(datetime.date.today())
    btn = st.button("Submit")
    btn1 = st.button("Display Records")
    if btn1:
        st.dataframe(displayRec())
    if btn:
        c.execute('insert into libTab(CollegeID,Course,BookCode,StudentName,DateOfIssue) values(?,?,?,?,?)',(CollegeID,Course,BookCode,StudentName,DateOfIssue))
        conn.commit()
        st.success("Records Added Successfully!")
def deleteRecords():
    CollegeID = st.text_input("Enter College ID Here: ")
    bookCode = st.text_input("Enter BookCode Here")
    btn = st.button("Delete Now!")
    if btn:
        Query="delete from libTab where CollegeID='{}' and BookCode='{}'".format(CollegeID,bookCode)
        c.execute(Query)
        conn.commit()
        st.success("Records Deleted Successfully")
        st.write("Updated Records")
        st.dataframe(displayRec())
def letter():
    st.title("Library Management Program")
    st.subheader("Dashboard")
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home","Issue Book","Delete Records","About"],
        icons=["house","book","envelop","contact"],
        menu_icon="cast",
        orientation="horizontal"
        )
    if selected=="Home":
        st.markdown('Library Management By Nishika Kumari CSE3')
    if selected=="Issue Book":
        issueBook()
    if selected=="Delete Records":
        deleteRecords()
letter()