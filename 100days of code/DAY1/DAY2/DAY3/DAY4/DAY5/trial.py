import random

#how to join numbers or characters in a lists
# List of members
opio = ['w', 'e', 'r', 't', 'y', 'u', 'i', 'o']

# Pick 3 random members from the list
random_members = random.sample(opio, 3)

# Print the random members in a single statement
print(random_members)
result =''.join(random_members)
print(result)


print("""EXPENDITURE 															
DAY	DATE	REASON	SPENT	DAILY TOTOL	WEEKLY TOTAL	MONTHLY TOTAL									
WEDNESDAY	01/01/2025 00:00	TRANSPORT	11000												
		SNACKS	5000												
		FOOD 	2000												
WEDNESDAY	01/01/2025	TOTAL	18000	18000											
THURSDAY	02/01/2025	TRANSPORT	12000												
		AIRTIME	1000												
THURSDAY	02/02/2025	TOTAL	13000	13000											
FRIDAY	03/04/2025	TRANSPORT	2000												
		LILIAN	15000												
		charge	1050												
		charge	775												
		lilIAN	1000												
		TRANSPORT	7000												
		AIRTIME	1000												
FRIDAY	03/01/2025	TOTAL	27825	27825											
SATURDAY	04/01/2025	SNACKS	3000												
		DATA	2000												
SATURDAY	04/01/2025	TOTAL	5000	5000											
SUNDAY	05/01/2025	charge	775												
		teacher	7000												
		AIRTIME	1000												
SUNDAY	05/01/2025	TOTAL	8775	8775	72600										
MONDAY	06/01/2025	breakfast	1000												
		AIRTIME	500												
		DATA	1500												
MONDAY	06/01/2025	TOTAL	3000	3000											
TEUSDAY	07/01/2025	intern	1500												
		DATA	5000												
		cazin	10000												
		SNACKS	2000												
TEUSDAY	07/01/2025	TOTAL	18500	18500											
WEDNESDAY	08/01/2024	SNACKS	1000												
		LILIAN	15000												
		charge	500												
		charge	500												
		EARPHONES	5000												
		TRANSPORT	2000												
WEDNESDAY	08/01/2025	TOTAL	24000	24000											
THURSDAY	O9/01/2025	TRANSPORT	2000												
		SNACKS	2000												
		SNACKS	2000												
		AIRTIME	1000												
		WATCH	18000												
		charge	1000												
THURSDAY	09/01/2025	TOTAL	26000	26000											
FRIDAY	10/01/2025	SNACKS	2000												
		DATA SCIENCE COURSE	50000												
		TRANSPORT	2000												
		DATA	2000												
		AIRTIME	1000												
FRIDAY	10/01/2025	TOTAL	57000	57000											
SATURDAY	11/01/2025	LILIAN	14000												
		FOOD 	15000												
		DATA	2000												
SATURDAY 	11/01/2025	TOTAL	31000	31000											
SUNDAY	12/01/2025	charge	750												
		LILIAN	25000												
		bottle	17000												
		snacks	1500												
		TRANSPORT	5000												
		FOOD 	16000												
		data	500												
		AIRTIME	500												
SUNDAY	12/01/2025	TOTAL	66250	66250	225750	""")									
