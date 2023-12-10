# Accept any city from the user and display monument of that city.
#                 City                                 Monument
#                 Delhi                               Red Fort
#                 Agra                                Taj Mahal
#                 Jaipur                              Jal Mahal

a=input("Enter city name")
b=a.lower()
if b=="delhi":
    print("Red Fort")
elif b=="aagra":
    print("Taj Mahal")
elif b=="Jaipur":
    print("Jal Mahal")
else:
    print("City is not in the data")