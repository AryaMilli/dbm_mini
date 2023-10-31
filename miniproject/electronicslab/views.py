from django.shortcuts import render
import mysql.connector as sql
en=''
rn=''
cost=''
al=''
# Create your views here.
def electronic_inventory(request):
  global en,rn,cost,al
  if request.method=='POST':
    n=sql.connect(host="localhost",user="root", passwd="ari28", database='miniproject')
    cursor=n.cursor()
    d=request.POST
    for key,value in d.items():
      if key=="equipment_name":
        en=value
      if key=="registration_number":
       rn=value
      if key=="cost_of_purchase":
       cost=value
      if key=="user_permission":
        al=value
      c="insert into inventory values('{}','{}','{}','{}','{}')".format(en,rn,cost,al)
      cursor.execute(c)
      n.commit() 

  return render(request,'electronicslab.html')
