#write a python program which will insert employee number, ename,salary and company name as a record in employee table of oracle database
#emp1.py---file name and acts as module name
import cx_Oracle # step-1
def   empinsert():
	try:
		while(True):
			try:
				con=cx_Oracle.connect("scott/tiger@localhost/orcl") #step-2
				cur=con.cursor()  # step-3
				#accept employee data
				empno=int(input("Enter Employee Number:"))
				ename=input("Enter Employee Name:")
				sal=float(input("Enter Employee Salary:"))
				cname=input("Enter Employee Company Name:")
				#design the query and execute
				cur.execute("insert into employee values(%d,'%s',%f,'%s' ) " %(empno,ename,sal,cname) )
				con.commit()
				print("{} Employee Record Inserted :".format(cur.rowcount))
				print("-"*50)
				ch=input("Do u want to another Record(yes/no):")
				if(ch.lower()=="no"):
					print("Thanks for using this program")
					break
			except ValueError:
				print("\nDon't enter strs/symbols/alpha-numerics for Emp Number and salary..")
	except cx_Oracle.DatabaseError as db:
		print("Problem in Database:",db)

