
# Online Python - IDE, Editor, Compiler, Interpreter

print('Marks in 5 subject:97,90,100,95,98')

def calculatesum(a,b,c,d,e):
  C=a+b+c+d+e
  return C

print(f'Total marks:{calculatesum(97,90,100,95,98)}')

                                 
def calculatepercentage(a,b,c,d,e):
    P=(a+b+c+d+e)/500*100
    return P
    
print(f'Percentage:{calculatepercentage(97,90,100,95,98)}%')


(Percentage)=96
if(Percentage<40):
    print('Final Result:fail')
else:
     print('Final Result:Pass')