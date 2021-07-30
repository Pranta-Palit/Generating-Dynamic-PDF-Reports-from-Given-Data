import pandas as pd
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch
from reportlab.lib import utils
from reportlab.lib.utils import ImageReader

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns
from io import BytesIO


def get_Attempts_vs_Correct_Chart(self, attempts_dict):
    # Initialize the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 9), dpi=300) # 6,15

    # load data from dict of dict
    attempts = [int(attempts_dict[i]['attempt']) for i in attempts_dict.keys()]
    correct = [int(attempts_dict[i]['correct']) for i in attempts_dict.keys()]
    tot_questions = attempts_dict['Q1']['total']

    df = pd.DataFrame()
    df['Student Attempted'] = attempts
    df['Correct Answer'] = correct
    df['Unattempted'] = [tot_questions]* len(attempts_dict.keys())
    df.index = attempts_dict.keys()
    
    sns.set_theme(style="whitegrid")
    # sns.set(font_scale = 12)

    # Plot the attempts
    sns.set_color_codes("pastel")
    sns.barplot(x="Unattempted", y=df.index, data=df,
                label="Unattempted", color="grey")

    # Plot the total questions
    sns.set_color_codes("pastel")
    sns.barplot(x="Student Attempted", y=df.index, data=df,
                label="Incorrect", color="b")

    # Plot the attempts
    sns.set_color_codes("muted")
    sns.barplot(x="Correct Answer", y=df.index, data=df,
                label="Correct", color="b")

    # Add a legend and informative axis label
    ax.legend(ncol=3, bbox_to_anchor =(0.17,-0.12), loc='center left', frameon=True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set(xlim=(0, int(tot_questions)), ylabel="Questions",
        xlabel="Number of Students")
    sns.despine(left=True, bottom=True)


    imgdata = BytesIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)  # rewind the data

    # adjusting image ratio
    w,h = ImageReader(imgdata).getSize()
    aspect = h/float(w)

    self.drawImage(ImageReader(imgdata), 15, 56, 8.2*inch, (8.2*aspect)*inch, mask='auto', preserveAspectRatio=True)


def draw_horizontal_line(self, width, x1,y1,x2,y2, r,g,b):
    # set width and color
    self.setLineWidth(width)
    self.setStrokeColorRGB(r,g,b)
    # start(x1,y1) end(x2,y2)
    self.line(x1,y1,x2,y2)
    self.setStrokeColorRGB(0/255, 64/255, 255/255) # set to default
    
def draw_alligned_image(self, allign, path, x,y, width=5*cm, height=4*cm):
    img = utils.ImageReader(path)

    # if height not given, but width given, then set aspect and resize
    if height!=4*cm:
        iw, ih = img.getSize()
        height = iw * (ih/float(iw))

    if allign=='right':
        x -= width
    self.drawImage(path, x, y, width=width, height=height, mask='auto', preserveAspectRatio=True)


def style_topbar(self):
    # for color convert rgb to 0-1 scale
    draw_horizontal_line(self, 18, 0,833,595.5,833, 0/255,64/255,255/255) # topline
    draw_horizontal_line(self, 18, 0,9,595.5,9, 0/255,64/255,255/255) # bottomline
    
    x = 30
    right_allign_x = 570
    y = 834-75

    # set logo
    logo = './static/logo.png'
    self.drawImage(logo, x, y, mask='auto')

    # set font, color and size
    self.setFillColorRGB(0/255, 64/255, 255/255)
    self.setFont("Helvetica-Bold", 25) #textfont
    # header: Test Name
    self.drawRightString(right_allign_x, y+28, test_info['testname'])

    self.setFont("Helvetica-Bold", 18) #textfont
    self.drawRightString(right_allign_x, y+5, 'Round '+str(test_info['round'])) # test_round_no

    # horizontal line
    y -= 5
    draw_horizontal_line(self, 2, 0,y,595.5,y, 130/255, 130/255,130/255)

    
def style_infobar(self):
    x = 30
    right_allign_x = 570
    y = 754

    # info part: image, name and other info
    y -= 150
    self_image = './media/'+personal_info['fullname']+'.png'
    draw_alligned_image(self, 'right',self_image, right_allign_x, y)
    
    # prints position/rank
    self.roundRect(right_allign_x-120, y-20, 110,15,6, stroke=1, fill=0)
    self.setFont("Helvetica-BoldOblique", 10)
    self.drawRightString(right_allign_x-18, y-16, 'in top {}% (#{})'.format((meritlist[personal_info['regno']]['rank']/len(meritlist))*100 ,  str(meritlist[personal_info['regno']]['rank']))) # rank

    y += 110
    # Bold texts
    self.setFont("Helvetica-BoldOblique", 18)
    self.drawString(x, y, personal_info['fullname']) # fullname 
    self.setFillColorRGB(5/255, 5/255, 5/255)
    self.setFont("Helvetica-Bold", 12)

    # headlines
    self.drawString(x, y-20, "First Name") #firstname
    self.drawString(x, y-35, "Last Name") #lastname
    self.drawString(x, y-50, "Gender") #gender
    self.drawString(x, y-65, "Date Of Birth") #dob
    self.drawString(x, y-80, "Residential Address") #city, country
    self.drawString(x, y-95, "Name of School") #schoolname
    self.drawString(x, y-110, "Grade") #grade
    self.drawString(x, y-125, "Registration No") #registration number
    
    y = 714
    # values
    self.setFont("Helvetica-BoldOblique", 12)
    self.drawString(x+120, y-20, ": "+personal_info['firstname']) #firstname
    self.drawString(x+120, y-35, ": "+personal_info['lastname']) #lastname
    self.drawString(x+120, y-50, ": "+personal_info['gender']) #gender
    self.drawString(x+120, y-65, ": "+personal_info['dob']) #dob
    self.drawString(x+120, y-80, ": "+personal_info['city']+", "+personal_info['country']) #city, country
    self.drawString(x+120, y-95, ": "+personal_info['school']) #schoolname
    self.drawString(x+120, y-110, f": {personal_info['grade']}") #grade
    self.drawString(x+120, y-125, ": "+personal_info['regno']) #registration number

    # horizontal line
    y = 570
    draw_horizontal_line(self, 2, 0,y,595.5,y, 130/255, 130/255,130/255)


def style_result(self):

    x = 30
    right_allign_x = 565
    y = 545

    self.setFillColorRGB(0/255, 64/255, 255/255)
    self.setFont("Helvetica-Bold", 20) #textfont
    
    # header: Test Report
    self.drawString(x, y, "Test Report") # static
    self.drawRightString(right_allign_x, y, "Max Marks : "+str(test_info['maxmarks']))

    # horizontal line
    y -= 10
    draw_horizontal_line(self, 2, 0,y,595.5,y, 130/255, 130/255,130/255)

    y -= 12
    draw_horizontal_line(self, 1, x,y,right_allign_x,y, 0/255, 64/255, 255/255)

    y -= 20
    # table column header
    self.setFont("Helvetica-Bold", 14)
    self.drawString(x+5, y, "Question")
    self.drawString(x+80, y, "Your")
    self.drawString(x+74, y-13, "Answer")
    self.drawString(x+135, y, "Correct")
    self.drawString(x+135, y-13, "Answer")
    self.drawString(x+200, y, "Outcome")
    self.drawString(x+290, y, "Your")
    self.drawString(x+288, y-13, "Score")
    self.drawString(x+352, y, "Max")
    self.drawString(x+347, y-13, "Score")
    

    self.drawString(x+406, y+3, "Students Average")
    self.drawString(x+435, y-13, "Attempts")

    y -= 21
    draw_horizontal_line(self, 1, x,y,right_allign_x,y, 0/255, 64/255, 255/255)

    y -= 15
    # add rows in table
    for q in range(0, len(test_info['qno'])):
        add_row(self, test_info['qno'][q], test_info['marked_ans'][q], test_info['correct_ans'][q], test_info['outcome'][q], test_info['cs'][q], test_info['ys'][q], x, y)
        y -= 17.5

    
    # vertical lines
    self.line(x,523,x,y+12) # most left
    self.line(right_allign_x,523,right_allign_x,y+12) # most right
    self.line(x+70,523,x+75,y+12) # after qstn no
    self.line(x+130,523,x+130,y+12) # after your ans
    self.line(x+190,523,x+190,y+12) # after correct ans
    self.line(x+280,523,x+280,y+12) # after outcome
    self.line(x+335,523,x+335,y+12) # after your score
    self.line(x+400,523,x+400,y+12) # after questions max score

    y -= 5
    self.setFont("Helvetica-BoldOblique", 14)
    # Date and time of test
    self.drawString(x, y, "Date and Time of Test : "+test_info['test_time'])

    # your score
    total_score_obtained = sum(test_info['ys'])
    total_score_for_test = sum(test_info['cs'])
    self.drawRightString(right_allign_x, y, f"Your Total Score : {total_score_obtained}/{total_score_for_test}")

    # Final result
    # header: Test Report
    y = 4
    self.setFont("Helvetica-Bold", 15)
    self.setFillColorRGB(1, 1, 1)
    self.drawString(x, y, 'Final Result: '+test_info['final_result'])


def add_row(self, qn, ans, ca, outcome, cs, ys, x, y):

    self.setFont("Helvetica-Bold", 12)
    self.drawString(x+25, y, qn)
    self.drawString(x+95, y, ans)
    self.drawString(x+155, y, ca)
    self.drawString(x+202, y, outcome)
    self.drawString(x+305, y, str(ys))
    self.drawString(x+362, y, str(cs))

    draw_horizontal_line(self, 1, x,y-5,565,y-5, 0/255, 64/255, 255/255)

def load_excel_data():

    print('loading data',end='')
    data = pd.read_excel('./data/Dummy Data.xlsx', sheet_name='Sheet1')
    print(end='.')
    data.columns = data.iloc[0,:] #set excels first row as df columns name
    print(end='.')
    data = data.iloc[1:,:] # drop first row
    print(end='.')
    # drop nan value in marked_ans
    data.iloc[:,14].fillna('',inplace=True)

    # get total student using Candidate No column
    total_student = max(data['Candidate No. (Need not appear on the scorecard)'])

    # generate merit list
    global meritlist
    meritlist = {}
    for id in range(1,total_student+1):
        student = data[data['Candidate No. (Need not appear on the scorecard)']==id]
        student = student.iloc[:,[4,5,17,18]]
        meritlist[str(student.iloc[0,1])] = {
            'name': student.iloc[0,0],
            'total_marks': sum(student.iloc[:,2].astype(int)),
            'total_obtained_marks': sum(student.iloc[:,3].astype(int)),
            'rank': 0
        }
    meritlist =  dict(sorted(meritlist.items(), key=lambda item: item[1]['total_obtained_marks'], reverse=True))

    # set rank
    r=1
    for id in meritlist.keys():
        meritlist[id]['rank'] = r
        r +=1

    # find attempts and success count for each questions
    global attempt_vs_correct_dict
    attempt_vs_correct_dict = {}
    for q in data.iloc[:,13].unique():
        temp_data = data[data['Question No.']==q][['Outcome (Correct/Incorrect/Not Attempted)']]
        
        attempt = (temp_data['Outcome (Correct/Incorrect/Not Attempted)'] != 'Unattempted').sum()
        correct = (temp_data['Outcome (Correct/Incorrect/Not Attempted)'] == 'Correct').sum()
        total = len(temp_data)

        attempt_vs_correct_dict[q]= {'attempt': attempt, 'correct': correct, 'total': total}

    print('done!')
    
    global personal_info
    global test_info
    for id in range(1,(total_student+1)):
        student = data[data['Candidate No. (Need not appear on the scorecard)']==id]
        student = student.iloc[:,1:]
        
        personal_info = {
            'firstname': str(student.iloc[1,1]),
            'lastname': str(student.iloc[1,2]),
            'fullname': str(student.iloc[1,3]),
            'regno': str(student.iloc[1,4]),
            'grade': int(student.iloc[1,5]),
            'school': str(student.iloc[1,6]),
            'gender': str(student.iloc[1,7]),
            'dob': str(student.iloc[1,8]),
            'city': str(student.iloc[1,9]),
            'country': str(student.iloc[1,11]),
        }

        test_info = {
            'testname': 'English Mock Test',
            'maxmarks': 100,
            'round': student.iloc[1,0],
            'test_time': str(student.iloc[1,10]),
            'qno': [str(qn) for qn in student.iloc[:,12]],
            'marked_ans': list(student.iloc[:,13]),
            'correct_ans': list(student.iloc[:,14]),
            'outcome': list(student.iloc[:,15]),
            'cs': [int(cs) for cs in student.iloc[:,16]],
            'ys': [int(ys) for ys in student.iloc[:,17]],
            'final_result': student.iloc[1,18]
        }
        print('data collection for '+personal_info['fullname']+': [completed]')
        generate_pdf()


def generate_pdf():
    print('generating result for '+personal_info['fullname'],end='')
    
    # creating pdf file
    canvas = Canvas('./output/'+personal_info['fullname']+'.pdf', pagesize=A4)
    print(end='.')
    style_topbar(canvas)
    print(end='.')
    style_infobar(canvas)
    print(end='.')
    style_result(canvas)
    print(end='.')
    draw_attempt_vs_correct(canvas)
    print(end='.')
    canvas.save()
    print('file '+personal_info['fullname']+'.pdf [generated]')

def draw_attempt_vs_correct(self):
    # attempt color code (155/255,34/255,138/255) purple
    # correct color code (127/255,255/255,0/255) green
    # default color code (0/255, 64/255, 255/255) blue

    self.setFillColorRGB(0/255, 64/255, 255/255)
    self.setFont("Helvetica-BoldOblique", 8)

    x = 30
    right_allign_x = 565
    y = 470
    
    # draw_horizontal_line(self, width, x1,y1,x2,y2, r,g,b)
    for q in attempt_vs_correct_dict.keys():
        # x2=x+530, 530-438 = 92 (full) - for printing number

        # for attempt
        x2 = 434 + 86 * (attempt_vs_correct_dict[q]['attempt'] / float(attempt_vs_correct_dict[q]['total']) )
        self.setFontSize(8)
        self.drawString(x+402, y+1, "attempt:")
        draw_horizontal_line(self, 6, x+434,y+4,x+x2,y+4, 155/255,34/255,138/255)
        self.setFontSize(5)
        self.drawString(x+x2-1, y+3, "-|"+str(attempt_vs_correct_dict[q]['attempt']))

        
        # for correct
        x2 = 434 + 86 *(attempt_vs_correct_dict[q]['correct']/float(attempt_vs_correct_dict[q]['total']))        
        self.setFontSize(8)
        self.drawString(x+403, y-6, "correct:")
        draw_horizontal_line(self, 6, x+434,y-3,x+x2,y-3, 127/255,255/255,0/255)
        self.setFontSize(5)
        self.drawString(x+x2-1, y-4.5, "-|"+str(attempt_vs_correct_dict[q]['correct']))
        y -= 17.5

def draw_vertical_lines(self, x1,y1,x2,y2):
    self.setLineWidth(1.3)
    self.setStrokeColorRGB(0/255, 64/255, 255/255)
    self.line(x1,y1,x2,y2)
    self.line(x1+100,y1,x2+100,y2)
    self.line(x1+270,y1,x2+270,y2)
    self.line(x1+420,y1,x2+420,y2)
    self.line(x1+535,y1,x2+535,y2)
    draw_horizontal_line(self, 1.3, x1,y2,565,y2, 0/255, 64/255, 255/255)


def new_page_meritlist(self, title, plotpage=False):
    style_topbar(self)
    
    x=30
    right_allign_x = 565
    y = 750

    # header: Round 2 - Merit List
    y -= 20
    self.setFontSize(20)
    
    if plotpage is False:
        self.drawString((right_allign_x-x)/2 -60, y, title) # static
        draw_horizontal_line(self, 2, 0,y-8,595.5,y-8, 130/255,130/255,130/255)

        y -= 15
        draw_horizontal_line(self, 1.3, x,y,right_allign_x,y, 0/255, 64/255, 255/255)

        # table column header
        self.setFont("Helvetica-Bold", 16)
        self.drawString(x+30, y-18, "Rank")
        self.drawString(x+125, y-18, "Registration No")
        self.drawString(x+320, y-18, "Name")
        self.drawString(x+450, y-18, "Score")

        draw_vertical_lines(self, x, y ,x, y-25) # header end
    else:
        self.drawString(130, y, title) # static
        draw_horizontal_line(self, 2, 0,y-8,595.5,y-8, 130/255,130/255,130/255)
    
    self.setFont("Helvetica-Bold", 12)

def generate_merit_list():
    # creating pdf file
    canvas_meritlist = Canvas('./output/'+str(test_info['testname']).replace(' ','_')+'_Round_'+str(test_info['round'])+'_Merit_List.pdf', pagesize=A4)
    
    title = f"Round {str(test_info['round'])} - Merit List"
    new_page_meritlist(canvas_meritlist, title)

    x,y = 30, 690
    perPage = 26
    for id in meritlist.keys():
        if perPage==0:
            canvas_meritlist.showPage()
            new_page_meritlist(canvas_meritlist,title)
            x,y = 30, 690
            perPage = 26

        canvas_meritlist.drawString(x+40, y-18, str(meritlist[id]['rank']))
        canvas_meritlist.drawString(x+135, y-18, id)
        canvas_meritlist.drawString(x+310, y-18, meritlist[id]['name'])
        canvas_meritlist.drawString(x+455, y-18, str(meritlist[id]['total_obtained_marks'])+"/"+str(meritlist[id]['total_marks']))
        draw_vertical_lines(canvas_meritlist, x, y ,x, y-25) # header end
        y -= 25
        perPage -= 1
    

    # drawing plots in a new page inside meritlist pdf
    print('plotting comparison graph inside meritlist...please wait...')
    canvas_meritlist.showPage()
    new_page_meritlist(canvas_meritlist, 'Correct vs Incorrect vs Unattempted', True)
    get_Attempts_vs_Correct_Chart(canvas_meritlist,attempt_vs_correct_dict)
    canvas_meritlist.save()

if __name__=="__main__":
    # loading data
    load_excel_data()

    #meritlist
    generate_merit_list()
