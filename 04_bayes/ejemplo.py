# http://www.greenteapress.com/thinkbayes/thinkbayes.pdf
# http://thinkbayes.com/thinkbayes.py
# python -m pip install scipy numpy matplotlib pandas


from thinkbayes2 import Pmf

pmf = Pmf()

pmf.Set('tazon1', 0.5)
pmf.Set('tazon2', 0.5)

pmf.Mult('tazon1', 0.75)
pmf.Mult('tazon2', 0.5)

pmf.Normalize()

print(pmf.Prob('tazon1'))
