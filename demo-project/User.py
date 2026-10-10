from analytics import calculate_engagement


result = calculate_engagement(100,50,200)
def authorized_list(user,name):
    users=[
        {"name":"Bilal","password":"Bilal8137"},{"name":"Hamza","password":"Hamza09"}
       
      ]
    if user in users:
        print("Authorized User detected")
        print("Access Granted")
        print("Welcome back,",name)
        print("your reel enagagement rate is ",result)
    else:
       return "access denied!!"
      