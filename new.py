import streamlit as st
import time

st.title('Math Baby')
co1,co2,co3 = st.columns(3)
c = None
with co1:
    a = st.number_input('Number a')
with co2:
    problem = st.radio('kind of math idk', ('\+','\-','x',':'), horizontal = True)
with co3:
    b = st.number_input('Number b')
if b==0 and problem == ':':
    st.write("you can't divide anything by zero")
else:
  possible_ans = (a+b,a-b,a*b,c)
  pro = ('\+','\-','x',':')
  for n,i in zip(possible_ans,pro):
      if i == problem:
          ans = n
          if n == c:
              ans = a/b
  if st.button('check answer'):
      st.write('the answer is', ans)


