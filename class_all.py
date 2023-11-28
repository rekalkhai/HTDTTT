import re
import mysql.connector
class Validate:
    def __init__(self) -> None:
        pass

    def validate_input_number_form(self,value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))
            check = valueGetRidOfSpace.isnumeric()
            if (check):
                return valueGetRidOfSpace
            else:
                print("-->Chatbot: Vui lòng nhập 1 số dương")
                value = input()

    def validate_phonenumber(self,value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))
            check = valueGetRidOfSpace.isnumeric()
            if (check):
                return valueGetRidOfSpace
            else:
                print("-->Chatbot: Vui lòng nhập 1 số điện thoại đúng định dạng")
                value = input()


    def validate_email(self, email):
        while (1):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            if (re.fullmatch(regex, email)):
                # print("Chatbot:Tôi đã nhận được thông tin Email của bạn")
                return email

            else:
                print("-->Chatbot: Vui lòng nhập lại email")
                email = input()

    def validate_name(self, value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))

            check = valueGetRidOfSpace.isalpha()
            if (check):
                # print("Tôi đã nhận được thông tin Tên của bạn")
                return value
            else:
                print("-->Chatbot: Vui lòng nhập lại tên ! ")
                value = input()

class Person:
    def __init__(self, name, phoneNumber, email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phoneNumber} - {self.email}"
def query_tenNganhTruong_from_table(host, user, password, database, table, id_set):
    # Thiết lập kết nối với cơ sở dữ liệu MySQL
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    mycursor = mydb.cursor()
    id_list = ",".join(["'" + id + "'" for id in id_set])
    sql_query = "SELECT tenNganhTruong FROM {} WHERE idnganh IN ({})".format(table, id_list)
    mycursor.execute(sql_query)
    result = mycursor.fetchall()
    mydb.close()
    return result
def query_data_from_table(host, user, password, database, table, id_set):
    # Thiết lập kết nối với cơ sở dữ liệu MySQL
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    mycursor = mydb.cursor()
    id_list = ",".join(["'" + id + "'" for id in id_set])
    sql_query = "SELECT tenNganhTruong,hinhThucTuyenSinh,thongTinThem FROM {} WHERE idnganh IN ({})".format(table, id_list)
    mycursor.execute(sql_query)
    result = mycursor.fetchall()
    mydb.close()
    return result