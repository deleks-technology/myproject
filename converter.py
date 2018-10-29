print ("Currency Converter")
print ("You are Welcome")
print("========================================================")

#Guide User to input intended conversion
print("For NGN to USD input '1', For USD to NGN input '2', For NGN to PNDS input '3', For PNDS to Naira input '4'")
#Prompt User to Input Intended Conversion
user_input = input("Please input figure corresponding to your intended conversion:")
if user_input == '1':    
      print ("You intend to convert NGN to USD")
      #Prompt User to input values for NGN and USD
      NGN = int (input ("Please input your currency value in Nigeria Naira:"))
      # 1 NGN = 305.85 USD
      NGN_2_USD = NGN / 305.85
      print ("Your currency value equivalent in today's market is (USD): ", NGN_2_USD)
      print ("=================================================================")
      print ("Thank You for choosing Our Currency Converter.....Have a Nice Day")
elif user_input == '2':
      print ("You intend to convert USD to NGN")
      #Prompt Usern to input values for NGN and USD
      USD = int(input ("Please input your currency value in US Dollars:"))
      # 1 NGN = 305.85 USD
      USD_2_NGN = USD * 305.85
      print ("Your currency value equivalent in today's market is (NGN): ", USD_2_NGN)
      print ("=================================================================")
      print ("Thank You for choosing Our Currency Converter.....Have a Nice Day")
elif user_input == '3':
      print ("You intend to convert NGN to PNDS")
      # 1 NGN = 403.2326 PNDS
      NGN = int(input ("Please input your currency value in Nigeria Naira:"))
      NGN_2_PNDS = NGN * 403.2326
      print ("Your currency value equivalent in today's market is (NGN): ", NGN_2_PNDS)
      print ("=================================================================")
      print ("Thank You for choosing Our Currency Converter.....Have a Nice Day")

elif user_input == '4':
      print ("You intend to convert PNDS to NGN")
      # 1 NGN = 403.2326 PNDS
      PNDS = int(input ("Please input your currency value in Nigeria Naira:"))
      PNDS_2_NGN = PNDS / 403.2326
      print ("Your currency value equivalent in today's market is (NGN): ", PNDS_2_NGN)
      print ("=================================================================")
      print ("Thank You for choosing Our Currency Converter.....Have a Nice Day")                
