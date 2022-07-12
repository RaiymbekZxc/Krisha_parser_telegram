
import bs4, requests
class AdKrisha:
    def __intcheck(self, num):
        try:
            int(num)
        except ValueError:
            return False
        return True


    def __make_price(self, soup):
        pr = str(soup.find(class_='offer__price'))
        price = ''
        for i in pr.split():
            if self.__intcheck(i):
                price += i
        return int(price)
    def get_price(self):
        return self.__price


    def __make_advert(self, soup):
        advert = str(soup.find('h1'))
        advert = advert.split("\n")
        return advert[1].strip()
    def get_advert(self):
        return self.__advert


    def __make_district(self, soup):
        try:
            district = str(soup.find(class_="offer__location offer__advert-short-info")).split('span>')
            district = district[1].split()
            return district[1]
        except Exception:
            return "None"
    def get_district(self):
        return self.__district


    def get_rooms(self):
        return self.__rooms
    
    def __make_squares(self, ad):
        ad_info = ad.split(",")
        squares = ''
        for i in ad_info[1]:
            if self.__intcheck(i) or i == ',' or i == '.':
                squares += i
        return squares
    def get_squares(self):
        return float(self.__squares)
    

    def __make_house_type(self, soup):
        temp = ''
        try:
            for i in soup.find_all('div', {'data-name':'flat.building'}):
                temp += i.text
            temp = temp.strip().split("\n")
            return temp[2]
        except Exception:
            return "None"
    def get_house_type(self):
        return self.__house_type


    def __make_floor_info(self, soup):
        try:
            temp = ''
            for i in soup.find_all('div', {'data-name':'flat.floor'}):
                temp = i.text
            temp = temp.strip().split("\n")
            return str(temp[2])
        except Exception:
            return 'None'
    def get_floor_info(self):
        return self.__floor_info


    def __make_floor(self):
        try:
            temp = self.__floor_info.split()
            return int(temp[0]) 
        except Exception:
            return -1
    def get_floor(self):
        return self.__floor
    

    def __make_of_floor(self):
        try:
            temp = self.__floor_info.split()
            return int(temp[2])
        except Exception:
            return -1
    def get_of_floor(self):
        return self.__of_floor


    def __make_year_built(self, soup):
        try:
            temp = ''
            for i in soup.find_all('div', {'data-name':'house.year'}):
                temp += i.text
            temp = temp.strip().split("\n")
            return int(temp[2])
        except Exception:
            return -1
    def get_year_built(self):
        return self.__year_built


    def __init__(self, soup):
        self.__price = self.__make_price(soup)
        self.__advert = self.__make_advert(soup)
        self.__rooms = int(self.__advert[0])
        self.__district = self.__make_district(soup)
        self.__squares = self.__make_squares(self.__advert)
        self.__house_type = self.__make_house_type(soup)
        self.__floor_info = self.__make_floor_info(soup)
        self.__floor = self.__make_floor()
        self.__of_floor = self.__make_of_floor()
        self.__year_built = self.__make_year_built(soup)
    
    def __str__(self):
        return self.__advert