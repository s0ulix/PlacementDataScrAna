import pandas as pd
df=pd.read_csv('placement3.csv')
cmp=[]
gen=[]
deg=[]
ele=[]
stp=[]
ctcmin=[]
ctcmax=[]
loc=[]
#minctc=int(input("Enter min ctc req: "))
minctc=int(input("Enter min stipend req: "))
for ind,r in df.iterrows():
    if(type(r['CTC'])!=float):
        maxt=0
        mint=0
        st=0
        temp=[i for i in (r['CTC']).split()]
        for i in range(len(temp)):
            if(temp[i]=='LPA'):
                try:
                    #print(float(temp[i-1]))
                    if(maxt>float(temp[i-1])):
                        try:
                            mint=float(temp[i-1])
                        except:
                            mint=float(temp[i-1][3:])
                    else:
                        try:
                            mint = maxt
                            maxt=float(temp[i-1])

                        except:
                            mint = maxt
                            maxt = float(temp[i - 1][3:])

                except:
                    #print(float(temp[i-1][3:]))
                    if (maxt > float(temp[i - 1][3:])):
                        try:
                            mint = float(temp[i - 1])
                        except:
                            mint = float(temp[i - 1][3:])
                    else:
                        try:
                            mint = maxt
                            maxt = float(temp[i - 1])

                        except:
                            maxt = float(temp[i - 1][3:])
                            mint = maxt
            if(temp[i]=='Stipend'):
                try:
                    st=int(temp[i+2])
                except:
                    try:
                        st=int(temp[i+1][3:])
                    except:
                        #print(temp)
                        pass
        #print(maxt)
        if(st>=minctc):
            ctcmin.append(mint)
            ctcmax.append(maxt)
            stp.append(st)
            cmp.append(r['Company'])
            gen.append(r['Gender'])
            loc.append((r['Location']))
            ele.append(r['Eligibility'])
            deg.append(r['Designation'])

df=pd.DataFrame(list(zip(cmp,deg,ele,ctcmin,ctcmax,stp,gen )),columns =['Company', 'Designation','Eligibility','MIN CTC','MAX CTC','Stipend','Gender'])
df1=df.sort_values("MAX CTC",ascending=False)
df1.to_csv("ctc_"+str(minctc)+".csv")
