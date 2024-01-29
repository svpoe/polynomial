# References: Used chatGBT 3.5 to find way to refresh python syntax with self (used to Java) e.g.: self.p2.evaluate(X)
# add and commit this file with the following message "cs 506 exercise part a". Push these changes to github.
class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self,X):
        return X

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self,X):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, X):
        return self.p1.evaluate(X) + self.p2.evaluate(X)
    
#Adding class sub
class Sub: 
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, X):
        return self.p1.evaluate(X) - self.p2.evaluate(X)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        #if isinstance(self.p1, Add):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            # if isinstance(self.p2, Add):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        # if isinstance(self.p2, Add):
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self,X):
        return self.p1.evaluate(X) * self.p2.evaluate(X)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        #if isinstance(self.p1, Add):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            # if isinstance(self.p2, Add):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        # if isinstance(self.p2, Add):
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    
    def evaluate(self, X):
        return self.p1.evaluate(X) / self.p2.evaluate(X)

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

poly = Add( Add( Int(4), Int(3)), Add( X(), Div( Int(1), Add( Div(X(), X()), Int(1)))))
print(poly)

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))