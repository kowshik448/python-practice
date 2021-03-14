# w=len(bin(n).replace(''))
def print_formatted(number):
    for i in range(1,n+1):
        print(str(i).rjust(w+1,' ')+ oct(i).replace('0o','').rjust(w+1,' ')+ hex(i).replace('0x','').upper().rjust(w+1,' ') + bin(i).replace('0b','').rjust(w+1,' '))

n = int(input())
w=len(bin(n).replace('0b',''))
print_formatted(n)

