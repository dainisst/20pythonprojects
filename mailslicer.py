# collect email from user
# split email into three parts

def main():
  print("welcome to email slicer")

  email_input = input("input your email: ")

  (username, domain) = email_input.split("@")
  (domain, extension) = domain.split(".")

  print(f"Username: {username}")
  print(f"Domain: {domain}")
  print(f"Extension: {extension}")

main()