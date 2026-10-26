# 12. ID Preservation: `"00125"` ko string aur integer ke roop mein 
# store karo. Explain karo ki ID ke liye string kab better hai.
# Ans. ID ke liye string kab better hai?
# Jab value sirf kisi person, product, employee ya account ko identify 
# karti hai aur us par mathematical calculations nahi karni hoti.
# Examples:
# - Employee ID: "00125"
# - PIN code: "262309"
# - Product code: "000847"
# - Phone number: "09876543210"
# In values ko string mein rakhna useful hai, kyunki leading zeros 
# preserve hote hain aur +, - jaise characters bhi store kiye ja sakte 
# hain.
# Data Analytics mein important: Customer ID, product ID aur order ID 
# ko generally text/string ke roop mein treat karna chahiye, chahe unmein
# sirf digits hon.
id_string = "00125"
id_integer = int("00125")
print("String ID : ",id_string)
print("String ID type : ",type(id_string))
print("Integer ID : ",id_integer)
print("Integer ID type : ",type(id_integer))