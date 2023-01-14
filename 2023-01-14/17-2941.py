word = input()
word = word.replace('c=', '1').replace('c-', '2').replace('dz=', '3').replace('d-', '4').replace('lj', '5').replace('nj', '6').replace('s=', '7').replace('z=', '8')
print(len(str(word)))