import json

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .database import SessionLocal, EmployeeDB
from .models import Employee

# Load config files
with open("config.json") as config_file:
    data = json.load(config_file)
    PROJECT_NAME = data["project_name"]


def get_application():
    "FastAPI app configuration"
    _app = FastAPI(title=PROJECT_NAME)
    _app.add_middleware(
        CORSMiddleware,
        # allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return _app


# Load The App and Models
app = get_application()
print("Loading Application... This may take a while")


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Routes
@app.get("/", response_model=str, tags=["Home"])
async def get_home():
    return f"Welcome to {PROJECT_NAME} API! Use routes '/docs' to try out Interactive docs or '/redoc' for documentation."


@app.post("/employees/", response_model=Employee, tags=["Employees"])
def create_employee(employee: Employee, db: Session = Depends(get_db)) -> EmployeeDB:
    """
    Create a new employee.

    Args:
        employee (Employee): Employee data to be created.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        Employee: Created employee data.
    """
    db_employee = EmployeeDB(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


@app.get("/employees/{employee_id}", response_model=Employee, tags=["Employees"])
def read_employee(employee_id: int, db: Session = Depends(get_db)) -> EmployeeDB:
    """
    Get employee data by employee ID.

    Args:
        employee_id (int): Employee ID.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        Employee: Employee data.
    """
    employee = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.get("/employees/", response_model=list[Employee], tags=["Employees"])
def read_employees(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
) -> list[EmployeeDB]:
    """
    Get a list of employees.

    Args:
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to retrieve. Defaults to 10.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        List[Employee]: List of employee data.
    """
    employees = db.query(EmployeeDB).offset(skip).limit(limit).all()
    return employees


@app.delete("/employees/{employee_id}", response_model=Employee, tags=["Employees"])
def delete_employee(employee_id: int, db: Session = Depends(get_db)) -> EmployeeDB:
    """
    Delete an employee by employee ID.

    Args:
        employee_id (int): Employee ID.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        Employee: Deleted employee data.
    """
    employee = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(employee)
    db.commit()
    return employee


@app.put(
    "/employees/{employee_id}/{column}/{new_value}",
    response_model=Employee,
    tags=["Employees"],
)
def update_employee(
    employee_id: int, column: str, new_value: str, db: Session = Depends(get_db)
) -> EmployeeDB:
    """
    Update employee data.

    Args:
        employee_id (int): Employee ID.
        column (str): Column to update (name, department).
        new_value (str): New value for the column.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        Employee: Updated employee data.
    """
    employee = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    setattr(employee, column, new_value)
    db.commit()
    db.refresh(employee)
    return employee
