def get_links(url):

  import requests
  from bs4 import BeautifulSoup

  #website url


  #blank links list
  links = []

  #getting website requests links
  website = requests.get(url)

  #getting website text
  website_text = website.text

  #converting it to beautiful format
  soup = BeautifulSoup(website_text)

  #iterating over text to get all the links
  for link in soup.find_all('a'):
  
    #adding links the list
    links.append(link.get('href'))
  
  for link in links:
    if link != 'None' or link != '#':
      print(link)
    else:
      pass

  print(len(links))
print("\n\t")
print("Google Links")
print("=================================================================")
print("\n\t")
get_links("https://www.google.com")
print("\n\t")
print("LinkedIn Links")
print("=================================================================")
get_links("https://www.linkedin.com")
print("\n\t")
print("Yahoo Links")
print("=================================================================")
get_links("https://www.yahoo.com")
print("\n\t")
print("Digiskills Links")
print("=================================================================")
get_links("https://digiskills.pk/")
print("\n\t")
