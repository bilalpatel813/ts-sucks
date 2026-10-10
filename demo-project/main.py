from User  import authorized_list


name= input("Enter ur name: ")
password = input("Enter ur password: ")
user={"name":name,"password":password}
print(authorized_list(user,name))
    
     
     