#### You will find the 'Generate_Reportcard.exe' file inside the src folder
#### before running the .exe file, replace 'Dummy Data.xlsx' with your data
#### keep all students photos inside 'Pics for assignment' folder
#### Note thats photos must be named by fullname, format: fullname.png, e.g: ABC1 XYZ1.png for student name ABC1 XYZ1
#### Outputs will be generated in the folder named 'output'
#### Don't delete any folder, just replace photos(.png) and excel(.xlsx) file with same file extention

>>>
given photos are named by 'Full Name' of students, though there is an
instruction as following 
"Once the program runs, it should pick the 
student photos from the Pics folder as per the student's registration number."

I asked in the chat, but none replied thats why I kept it as given, means Once the program runs, it should pick the 
student photos from the Pics folder as per the student's full name.
<<<

Notes:
* This project is created and executed in Visual Studio Code Version 1.58.2
* using Python 3.9.6, pip 21.2.1
* in a virtual environment 

Windows Terminal Commands:
* Virtual Environment: python -m venv .\venv
* Pandas: pip install pandas
* Openpyxl: pip install openpyxl
* ReportLab: pip install reportlab
* Matplotlib: pip install matplotlib
* Seaborn: pip install seaborn
* PyInstaller: pip install pyinstaller
[Command to convert .py to .exe - pyinstaller.exe --onefile --windowed --icon=app.ico app.py ]

Installed Packeges in Virtual Environment: (checked with command pip freeze)
cycler==0.10.0
et-xmlfile==1.1.0
kiwisolver==1.3.1
matplotlib==3.4.2
numpy==1.21.1
openpyxl==3.0.7
pandas==1.3.1
Pillow==8.3.1
pyparsing==2.4.7
python-dateutil==2.8.2
pytz==2021.1
reportlab==3.5.68
scipy==1.7.0
seaborn==0.11.1
six==1.16.0


Folders:
Output Folder: ./output/

>>>>>>>> All the requirements are covered in the project <<<<<<<<<

Extra Features:
* plots comparison graph: Correct vs Incorrect vs Unattempted
* developed in a virtual environment
* loaded with logo and profile photos
* covers every data from given excel file
* Generates merit list
* Can handle pages for merilist pdf file, perpage=26
* computes merit rank
* shows rank(#) and position(in %) in the test, below profile photo
* line plot for all students attemps vs correct with value levels beside each questions in each report
* computes total score
* upload photos maintains aspect ratio
