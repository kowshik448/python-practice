def stock_span(price,n):
    span=[]
    span.append(1)
    st=[]
    st.append(0)
    for i in range(1,n):
        next=price[i]
        while len(st)>0 and price[st[-1]]<=next:
            st.pop()
        if len(st)==0:
            span.append(i+1)
        else:
            span.append(i-st[-1])
        st.append(i)
    print(span)
price=list(map(int,input().split()))
n = len(price)
stock_span(price,n)
   

         
