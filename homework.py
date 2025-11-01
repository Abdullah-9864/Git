# import numpy as np
# data=[15,16,18,19,22,24,29,30,34]
# print("mean:",np.mean(data))
# print("median",np.median(data))
# print("50th precentile (median)",np.percentile(data,50))
# print("75th percentile (median)",np.percentile(data,25))
# print(np.var(data))
# print(np.std(data))


# print("""this a multiline 
      
      
#       string""")


# def password_check():
#       correct_password="python3"
#       attempts=6
      
#       while attempts >0:
#             password= input("Enter the password: ").strip()
            
#             if password=="":
#                   continue
            
#             if password== correct_password:
#                   print("correct password")
#                   break
#             else:
#                   attempts-=1
#                   print("wrong password entered")
                  
#                   if attempts==0:
#                         print("attempts exceeded")
                        
                  
# password_check() 


# print("span "*3)
# print(4*"span ")

# import numpy as np
# data=[1,2,3,4,5,6,7,8]
# print(np.mean(data))
# print(2-1)
# print(2+1)
# print(2**5)
# print(-7//2)

#string, tuple and list

# a1 = "1, 2, 3"
# print(a1)
# print(type(a1[0]))
# print(a1[0])

# nums=[1,2,3]
# print(nums+[4,5,6])
# print(nums*3)



import numpy as np
signal = np.array([1, 2, 3, 4])
ft = np.fft.fft(signal)
print(ft)

