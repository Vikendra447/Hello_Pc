from Tkinter import *
root=Tk()
root.title('PYTHON PROJECT')
var2 = StringVar()
var2.set(" ")
var1 = StringVar()
var1.set(" ")
Label(root,text=' J  O  B    S  E  A  R  C  H', font=('Helvetica',25),fg='black',relief=SUNKEN,bg='green').grid()
Label(root,text='Student_Name', font=('Helvetica',15),fg='red').grid(row=1,column=0,sticky=W)
Label(root,text='Vikendra Singh',width=12, font=('Helvetica',15),fg='blue').grid(row=1,column=0,sticky=E)
Label(root,text='EnrolL_nO.', width=12,font=('Helvetica',15),fg='red').grid(row=2,column=0,sticky=W)
Label(root,text='151447   ',width=12, font=('Helvetica',15),fg='blue').grid(row=2,column=0,sticky=E)
Label(root,text='Batch    ', width=12,font=('Helvetica',15),fg='red').grid(row=3,column=0,sticky=W)
Label(root,text='B-7      ', width=12,font=('Helvetica',15),fg='blue').grid(row=3,column=0,sticky=E)
Label(root,text='Branch     ', width=12,font=('Helvetica',15),fg='red').grid(row=4,column=0,sticky=W)
Label(root,text='SCE       ',width=12, font=('Helvetica',15),fg='blue',).grid(row=4,column=0,sticky=E)
Label(root,text='Submitted to     ', width=12,font=('Helvetica',15),fg='red').grid(row=5,column=0,sticky=W)
Label(root,text='DR.Mahesh kumar',width=15, font=('Helvetica',15),fg='blue',).grid(row=5,column=0,sticky=E)
Button(root,text='find job              find resume          Employers / Post Job                                                               Post your resume       Sign/login',bg='black',fg='red',width=150).grid(row=10,column=0)

def start():
    Label(root,text='indeed:',font=('Helvetica',50),fg='blue').grid(row=19,column=0,sticky=W)
    Label(root,text='what',font=('Helvetica',30),fg='red').grid(row=20,column=0,sticky=W)
    Label(root,text='where',font=('Helvetica',30),fg='red').grid(row=20,column=0)
    op=OptionMenu(root,var2,'Delhi','Banglore','Chennai','Bhopal','Mumbai','Wizag','Ahamdabad','Indore','Madhyapredesh','Punjab','Surat','Uttarpradesh','Chhatisgarh','Gujrat')
    op.grid(row=21,column=0)
    op=OptionMenu(root, var1,"Copmuter Science","Civil","Electronic","Electrical",'Machenical','Teacher','Banking','Medical','Army','Online marketing','Civil survice')
    op.grid(row=21,column=0,sticky=W)
    def find():
        import Tkinter
        root=Tk()
        if var1.get()=='Copmuter Science':
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Copmuter Science]\n\nCustomer Service Executive (CSE):\nOperations and Customer Quality Engineer II - (E2) :\nSr. Software Development Engineer in Test (SDET): \nTelephonic Clinical Counselor:\nPrincipal Business Analyst, India IT\:nSDSO Knowledge Training & Compliance Expert:\nManual Testing(Gherkin Language):\nSMTS Software Engineer:\nSoftware Engineer 2:\nTechnical Helpdesk Management:\nEngineering Manager - DWH/Big Data:\nClient Service Executive').grid()
        elif var1.get()=="Civil":
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Civil]\n\nAutocadd Draftsperson:\nPROJECT MANAGER - CIVIL:\nSite Engineer (Civil):\nSite Engineers:\nCivil Engineer - QS:\nAutoCAD Draftsman:\nMarketing Executives, Civil Engineer, Store Incharge & Recep:\nTrainee Testing Engineer:\nUrgently Looking for a project coordinator ( civil ):\nSite Supervisor (Civil) - Building Construction having 5 Yrs:\nCivil Engineer walk in Interview 15 nov 2016 to 26 nov 2016:').grid()
        elif var1.get()=="Electronic":
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Electronic]\n\nField Application Engineer - 5093:\nSenior Application Engineer - 4885:\nSenior Statistical Programmer :\nElectronics Engineering walk 15 nov 2016 to 26 nov 2016:\nJunior-Engg CAM-Diploma ,Electrical / Electronics / Mecatron:\nSOLDERING & PANEL ASSEMBLER:\nElectronic Engineering Jr:\nHardware Designer / Technician:\nR&D Engineer - Electronics: \nEngineer (Electrical/Electronics):\nSystem Engineer Power Breaker:\nPurchase Exeutive (Electrical and Electronics)').grid()
        elif var1.get()== "Electrical":
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Electrical]\n\nElectrical Maintenance Engineer:\nElectrical Engineering walk in 15nov 2016 to 26 nov 2016:\nElectrical Engineer:\nEngineer (Electrical):\nElectrical Engineer (Maintenance):\nElectrical Design Engineer:\nElectrical Technician:\nJunior-Engg CAM-Diploma ,Electrical / Electronics / Mecatron:\nSenior Test Engineer :\nRisk Engineer ').grid()
        elif var1.get()== "Machenical":
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Machenical]\n\nGeneral Manager / Dy. General Manager - Operation:\nMechanical Engineer Fresher,Electrical:\nMechanical Engineer:\nMechanical and Automobile Engineering:\nTrainee Engineer:\nMechanical plant inchage:\nmechanical engineer freshers:\nTrainee Engineer(ITI/ Dip Mechanical) Pithampur:\nMechanical / Thermo Mechanical Engineer').grid()
        elif var1.get()== "Teacher":
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Teacher]\n\nPGT,TGT,PRT All subject teachers for Next Academic Session:\nWanted primary teachers for cbse school:\nPrimary & Pre Primary Teachers:\nJOB FOR NGO:\nSubject Expert Teacher (Curriculum Based-State/CBSE/ICSE):\nCenter Head - EuroKids Preschool / Creche:\nUrgent Requirement of Computer Teacher:\nPrincipal required for an upcoming CBSE School at Seoni:\nPre-primary Teacher').grid()
        elif var1.get()== "Banking":
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Banking]\n\nFemale Candidate Back Office Work and Telecalling :\nassistant manager, operations - banking, credit and investme.:\nbanking operations:\nFRESHERS IN BANKING OPERATION:\nInterviews for Banking Sector:\nJobs In Banking Sector:\nRelationship Manager- Commercial Business Banking:\nVacancy in Bank\nback office executive for Banking Sector:\nassistant manager, corporate banking services').grid()
        elif var1.get()== "Medical":
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Medical]\n\nClinical Data Associate :\nMedical Officer and Hindi Officer / AR:\nCOMPANY SUPERVISOR:\nTransaction Processor II, Service Delivery\nMedical Transcriptionist for CT-MRI:\nMedical Officer MBBS:\nMedical Officer (Female doctor):\nJunior Scientific Officer (Explosives):\nVacancy for Medical Representative (MR / AM / ZM / RM):\nCRM/Customer Relationship Officer/Relationship Manager').grid()
        elif var1.get()== "Army":
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Army]\n\nOperations Analyst:\nBTL & Trade Marketing Executive :\nSecurity Officer:\nCounselor/TGT:\nRegional Head West:\nMale Warden:\nHead - DRA ( Regulatory Affairs ):\nLabour Officer:\nWARDENS\nBusiness Development Executive:\n[Government] Security Watchman cum Fireman (Second Attempt)').grid()
        elif var1.get()== "Online marketing":
            Label(root,bg='black',fg='white',text='[YOU HAVE AVAILABLE JOB FOR Online marketing]\n\nMarketing and Business Development Executive:\nSr. Analyst - Email Operations:\nSales & Marketing Manager :\nDigital Marketing Executive:\nDigital Marketing Manager:\nUrgent Requirement for Digital Marketing Manager:\nOnline Marketing Manager for E Commerce:\nUrgently required Marketing/Branding Manager for FMCG sector:\nFront End Developer - SDE II ').grid()
        mainloop()
    Label(root,text='job title, keywords or company name',fg='blue').grid(row=22,column=0,sticky=W)
    Button(root,text='find jobs',width=15,height=1,command=find).grid(row=21,column=0,sticky=E)
    Label(root,text='city or postcode',fg='blue').grid(row=22,column=0)
    Label(root,text='Advanced job search',fg='blue').grid(row=22,column=0,sticky=E)
Button(root,text='LET BEGIN YOUR PROJECT WORK',command=start,height=2,bg='green').grid(row=6,column=0)
root.mainloop()
