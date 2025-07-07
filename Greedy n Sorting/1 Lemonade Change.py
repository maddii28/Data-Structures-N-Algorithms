def lemonadeChange(self, bills: list[int]) -> bool:
        Fives = 0
        Tens = 0 
        Twen = 0
        for i in bills:
            if i /5 == 1:
                Fives += 1
            elif i/5 == 2:
                if Fives >= 1:
                    Fives-= 1
                    Tens += 1
                else:
                    return False
            elif i/5 == 4:
                if Tens >= 1 and Fives >= 1:
                    Fives-=1
                    Tens-=1
                    Twen+=1
                elif Fives >= 3:
                    Fives-=3
                else:
                    return False
        
        return True