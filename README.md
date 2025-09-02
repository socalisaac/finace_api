Install driver for MS SQL Server Local:
    https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17
    
Install Packages needed for porject stored in requirements.txt:
    psycopg2-binary
    python-dotenv
    pyodbc

You can run when creating a new env you can run:
    (Optional) Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    (Optional) conda init powershell
    (Optional) conda init cmd.exe
    conda create --name myenv python=3.11
    conda activate myenv
    pip install -r requirements.txt