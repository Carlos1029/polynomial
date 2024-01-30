class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)



class Div:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        #Check if left argument is add or sub type
         if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
             #if so check right argument type 
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            #return if only left is add or sub type\
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
         if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
             return repr(self.p1) + " / ( " + repr(self.p2) + " )"
         return repr(self.p1) + " / " + repr(self.p2)
                 

class Sub: 
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)


 



# simple mul case with no add types
simp_mul = Mul(2,2)
print(simp_mul)

#left is add type (2+2) * 2
mul_addleft = Mul( Add(Int(2),Int(2)), 2) 
print( mul_addleft)

#Right is add type in Mul
mul_addright = Mul(2 , Add(Int(2),Int(2))) 
print( mul_addright)

#Both left and right are add types in Mul
mul_addboth = Mul( Add(Int(2),Int(2)) , Add(Int(2),Int(2))) 
print( mul_addboth)

#Simple Div with no add types
simp_Div = Div(2,2)
print(simp_Div)

#left is add type (2+2) * 2
Div_addleft = Div( Add(Int(2),Int(2)), 2) 
print( Div_addleft)

#Right is add type
Div_addright = Div(2 , Add(Int(2),Int(2))) 
print( Div_addright)

#Both left and right are add types in Mul
Div_addboth = Div( Add(Int(2),Int(2)) , Add(Int(2),Int(2))) 
print( Div_addboth)

#Simple sub
sub_simple = Sub(Int(2),Int(1))
print (sub_simple)

#Div with sub
div_sub = Div(1, Sub(3,3))
print (div_sub)

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))

poly_w_sub = Add( Sub( Int(4), Int(3)), Add( X(), Mul( Int(1), Sub( Mul(X(), X()), Int(1)))))

print(poly, '\n', poly_w_sub)

