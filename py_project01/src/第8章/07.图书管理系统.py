from abc import ABC, abstractmethod
import json

class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num
        self.__available_num = total_num

    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self):
        self.__available_num += 1

    def get_available_num(self):
        return self.__available_num




class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name
        self.__password = password
        self.__borrowed_books = []

    def borrow_book(self, book: Book):

        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅失败，您的借阅数量已达到最大限制！")
            return False


        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name} 已成功借阅图书 {book.title}")
            return True
        else:
            print(f"借阅失败，图书 {book.title} 已被借完！")
            return False

    def return_book(self, book: Book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name} 已成功归还图书 {book.title}")
        else:
            print(f"归还失败，您没有借阅图书 {book.title}")

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books

    @abstractmethod
    def get_max_books(self) -> int:
        pass

class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3

class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level

    def get_max_books(self) -> int:
        return 6 + self.vip_level


class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.current_member: Member|None = None
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        with open("data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book['编号']] = Book(book['编号'], book['标题'], book['作者'], book['数量'])
            print("加载书籍数据成功！")

    def load_members_data(self):
        with (open("data/members.json", "r", encoding="utf-8") as f):
            members_data = json.load(f)
            for member in members_data:
                if member['卡号'].startswith('N'):
                    self.members[member['卡号']] = NormalMember(member['卡号'], member['姓名'], member['密码'])
                elif member['卡号'].startswith('V'):
                    self.members[member['卡号']] =VIPMember(member['卡号'], member['姓名'], member['密码'], member['会员等级'])
            print("加载会员数据成功！")


    def login(self):
        while True:
            print("\n【登录】")
            member_id = input("请输入会员卡号: ")
            password = input("请输入会员密码: ")

            if member_id not in self.members:
                print("登录失败，会员卡号不存在！")
                continue

            member = self.members[member_id]
            if member.get_password() == password:
                print(f"登录成功, 欢迎您, {member.name}")
                self.current_member = member
                return True
            else:
                print("登录失败，密码错误！")
                continue

    def borrow_book(self):
        for book in self.books.values():
            print(f"编号: {book.book_id}, 标题: {book.title}, 作者: {book.author}, 总数: {book.total_num}, 可用: {book.get_available_num()}")

        book_id = input("请输入要借阅的图书编号: ")
        if book_id not in self.books:
            print("借阅失败，图书编号不存在！")
            return
        self.current_member.borrow_book(self.books[book_id])

    def return_book(self):
        borrowed_books = self.current_member.get_borrowed_books()
        print("【已经借阅的图书列表:】")
        for book in borrowed_books:
            print(f"编号: {book.book_id}, 标题: {book.title}")

        book_id = input("请输入要归还的图书编号: ")
        if book_id not in self.books:
            print("还书失败，图书编号不存在！")
            return
        self.current_member.return_book(self.books[book_id])


    def show_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("【已经借阅的图书列表:】")
            for book in borrowed_books:
                print(f"编号: {book.book_id}, 标题: {book.title}")
        else:
            print("您没有借阅任何图书！")


    def run(self):
        if self.login():
            while True:
                print("\n1. 借阅图书")
                print("2. 归还图书")
                print("3. 查看借阅")
                print("4. 退出系统")

                choice = input("请选择操作(1-4): ")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统, Bye Bye ~")
                        break
                    case _:
                        print("无效的选项，请重新选择！")


if __name__ == '__main__':
    ls = LibrarySystem()
    ls.run()

