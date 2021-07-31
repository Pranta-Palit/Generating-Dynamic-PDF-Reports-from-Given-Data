# Generating Dynamic PDF Reports from Given Data

## Task:
Write a code to create report cards. The details required are mentioned in the excel '**Dummy Data**'. There are 5 students whose report card needs to be created through your program. You can decide the format/design of the report card. These are the conditions 
*	The program should pick up all the information from the excel sheet and start creating PDFs of the report card. The scorecard should have a pic of the student as well. The pics of the 5 students are mentioned in the folder ‘media’
*	You can decide the layout of the report card and any exam name. However, all the information mentioned in the excel sheet should be captured 
*	The scorecard should mention the maximum marks (100) and the score of the student. There are no negative marks.
*	The headers mentioned in blue in the datasheet should be fixed in the report cards, and the marks and responses should change for every student. 
*	Once the program runs, it should pick the student photos from the **media** folder as per the student's registration number or full name. 
*	There needs to be a logo. Pick any logo you wish. It could be scenery for all we care. Pick a white background for the scorecard for clarity
*	.exe file should generate the PDFs (scorecards)

Be creative. As long as you keep up the conditions given above, any (digestible) creativity will be accepted. For example, feel free to throw in some comparison bar graphs if you wish to (for example, Student attempts, World average attempts).

## Implemented Features:
* loaded with logo and profile photos, uploaded photos kept preserving aspect ratio
* covers every data from given excel file
* computes merit position among perticipants (e.g: in top 10%), printed under profile photo in each scorecard
* shows rank(#) in the test round, printed under profile photo in each scorecard
* computes total score obtained and total score tested
* barplot for all students attemps vs correct with value levels beside each questions in each scorecard
* generates merit list pdf including all perticipants
* can handle pages for merilist pdf file, **perpage=26**
* plots comparison graph - Correct vs Incorrect vs Unattempted (**barplot** inside the meritlist pdf)

## Folders:
- **Input Data**:
    - Excel File: _./data/Dummy Data.xlsx_     (_.xlsx_ file required)
    - Student Photos: _./media/_     (_.png_ files required for each student, named by fullname)
- **Output Data**: _./output/>Dummy Data.xlsx_

## Requirements:
This code is written and executed in **Visual Studio Code** (Version 1.58.2) using **Python** 3.9.6 and **pip** 21.2.1 in a virtual environment.
* Pandas (terminal cmd: `pip install pandas`)
* Openpyxl (terminal cmd: `pip install openpyxl`)
* ReportLab (terminal cmd: `pip install reportlab`)
* Matplotlib (terminal cmd: `pip install matplotlib`)
* Seaborn (terminal cmd: `pip install seaborn`)

#### Other Commands:
* to create python virtual environment in windows terminal run `python -m venv .\venv`
* to convert .py file to onefile .exe with appicon run `pyinstaller.exe --onefile --windowed --icon=./static/app.ico ./src/generate_dynamic_reportcards.py`

## Installed Packeges in Virtual Environment:
(checked with command `pip freeze`)

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