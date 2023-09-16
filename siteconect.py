# import urllib
# use urllib request to get the data from he url
# write a function that takes a url
# returns response

import urllib.request as urllib

def main(url):
  print("checking connectivity")

  response = urllib.urlopen(url)
  print("connected to", url, "succesfully")
  print("the response code was: ", response.getcode())

print("this is site connectivity checker program")
input_url = input("input the url of the site you want to check: ")

main(input_url)