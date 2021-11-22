#Commented USN column as the entries to it is showing as 'Datatype Mismatch'. Except that issue everything works fine
#Due to no access to USN , update and delete are on halt, the iterating and fetching vales from user given data is ready, but without USN
# we can't access that.

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
engine = create_engine('sqlite:///task_1.db', echo=True)
meta = MetaData()

study = Table(
    'student', meta,
    #Column('USN', String, primary_key= True),
    Column('Name', String),
    Column('Gender', String),
    Column('Entry', String),
    Column('YOA', Integer),
    Column('Migration', Boolean),
    Column('Transfer_details', String),
    Column('admission', Boolean),
    Column('admission_div', String),
    Column('YOP', Integer),
    Column('degree_type', String),
    Column('pu_marks', Integer),
    Column('entrance_marks', Integer),
    Column('rank', Integer), 
)
meta.create_all(engine)
conn = engine.connect()


def create():
    N = int(input("Enter the number of student's details to be entered: "))
    for i in range(N):
        #sUSN = input("Enter the USN of the student: ")
        sName = input("Enter the name of the student: ")
        sGender = input("Gender :")
        sEntry = input("Type of entry(Normal/Lateral) : ")
        sYOA = input("Enter the year of admission : ")
        
        sMigration = input("Has the student migrated to other programs or institutions(Yes/No):")
        if sMigration == "Yes":
            sMigration = True
        elif sMigration == "No":
            sMigration = False
        
        sTransfer_details = input("Enter the details of transfer :")
        sadmission = input("Did the student take admission in separate division(Yes/No) :")
        if sadmission == "Yes":
            sadmission = True
        elif sadmission == "No":
            sadmission = False
        sadmission_div = input("Enter the details of admission in separate division :")
        sYOP = input("Year of passing :")
        sdegree = input("UG/PG : ")
        smarks = input("Marks obtained in 12th in PCM subjects :")
        sentrance_marks = input("Marks obtained in entrance exam :")
        srank = input("Rank in entrance exam :")
        result = conn.execute(study.insert(),
                              [{'Name': sName, 'Gender': sGender, 'Entry': sEntry, 'YOA': sYOA , 'Migration': sMigration,
                                'Transfer_details': sTransfer_details, 'admission': sadmission, 'admission_div': sadmission_div,
                               'YOP': sYOP, 'degree_type': sdegree, 'pu_marks': smarks, 'entrance_marks': sentrance_marks, 'rank': srank
                              }])
        
def read():
    dataview = study.select()
    result = conn.execute(dataview)
    for row in result:
        print (row)
create()        
