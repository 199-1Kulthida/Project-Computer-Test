import sqlite3 as sql #โมดูลsql
import os
from datetime import datetime, timedelta
from time import sleep

os.system("cls") #clear screen
def my_introduction(): #intro
    print("\u001b[41;1m 💻 Computer Test 💻 \u001b[0m".rjust(110)) #ให้ชิดขวา และระบุความยาวเป็น 110 ตัวอักษร
    print("ชั้นประถมศึกษาปีที่ 3".rjust(104))
    print("🏫โรงเรียนบ้านหนองชิงกาเบล🏫\n".rjust(105))
    print("ครูผู้สอน".rjust(96))
    print("นางสาวกุลธิดา แสนพันนา".rjust(102))
    print("นางสาวรัชฎาภรณ์ ศรัทธาคลัง\n".rjust(106))
    print("\u001b[33;1m 📖 แบบทดสอบวัดความรู้ทางด้านคอมพิวเตอร์ 📚 \u001b[0m\n".rjust(125))

class_y = ""
dt = sql.connect(r"E:\Project_Python\SQL\data.db") #สร้างตัวแปล dt เพื่อที่จะเก็บฐานข้อมูลผู้ใช้
cn = sql.connect(r"E:\Project_Python\SQL\question.db") #สร้างตัวแปล cn เพื่อที่จะเก็บฐานข้อมูลโจทย์
con = sql.connect(r"E:\Project_Python\SQL\quiz.db") #สร้างตัวแปล con เพื่อที่จะเก็บฐานข้อมูลchoice

#สร้างข้อสอบ
q = [] #สร้างตัวแปร q ขึ้นมาเก็บของส่วนของคำถาม
c = [] #สร้างตัวแปร c ขึ้นมาเก็บของส่วนของตัวเลือก
my_answer = [] #สร้างตัวแปร my_answer ขึ้นมาเก็บคำตอบที่ผู้ใช้เลือก
score = 0 #สร้างscoreเริ่มต้น=0
answer = ["D","A","B","D","C","C","B","C","B","D","D","D","B","B"] #เป็น List ของ String ที่ใช้สำหรับเก็บเฉลย
for i in cn.execute("select * from q_and_a"): #สร้างfor i ไปหมุนในฐานข้อมูลของโจทย์ ดึงข้อมูลจากdatabaseมาเก็บไว้แต่ละตัวแปร
    q.append(i) #เอาค่า i ที่หมุน มาเก็บใน q 
for i in con.execute("select * from choice"): #iไปหมุนในฐานข้อมูลของตัวเลือก เพื่อที่จะดึงข้อมูลมาเก็บไว้
    c.append(i) #เอาค่า i ที่หมุน มาเก็บใน c

#ตรวจสอบตัวอักษร
word = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮะาิีึืุูเแโัๆใไๅฤฦ่้๊๋์" #สร้างตัวแปล word เพื่อเก็บข้อมูลของตัวพยัญชนะภาษาไทย,สระ,วรรณยุกต์
def check(x):
    try:
        if x.isalpha():
            return True
        else:
            for i in x:
                if i not in word:
                    return False
            return True
    except Exception:
        return False

#เข้าสู่ระบบของนักเรียน   
def student():
    while True:
        os.system("cls")
        my_introduction()
        global fname,lname,start_time
        print("\u001b[44;1m 🌻 ล ง ท ะ เ บี ย น 🌻 \u001b[0m\n".rjust(113)) #ลงทะเบียนชื่อเข้าdatabase
        fname = str(input("\t\t\t\t\t\t\u001b[37;1mกรอกได้ทั้งภาษาไทยและภาษาอังกฤษ * \u001b[0mชื่อ : "))  
        if check(fname) == True:
            lname = input("\t\t\t\t\t\t\u001b[37;1mกรอกได้ทั้งภาษาไทยและภาษาอังกฤษ * \u001b[0mนามสกุล : ")
            if check(lname) == True:
                while True:
                    try:
                        c = int(input("\t\t\t\t\t\t\t\t   💚 ประถมศึกษาปีที่ 3/1 พิมพ์ 1\n\t\t\t\t\t\t\t\t   🧡 ประถมศึกษาปีที่ 3/2 พิมพ์ 2\n\t\t\t\t\t\t\t\t   💙 ประถมศึกษาปีที่ 3/3 พิมพ์ 3\n\t\t\t\t\t\t\t\t\tชั้นเรียน : "))
                        if c == 1:
                            class_y = "ป.3/1"
                            break
                        elif c == 2:
                            class_y = "ป.3/2"
                            break
                        elif c == 3:
                            class_y = "ป.3/3"
                            break
                        else:
                            print("⚠️ กรุณาทำรายการให้ถูกต้อง ⚠️".rjust(100))
                            sleep(1.5)
                    except ValueError:
                        print("⚠️ กรุณากรอกเฉพาะตัวเลข ⚠️".rjust(100))
                        sleep(1.5)
                while True:
                    try:
                        id = int(input("\t\t\t\t\t\t\t\t\tเลขที่ : "))
                        break
                    except ValueError:
                        print("\t\t\t\t\t\t\t\t\t⚠️ กรุณากรอกเฉพาะตัวเลข ⚠️")
                        sleep(1.5)
    
            else:
                print("\t\t\t\t\t\t\t\t\t   ⚠️ กรุณากรอกให้ถูกต้อง ⚠️") #ถ้ากรอกตัวเลขจะขึ้น
                sleep(1.5)
                student()
        else:
            print("\t\t\t\t\t\t\t\t\t   ⚠️ กรุณากรอกให้ถูกต้อง ⚠️")
            sleep(1.5)
            student()
            

        start_time = datetime.today() #เวลาเริ่มทำข้อสอบ
        start(class_y,id)



def start(class_y,id): #สร้างข้อสอบ
    i = 0
    while (i<len(q)): #for i จะวนเท่ากับจำนวนข้อมูลที่อยู่ในตัวแปร q ซึ่งเป็นชนิด List โดยใช้คำสั่ง len
        os.system("cls") 
        print(f"\n🔸ข้อ {i+1}. {q[i][1]}") #ค่าของ list ในindexจะเริ่มต้นนับที่ 0 แสดงค่าqในidexที่ i 0  โดยที่ i จะเปลี่ยนไปเรื่อยๆตามจำนวนข้อมูลq
        print(f"\t⭕ A. {c[i][1]} \n\t⭕ B. {c[i][2]} \n\t⭕ C. {c[i][3]} \n\t⭕ D. {c[i][4]}\n") #indexที่0-1-2-3จะไม่เปลี่ยนแปลง แต่indexที่i จะเปลี่ยนไปเรื่อยๆตามจำนวนของข้อมูลที่อยู่ในc
        get_answer = input("\n✅ คำตอบที่ถูกต้อง คือ ").upper().strip() #ถ้าผู้ใช้ป้อนตัวเล็กหรือช่องว่างโปรแกรมก็จะเปลี่ยนเป็นตัวใหญ่และไม่นับช่องว่าง
        if get_answer.isalpha() == False or len(get_answer) > 1 or len(get_answer) < 1 or get_answer not in "ABCD":
            print("⚠️ โปรดเลือกคำตอบที่อยู่ในเงื่อนไขเท่านั้น ⚠️")
            sleep(1.5)
        else:
            print("-"*80)
            my_answer.append(get_answer) #เอาข้อมูลที่ผู้ใช้กรอก get_answer มาเก็บใน list ว่างที่สร้างไว้ชื่อ my_answer
            i += 1
    edit(score,fname,lname,class_y,id) #ตรวจสอบความถูกต้องของข้อสอบ

#สร้างตัวเลือก
def edit(score,fname,lname,class_y,id): #ส่งค่าที่อยู่นอกdef
    while True: #ตรวจคำตอบ
        os.system("cls")
        print("\n\u001b[43;1m ✔️ ตรวจคำตอบของคุณ ✔️ \u001b[0m".rjust(90)) 
        print("-"*80)
        for i in range(len(q)): # i จะวนเท่ากับจำนวนข้อมูลที่อยู่ในตัวแปร q ซึ่งเป็นชนิด List โดยใช้คำสั่ง len
            print(f"\n🔸ข้อ {i+1}. {q[i][1]}") #ค่าของ list ในindexจะเริ่มต้นนับที่ 0 แสดงค่าqในidexที่ i 0  โดยที่ i จะเปลี่ยนไปเรื่อยๆตามจำนวนข้อมูลq
            print(f"\t⭕ A. {c[i][1]} \n\t⭕ B. {c[i][2]} \n\t⭕ C. {c[i][3]} \n\t⭕ D. {c[i][4]}\n") #indexที่0-1-2-3จะไม่เปลี่ยนแปลง แต่indexที่i จะเปลี่ยนไปเรื่อยๆตามจำนวนของข้อมูลที่อยู่ในc
            print(f"\nคำตอบของคุณคือ {my_answer[i]}") #คำตอบของผู้ใช้ที่เลือก
            print("-"*80)

        way = input("\n⚠️ นักเรียนต้องการแก้ไขคำตอบกด [E] หรือ เมื่อมั่นใจในข้อสอบแล้วกด [Enter] เพื่อส่งคำตอบพร้อมผลคะแนน --> ")
        if way.upper().strip()=="E":#เลือก E
            choice = int(input("\n🔸เลือกข้อที่ท่านต้องการแก้ไข > "))
            if choice > len(q):
                print("⚠️ โปรดเลือกคำตอบที่อยู่ในเงื่อนไขเท่านั้น ⚠️")
                sleep(1.5)
            new_answer = input("✔️ เลือกคำตอบใหม่ของคุณ > ").strip().upper()
            if new_answer.isalpha() == False or len(new_answer) > 1 or len(new_answer) < 1 or new_answer not in "ABCD":
                print("⚠️ โปรดเลือกคำตอบที่อยู่ในเงื่อนไขเท่านั้น ⚠️")
                sleep(1.5)
                continue
            my_answer[choice-1]=new_answer #คำตอบตอนแรกที่ผู้ใช้เลือกจะเป็นคำตอบใหม่ โดยที่จะให้ choice-1 
        else : #Enter
            end = datetime.today() #เวลาที่สิ้นสุดการทำข้อสอบ
            diff = end - start_time #คำนวณเวลาที่เริ่มต้น-เวลาที่สิ้นสุด
            for i in range(len(my_answer)): # i จะวนเท่ากับจำนวนข้อมูลที่อยู่ในตัวแปร my_answer เพื่อตรวจคำตอบ 
                if my_answer[i] == answer[i]: #ถ้า my_answerค่าตรงกันตรงกับanswer
                    score = score + 1
                else: #แต่ถ้าค่าไม่ตรงกัน
                    score = score + 0
            break
    os.system("cls")
    print("\n"*6)
    print("\n\t\u001b[33;1m 📚ผลคะแนนทำแบบทดสอบ📚 \u001b[0m\n".rjust(125))
    print("-"*45)
    print(f"\n🌷 คะแนนของ {fname} {lname} คือ {score} เต็ม {q[i][0]} 🌷\n") #แสดงคะแนนสอบ
    print("-"*45)
    cmd = f"""insert into register(fname,lname,class,id,score)
    values('{fname}','{lname}','{class_y}','{id}','{score}')"""
    dt.execute(cmd) 
#เวลาเริ่มทำข้อสอบ
    print("⏰เวลาที่เริ่มต้นทำข้อสอบ คือ %s " % start_time.time())
    print("🚩เวลาที่สิ้นสุดทำข้อสอบ คือ %s " % end.time())
    total_seconds = diff.total_seconds()
    print("\n🧨เวลาที่ใช้ในการทำข้อสอบ คือ %d วินาที" % total_seconds)
    hour = int(total_seconds / 3600)
    min = int(total_seconds % 3600 / 60)
    sec = int(total_seconds % 60)
    print("หรือ %d ชั่วโมง %d นาที %s วินาที 🎊" % (hour, min, sec))
    dt.commit()
    print("-"*45)
    re = input("\n\n⌨️  กดปุ่มใดก็ได้เพื่อดำเนินการต่อ...")
    os.system("cls")
    print("{}{:>90}".format("\n"*5,"❤️  Good luck ❤️"))
    re = input("\n\n\nกด Enter เพื่อเข้าสู่เมนูหลัก...")
    ready()

#ส่วนของการเพิ่มข้อสอบในระบบของครู
def add_more():
    os.system("cls")
    my_introduction()
    choice = ""
    while choice !="ok":
        question = input("\n\t\t\t\t\t\t\t📑 กรอกโจทย์คำถามที่ต้องการเพิ่ม :")
        answer = input("\n\t\t\t\t\t\t\t📕 กรอกคำตอบที่ถูกต้อง :")
        cn.execute(f"INSERT INTO q_and_a (question,answer) VALUES ('{question}','{answer}')")
        ca = input("\n\t\t\t\t\t\t\t\t\t⭕ กรอกตัวเลือก A: ")
        cb = input("\t\t\t\t\t\t\t\t\t⭕ กรอกตัวเลือก B: ")
        cc = input("\t\t\t\t\t\t\t\t\t⭕ กรอกตัวเลือก C: ")
        cd = input("\t\t\t\t\t\t\t\t\t⭕ กรอกตัวเลือก D: ")
        con.execute(F"INSERT INTO choice (Choice1,Choice2,Choice3,Choice4) VALUES ('{ca}','{cb}','{cc}','{cd}')")
        con.commit()
        cn.commit()
        choice = input("\n\t\t\t\t\t\t\t\t💻 กด Enter เพื่อเพิ่ม หรือ พิมพ์ 'ok' เพื่อเสร็จสิ้น :")
    print("\n\t\t\t\t\t\t\t\t\t✅เพิ่มแบบทดสอบเรียบร้อย✅")
    sleep(1.5)
    teacher()

#ส่วนของการโชว์คะแนนในระบบของครู
def show_score():
    os.system("cls")
    my_introduction()
    print("\n\t\t\t\u001b[33;1m 📚คะแนนของนักเรียน📚 \u001b[0m\n".rjust(125))
    print("-"*65)
    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("First name","Last name","Class","ID","Score"))
    print("-"*65)
    for i in dt.execute("SELECT * FROM register"):
        print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4]))
    re = input('กด Enter เพื่อย้อนกลับ')
    teacher()

#ส่วนของเมนูระบบของครู
def teacher():
    while True:
        os.system("cls")
        try:
            my_introduction()
            x = input("\n\t\t\t\t\t\t\t\t\t[1] เพิ่มแบบทดสอบ📖\n\t\t\t\t\t\t\t\t\t[2] แสดงคะแนนของนักเรียน💻\n\t\t\t\t\t\t\t\t\t[3] กลับสู่เมนูหลัก🏠\n\n\t\t\t\t\t\t\t\t\tตัวเลือกของคุณ :")
            if x.strip() == "1":
                add_more()
                break
            elif x.strip() == "2":
                show_score()
                break
            elif x.strip() == "3":
                ready()
                break
            else:
                os.system("cls")
                my_introduction()
                print("โปรดทำรายการให้ถูกต้อง".rjust(102))
                sleep(1.5)
        except ValueError:
            os.system("cls")
            my_introduction()
            print("โปรดทำรายการให้ถูกต้อง".rjust(102))
            sleep(1.5)

#สร้างตัวแปรเก็บ username และ password เก็บข้อมูลของครูเพื่อเข้าสู่ระบบ
def login():
    while True:
        user1 = "Ratchadaphon_jgb"
        password1 = "222078"
        user2 = "Kulthida_jgb"
        password2 ="111991"
        os.system("cls")
        my_introduction()
        get_user = input("\t\t\t\t\t\t\t\t\tUsername :")
        if get_user == user1 or get_user == user2:
            get_pass = input("\t\t\t\t\t\t\t\t\tPassword :")
            if (get_pass == password1 and get_user == user1) or (get_pass == password2 and get_user == user2):
                teacher()
                break
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t⚠️ รหัสผ่านไม่ถูกต้อง")
                sleep(1.5)
        else:
            print("\n\t\t\t\t\t\t\t\t\t\t⚠️ ไม่พบชื่อผู้ใช้")
            sleep(1.5)

#ให้ผู้ใช้เลือกเข้าระบบครูหรือนักเรียน
def ready():
    while True:
        os.system("cls")
        my_introduction()
        lg = input("\n\t\t\t\t\t\t\t\t\t[1] เข้าสู่ระบบของนักเรียน👧 \n\t\t\t\t\t\t\t\t\t[2] เข้าสู่ระบบของคุณครู👩 \n\n\t\t\t\t\t\t\t\tท่านต้องการเข้าสู่ระบบ :")
        if lg.strip() == "1":
            os.system("cls")
            student()
            break
        elif lg.strip() == "2":
            os.system("cls")
            login()
            break
        else:
            os.system("cls")
            my_introduction()
            print("\n\t\t\t\t\t\t\t\t    ⚠️ กรุณากรอกเฉพาะเลข 1 หรือ 2 เท่านั้นเพื่อเข้าสู่ระบบ❗")
            sleep(2.0)
ready()