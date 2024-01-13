# print("  *  ")
# print(" *** ")
# print("*****")


# Main Program


n = int(input("Enter Number Of Lines: \n\t"))
for i in range(n):
    print(" " * (n-i-1), end = "")
    print("*" * (2*i+1), end = "")
    print(" " * (n-i-1))



# Extra


# for i in range(n):
#     print("*" * (n-i-1), end = "")
#     print(" " * (2*i+1), end = "")
#     print("*" * (n-i-1))
#     for i in range(n):
#         print(" " * (n-i-1), end = "")
#         print("*" * (2*i+1), end = "")
#         print(" " * (n-i-1))
#     for i in range(n):
#         print("*" * (n-i-1), end = "")
#         print(" " * (2*i+1), end = "")
#         print("*" * (n-i-1))
