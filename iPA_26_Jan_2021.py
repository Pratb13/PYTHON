//Program 1
/* For Question to this program, please visit https://kingkrab.net/ipa-26-jan-2021-xplore-answer-python/ */

if __name__ == "__main__":

	t1=[]
	t2=[]
	t3=[]
	l1=[]

	for i in range(3):
		x=input()
		t1.append(x)
		l1.append(x)

	for i in range(3):
		x=input()
		t2.append(x)
		l1.append(x)

	for i in range(3):
		x=input()
		t3.append(x)
		l1.append(x)

	result1=list(set(l1))
	result1.sort()
	
	t1=set(t1)
	t2=set(t2)
	t3=set(t3)
	if(t1 & t2 & t3):
		result2=t1 & t2 & t3

	for i in result1:
		print(i)
	for j in result2:
		print(j)
    
//Program 2
/* For Question to this program, please visit https://kingkrab.net/ipa-26-jan-2021-xplore-answer-python/ */

class GoldInvoice:
	def __init__(self,i,n,q,r,w,p,ps):
		self.item_id=i
		self.item_name=n
		self.item_qty=q
		self.item_rate=r
		self.item_weight=w
		self.item_pwc=p
		self.item_pdis=ps

	def calc_Item_price_exGST(self,gold_invoice_list,item_id_choice):
		for i in gold_invoice_list:
			if(i.item_id==item_id_choice):
				 itemcost = (i.item_qty * i.item_rate * i.item_weight )
				 pw=itemcost*(i.item_pwc/100)
				 pd=itemcost*(i.itempdis/100)
				 res1=itemcost+pw-pd
				 return res1
		

	def calc_Item_price_inGST(self,gold_invoice_list,item_id_choice):
		for i in gold_invoice_list:
			if(i.item_id==item_id_choice):
				 itemcost = (i.item_qty * i.item_rate * i.item_weight )
				 pw=itemcost*(i.item_pwc/100)
				 pd=itemcost*(i.itempdis/100)
				 gst=itemcost*(3/100)
				 res2=itemcost+pw-pd+gst
				 return res2
		

if __name__ == "__main__":
	count=int(input())
	l=[]
	for i in range(count):
		id=int(input())
		name=input()
		qty=float(input())
		rate=float(input())
		weight=float(input())
		pwc=float(input())
		pdis=float(input())
		l.append(GoldInvoice(id,name,qty,rate,weight,pwc,pdis))

	item_id=int(input())

	g=GoldInvoice(0,"",0,0,0,0,0)
	res1=g.calc_Item_price_exGST(l,item_id)
	res2=g.calc_Item_price_inGST(l,item_id)
	
	print ('%.3f'%res1)
	print ('%.2f'%res2)
