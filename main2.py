
class firstClass:
    val1 = 0
    val2 = 0

    def __init__(self, a, b):
        print(' this is constructor')
        self.val1 = a
        self.val1 = b


    def addValue(self):
        print(f'addition = {self.val1 + self.val2}')



f1 = firstClass(6,7)

f1.addValue()

print('f1.val1 =', f1.val1)
print(f'f1.val2 = {f1.val2}')

f2 = firstClass(30,40)
f2.addValue()

