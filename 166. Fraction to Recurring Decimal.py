class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ###set a sign variable and make a,b both positive
        ###calculate the integer part and decimal part
        ###put all valid remainder in a stack, when it reappears, its index in stack is the same as its index in string 'digits'
        ###thus it's easy to seperate recurring part from the other
        if numerator==0:return "0"
        a,b=numerator,denominator
        if a*b<0:
            sign="-" 
        else:
            sign=""
        a,b=abs(a),abs(b)
        integer=""
        if a>=b:
            quotient=a//b
            integer+=str(quotient)
            remainder=a%b
            if remainder==0:return sign+integer
        else:
            remainder=a
            integer+='0'
        repeat=set()
        stack=[]
        digits=""
        quotient=0
        while remainder not in repeat:
            while remainder<b:
                repeat.add(remainder)
                stack.append(remainder)                
                remainder=remainder*10
                if remainder<b:digits+='0'

            quotient=remainder/b
            digits+=str(quotient)
            remainder=remainder%b
            if remainder==0:return sign+integer+'.'+digits
        startrepeat=stack.index(remainder)
        return sign+integer+'.'+digits[:startrepeat]+'('+digits[startrepeat:]+')'
        
            
        
        
        