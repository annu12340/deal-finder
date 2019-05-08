from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup
from csv import writer

#inputing the prdt name
s1=s2=s3=s4=s5=0


def flipkart() :
    print("******************************************Price in Flipkart *********************************************\n\n")
    #searching
    d="+".join(l)
    

#searching
    my_url = "https://www.flipkart.com/search?q="+d+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    print(my_url)

#calling the fn
    uClient = uReq(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    name= page_soup.findAll("a", {"class": "_2cLu-l"})      
    price= page_soup.findAll("div", {"class": "_1vC4OE"})
    rating= page_soup.findAll("div", {"class": "hGSR34"})

    if not name:
      name= page_soup.findAll("a", {"class": "_31qSD5"})
      price= page_soup.findAll("a", {"class": "_1vC4OE _2rQ-NK"})
#feature= page_soup.findAll("div", {"class": "_1rcHFq"})
    try:
     for i in range(0,4):
      print(name[i].text),
      print(price[i].text),
      print("Rating : ", rating[i].text)
    # print("Feature : ", feature[i].text)
      print("\n_________________\n")
    except:
      print("Sorry. An error occuured ")
        


def ebay():
    print("*********************************************Price in Ebay *********************************************\n\n")
    #searching
    d="+".join(l)
    
    my_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw="+d+"&_sacat=0&LH_TitleDesc=0&_sop=12"
    print(my_url)
#calling the fn
    uClient = uReq(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    namee= page_soup.findAll("h3", {"class": "s-item__title"})
    pricee= page_soup.findAll("span", {"class": "s-item__price"})
#feature= page_soup.findAll("div", {"class": "_1rcHFq"})
    try:
     for i in range(0,3):
      print(namee[i].text),
      print(pricee[i].text)
      print("Rating : ", rating[i].text)
    # print("Feature : ", feature[i].text)
      print("\n_________________")
    except:
        print("Sorry. An error occuured ")      


def patymmall():
    print("*********************************************Price in patymmall *********************************************\n\n")
    #searching
    d="%20".join(l)
    
    my_url = "https://paytmmall.com/shop/search?q="+d+"&from=organic&child_site_id=6&site_id=2"
    

#calling the fn
    uClient = uReq(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    pricep= page_soup.findAll("div", {"class": "_1kMS"})
    namep= page_soup.findAll("div", {"class": "_2apC"})
#feature= page_soup.findAll("div", {"class": "_1rcHFq"})
    try:
     for i in range(0,3):
      print(namep[i].text),
      print(pricep[i].text),
      #print("Rating : ", ratingp[i].text)
    # print("Feature : ", feature[i].text)
      print("\n_________________")
    except:
        print("Sorry. An error occuured ")
        

def snapdeal():
    print("*********************************************Price in Snapdeals *********************************************\n\n")
    #searching
    d="+".join(l)
    
    my_url = "https://www.snapdeal.com/search?keyword="+d+"&santizedKeyword=lady+bird+cycle&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=ALL&url=&utmContent=&dealDetail=&sort=rlvncy"
    print(my_url)

#calling the fn
    uClient = uReq(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    namea= page_soup.findAll("div", {"class": "bg-image hidden"})
    pricea= page_soup.findAll("span", {"class": "lfloat product-desc-price strike"})
#feature= page_soup.findAll("div", {"class": "_1rcHFq"})
    try:
     for i in range(0,3):
      print(namea[i].text),
      print(pricea[i].text),
      #print("Rating : ", ratingp[i].text)
    # print("Feature : ", feature[i].text)
      print("_________________\n")
    except:
        print("Sorry. An error occuured ")



def shop():
    print("*********************************************Price in Shop clueless *********************************************\n\n")
    #searching
    d="%20".join(l)
    
    my_url = "https://www.shopclues.com/search?q="+d+"&sc_z=4444&z=1&count=10"
    print(my_url)
#calling the fn
    uClient = uReq(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    names= page_soup.findAll("h2")
    prices= page_soup.findAll("span", {"class": "p_price"})
#feature= page_soup.findAll("div", {"class": "_1rcHFq"})
    try:
     for i in range(0,3):
      print(names[i].text),
      print(prices[i].text),
      print("\n_________________")
    except:
        print("Sorry. An error occuured ")
        








a=input("Enter product name  -  ")
l=a.split(" ")

flipkart()
print("\n\n")
print(s1)
ebay()
print("\n\n")
print(s2)
patymmall()
print("\n\n")

shop()
print("\n\n")

snapdeal()
print("\n\n")

small=min(s1,s2,s3,s4,s5)
print(small," is small")
print("**************___completed____********************")
input()
