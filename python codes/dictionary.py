phn_number=input('phone: ')
info={
'1':'one',
'2':'two',
'3':'three',
'4':'four'
}
output =""
for number in phn_number:
    output+=info.get(number,'!')+" "
print(output)