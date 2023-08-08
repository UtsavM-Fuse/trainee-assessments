import streamlit as st
import pandas as pd

from database import Employee, Department, SessionLocal


# Page 1: Employee Data Entry
def employee_page():
    st.header("Employee Data Entry")
    empno = st.text_input("Employee Number (Empno)")
    ename = st.text_input("Employee Name (Ename)")
    job = st.text_input("Job")
    deptno = st.text_input("Department Number (Deptno)")
    if st.button("Add Employee"):
        db = SessionLocal()
        employee = Employee(empno=empno, ename=ename, job=job, deptno=deptno)
        db.add(employee)
        db.commit()
        db.close()
        st.success("Employee added successfully!")


# Page 2: Department Data Entry
def department_page():
    st.header("Department Data Entry")
    deptno = st.text_input("Department Number (Deptno)")
    dname = st.text_input("Department Name (Dname)")
    loc = st.text_input("Location (Loc)")
    if st.button("Add Department"):
        db = SessionLocal()
        department = Department(deptno=deptno, dname=dname, loc=loc)
        db.add(department)
        db.commit()
        db.close()
        st.success("Department added successfully!")


# Page 3: Data Visualization
def visualization_page():
    st.header("Data Visualization")
    db = SessionLocal()
    employees = db.query(Employee).all()
    departments = db.query(Department).all()
    db.close()

    # Merge employee and department data based on Deptno
    merged_data = []
    for emp in employees:
        dept = next((dep for dep in departments if dep.deptno == emp.deptno), None)
        if dept:
            merged_data.append(
                {
                    "Empno": emp.empno,
                    "Ename": emp.ename,
                    "Deptno": emp.deptno,
                    "Dname": dept.dname,
                }
            )

    st.dataframe(pd.DataFrame(merged_data))


# Main App
def main():
    st.title("Data Entry and Visualization App")
    menu = ["Employee Data Entry", "Department Data Entry", "Data Visualization"]
    choice = st.sidebar.selectbox("Select Page", menu)

    if choice == "Employee Data Entry":
        employee_page()
    elif choice == "Department Data Entry":
        department_page()
    else:
        visualization_page()


if __name__ == "__main__":
    main()
