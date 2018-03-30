# -*- coding: UTF-8 -*-
import tkinter as tk
def Cnt():
	w=s1.get()
	t=s2.get()
	lenw=len(w)
	lent=len(t)
	Next=[]
	Next.append(0)
	Next.append(0)
	lent=len(t)
	for x in range(lent):
		if x==0:
			continue
		j=Next[x]
		while j!=0 and (t[x]!=t[j]):
			j=Next[j]
		if t[x]==t[j]:
			Next.append(j+1)
		else:
			Next.append(0)
	cnt =0
	j=0
	for x in range(lenw):
		while j!=0 and (w[x]!=t[j]):
			j=Next[j]
		if w[x]==t[j]:
			j=j+1
		if j==lent:
			cnt=cnt+1
			j=Next[j]
	c['text']=str(cnt)+'次！'
ass = tk.Tk()
ass.title('Sequence Count')
ass.geometry('400x400')
l1=tk.Label(ass,text=' 主串 ： ').grid(row=0,sticky='W')
s1=tk.Entry(ass,width=30)
s1.grid(row=0,column=1,sticky='E')
l2=tk.Label(ass,text='模式串： ').grid(row=1,sticky='W')
s2=tk.Entry(ass,width=30)
s2.grid(row=1,column=1,sticky='E')
b=tk.Button(ass,text=' COUNT! ',command=Cnt).grid(row=2,column=1,sticky='E')
c=tk.Label(ass,text='')
c.grid(row=3)
ass.mainloop()
