class MinhaString(str):
    def upper(self):
        print('Chamou upper')
        return super().upper()
    
string = MinhaString('André')
print(string.upper())