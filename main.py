import os
import sys
from class_all import *
from suydientien import *
# biến khởi tạo
person = Person(None, None, None)
validate = Validate()
host = "localhost"
user = "root"
password = "khai172305"
database = "htdttt"
table = "truong"
#################################################
# 1. câu hỏi chào hỏi
def welcome_question():
    print("-->Hệ thống: Chào mừng bạn đến với hệ thống tư vấn tuyển sinh của chúng tôi")

    print("-->Hệ thống: hãy nhập tên")
    person.name = validate.validate_name(input())
    print(f'-->Người dùng: Tên của tôi là, {person.name}')

    print("-->Hệ thống: hãy nhập email")
    person.email = validate.validate_email(input())
    print(f'-->Người dùng: Email của tôi là, {person.email}')

    print("-->Hệ thống: hãy nhập số điện thoại")
    person.phoneNumber = validate.validate_phonenumber(input())
    print(f'-->Người dùng: số điện thoại của tôi là {person.phoneNumber}')

    print(f'-->Hệ thống: Xin chào  {person.name} - {person.email} - {person.phoneNumber} ')

    return person
person = welcome_question()

#################################################
# 2. Một số câu hỏi đầu tiên

list_first_answer=[]
def first_question(list_first_answer, person):
    while (1):
        if (len(list_first_answer) == 0):
            print(
                f'-->Hệ thống: {person.name}  đang có định hướng sẽ học khối ngành nào?')
            print('1. Khối ngành xã hội nhân văn')
            print('2. Khối ngành kỹ thuật công nghệ')
            print('3. Khối ngành kinh tế dịch vụ')
            print('4. Khối ngành giáo dục')
            print('5. Khối ngành y tế dược phẩm')
            print('6. Khối ngành ngoại ngữ')
            print('7. Khối ngành nghệ thuật')
            print('8. Tôi chưa có định hướng')

        print("-------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
        if answer == "1":
            list_first_answer.append("S21")
        elif answer == "2":
            list_first_answer.append("S22")
        elif answer == "3":
            list_first_answer.append("S23")
        elif answer == "4":
            list_first_answer.append("S24")
        elif answer == "5":
            list_first_answer.append("S25")
        elif answer == "6":
            list_first_answer.append("S26")
        elif answer == "7":
            list_first_answer.append("S27")
        elif answer == "8":
            list_first_answer.extend(["S21", "S22", "S23", "S24", "S25", "S26", "S27"])
        if (len(list_first_answer) != 0):
            break
        elif (int(answer) < 1 or int(answer) > 8):
            print('-->Hệ thống: Vui lòng nhập 1 số từ 1 tới 8')
            continue
    return list_first_answer
list_first_answers=first_question(list_first_answer, person)
#############################################################
# 3. Câu hỏi thứ 2
list_second_answer=[]
def second_question(list_second_answer, person):
    while (1):
        if (len(list_second_answer) == 0):
            print(
                f'-->Hệ thống: {person.name}  Ngôi trường mơ ước của bạn là gì?')
            print('1. Học viện công nghệ bưu chính viễn thông (PTIT)')
            print('2. Đại học bách khoa Hà Nội(HUST)')
            print('3. Đại học khoa học xã hội nhân văn(USSH)')
            print('4. Đại học sưu phạm(HNUE)')
            print('5. Đại học Y dược Hà Nội(HUP)')
            print('6. Trường Đại học Mỹ thuật Việt Nam(VAU)')
            print('7. Tôi chưa có định hướng rõ ràng')
        print("-------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
        if answer == "1":
            list_second_answer.append("S29")
        elif answer == "2":
            list_second_answer.append("S30")
        elif answer == "3":
            list_second_answer.append("S31")
        elif answer == "4":
            list_second_answer.append("S32")
        elif answer == "5":
            list_second_answer.append("S33")
        elif answer == "6":
            list_second_answer.append("S34")
        elif answer == "7":
            list_second_answer.extend(["S29", "S30", "S31", "S32", "S33", "S34"])
        if (len(list_second_answer) != 0):
            break
        elif (int(answer) < 1 or int(answer) > 8):
            print('-->Hệ thống: Vui lòng nhập 1 số từ 1 tới 7')
            continue

    if  (len(list_second_answer) !=6) :
        while (1):
            print(
                f'-->Hệ thống: {person.name}   Ngoài ra bạn còn thích trường nào không?')
            print('1. Học viện công nghệ bưu chính viễn thông (PTIT)')
            print('2. Đại học bách khoa Hà Nội(HUST)')
            print('3. Đại học khoa học xã hội nhân văn(USSH)')
            print('4. Đại học sưu phạm(HNUE)')
            print('5. Đại học Y dược Hà Nội(HUP)')
            print('6. Trường Đại học Mỹ thuật Việt Nam(VAU)')
            print('7. Không')
            print("-------------Câu trả lời của bạn--------------")
            answer = validate.validate_input_number_form(input())
            print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
            if answer == "1":
                list_second_answer.append("S29")
            elif answer == "2":
                list_second_answer.append("S30")
            elif answer == "3":
                list_second_answer.append("S31")
            elif answer == "4":
                list_second_answer.append("S32")
            elif answer == "5":
                list_second_answer.append("S33")
            elif answer == "6":
                list_second_answer.append("S34")
            elif answer == "7":
                break
            elif (int(answer) < 1 or int(answer) > 7):
                print('-->Hệ thống: Vui lòng nhập 1 số từ 1 tới 7')
                continue
    return list_second_answer
list_second_answers=second_question(list_second_answer, person)
listbocauhoidau=[]
listbocauhoidau.extend(list_first_answer)
listbocauhoidau.extend(list_second_answer)
inferred_facts = forward_inference(rule1, listbocauhoidau)
print("Hệ thống: theo những gì hệ thống ghi nhận thì định hướng của bạn sẽ phù hợp với các trường sau:")
print(inferred_facts)
result = query_tenNganhTruong_from_table(host, user, password, database, table, inferred_facts)
for item in result:
    processed_item = item[0].replace("(", "").replace(")", "").replace("'", "").replace("\n", "")
    print(processed_item)
print("-------------Bạn xem file để biết thêm thông tin chi tiết của trường--------------")
result2 = query_data_from_table(host, user, password, database, table, inferred_facts)
with open('cac_truong_phu_hop.txt', 'w', encoding='utf-8') as file:
    for item in result2:
        processed_item = item[0].replace("(", "").replace(")", "").replace("'", "").replace("\n", "")
        file.write(processed_item + '\n')
        processed_item1 = item[1].replace("(", "").replace(")", "").replace("'", "").replace("\n", "")
        file.write(processed_item1 + '\n')
        processed_item2 = item[2].replace("(", "").replace(")", "").replace("'", "").replace("\n", "")
        file.write(processed_item2 + '\n')
#############################################################
#Bộ câu hỏi cho phần sau
# 4. Câu hỏi thứ 1
cauhoithu1=[]
def listcauhoithu1(cauhoithu1, person):
    while (1):
        if (len(cauhoithu1) == 0):
            print('Hệ thống: Sau đây hệ thống sẽ phán đoán các trường đại học bạn có thể đỗ')
            print(
                f'-->Hệ thống: {person.name}   sẽ xét tuyển theo những hình thức nào?')
            print('1. xét tuyển dựa trên kết quả học tập')
            print('2. xét tuyển dựa trên kết quả kì thi đầu vào')
            print('3. xét tuyển dựa vào bài thi năng khiếu')
            print('4. xét tuyển dựa vào kết quả kì thi riêng')
            print('5. xét tuyển dựa vào các chứng chỉ ngoại ngữ quốc tế')
            print('6. Tôi chưa có định hướng')
        print("-------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
        if answer == "1":
            cauhoithu1.append("S16")
        elif answer == "2":
            cauhoithu1.append("S17")
        elif answer == "3":
            cauhoithu1.append("S18")
        elif answer == "4":
            cauhoithu1.append("S19")
        elif answer == "5":
            cauhoithu1.append("S20")
        elif answer == "6":
            cauhoithu1.extend(["S16", "S17", "S18", "S19", "S20"])
        if (len(cauhoithu1) != 0):
            break
        elif (int(answer) < 1 or int(answer) > 6):
            print('-->Hệ thống: Vui lòng nhập 1 số từ 1 tới 6')
            continue
    if (len(cauhoithu1) != 5):
        while(1):
            print(f'-->Hệ thống: {person.name}   sẽ xét tuyển theo những hình thức nào nữa không ?')
            print('1. xét tuyển dựa trên kết quả học tập')
            print('2. xét tuyển dựa trên kết quả kì thi đầu vào')
            print('3. xét tuyển dựa vào bài thi năng khiếu')
            print('4. xét tuyển dựa vào kết quả kì thi riêng')
            print('5. xét tuyển dựa vào các chứng chỉ ngoại ngữ quốc tế')
            print('6. Không')
            print("-------------Câu trả lời của bạn--------------")
            answer = validate.validate_input_number_form(input())
            print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
            if answer == "1":
                cauhoithu1.append("S16")
            elif answer == "2":
                cauhoithu1.append("S17")
            elif answer == "3":
                cauhoithu1.append("S18")
            elif answer == "4":
                cauhoithu1.append("S19")
            elif answer == "5":
                cauhoithu1.append("S20")
            elif answer == "6":
                break
            elif (int(answer) < 1 or int(answer) > 6):
                print('-->Hệ thống: Vui lòng nhập 1 số từ 1 tới 6')
                continue
    return cauhoithu1
listcauhoithu1s=listcauhoithu1(cauhoithu1,person)
#############################################################
# 5. Câu hỏi thứ 2
cauhoithu2=[]
def listcauhoithu2(cauhoithu2, person):
    while (1):
        if (len(cauhoithu2) == 0):
            print(
                f'-->Hệ thống: {person.name} Khối môn bạn đang học ở trường THPT là gì?')
            print('1. A00')
            print('2. A01')
            print('3. B00')
            print('4. C00')
            print('5. D01')
            print('6. D04')
            print('7. D07')


        print("-------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
        if answer == "1":
            cauhoithu2.append("S9")
        elif answer == "2":
            cauhoithu2.append("S10")
        elif answer == "3":
            cauhoithu2.append("S11")
        elif answer == "4":
            cauhoithu2.append("S12")
        elif answer == "5":
            cauhoithu2.append("S13")
        elif answer == "6":
            cauhoithu2.append("S14")
        elif answer == "7":
            cauhoithu2.append("S15")
        if (len(cauhoithu2) != 0):
            break
        elif (int(answer) < 1 or int(answer) > 7):
            print('-->Hệ thống: Vui lòng nhập 1 số từ 1 tới 7')
            continue
    return cauhoithu2
listcauhoithu2s=listcauhoithu2(cauhoithu2,person)
#############################################################
# 5. Câu hỏi thứ 3
cauhoithu3=[]
def listcauhoithu3(cauhoithu3, person):
    while (1):
        if (len(cauhoithu3) == 0):
            print(
                f'-->Hệ thống: {person.name} Điểm thi thử của bạn trong khoảng nào?')
            print('1. Điểm xấp xỉ 23')
            print('2. Điểm xấp xỉ 24')
            print('3. Điểm xấp xỉ 25')
            print('4. Điểm xấp xỉ 26')
            print('5. Điểm xấp xỉ 27')
            print('6. Điểm xấp xỉ 28')
            print('7. Điểm xấp xỉ 29')
            print('8. Điểm xấp xỉ 30')

        print("-------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
        if answer == "1":
            cauhoithu3.append("S1")
        elif answer == "2":
            cauhoithu3.append("S2")
        elif answer == "3":
            cauhoithu3.append("S3")
        elif answer == "4":
            cauhoithu3.append("S4")
        elif answer == "5":
            cauhoithu3.append("S5")
        elif answer == "6":
            cauhoithu3.append("S6")
        elif answer == "7":
            cauhoithu3.append("S7")
        elif answer == "8":
            cauhoithu3.append("S8")
        if (len(cauhoithu3) != 0):
            break
        elif (int(answer) < 1 or int(answer) > 8):
            print('-->Hệ thống: Vui lòng nhập 1 số từ 1 tới 8')
            continue
    return cauhoithu3
listcauhoithu3s=listcauhoithu3(cauhoithu3,person)
listbocauhoi2=[]
listbocauhoi2.extend(list_first_answer)
listbocauhoi2.extend(cauhoithu1)
listbocauhoi2.extend(cauhoithu2)
listbocauhoi2.extend(cauhoithu3)
#print(listbocauhoi2)
inferred_facts2 = forward_inference(rule2, listbocauhoi2)
new_set = set()
for item in inferred_facts2:
    if 'D' in item:
        new_set.add(item)
print("Hệ thống: Theo điều kiện hiện tại của bạn hệ thống đã lọc ra các ngành ở các trường mà bạn có khả năng đỗ:")
print(new_set)
result2 = query_tenNganhTruong_from_table(host, user, password, database, table, new_set)
for item in result2:
    processed_item = item[0].replace("(", "").replace(")", "").replace("'", "").replace("\n", "")
    print(processed_item)
print("-------------Bạn xem file để biết thêm thông tin chi tiết của trường--------------")
result3 = query_data_from_table(host, user, password, database, table, new_set)
with open('cac_truong_kha_nang_do.txt', 'w', encoding='utf-8') as file:
    for item in result3:
        processed_item = item[0].replace("(", "").replace(")", "").replace("'", "").replace("\n", "")
        file.write(processed_item + '\n')
        processed_item1 = item[1].replace("(", "").replace(")", "").replace("'", "").replace("\n", "")
        file.write(processed_item1 + '\n')
        processed_item2 = item[2].replace("(", "").replace(")", "").replace("'", "").replace("\n", "")
        file.write(processed_item2 + '\n')