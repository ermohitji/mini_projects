# with the help of this program you can encode your message.
# this program shift all the alphabets with a specific number according to their sequence in letters
# and this will decode by the same program by shifting the encoded message by negative of that shifted number.
word = input("Write the code: ").lower()
shift = int(input("How much shift: "))
list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
code = ""
for i in word:
    index = list.index(i)+shift
    code+= list[index]
print(code)

