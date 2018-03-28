################
##实习周题目13##
################
print('请输入主串')
w=input()
print('请输入模式串')
t=input()
Next=[]
Next.append(0)
Next.append(0)
lent=len(t)
lenw=len(w)
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
print('串2在串1中出现了',cnt,'次')