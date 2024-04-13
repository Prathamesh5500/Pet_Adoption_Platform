# Pet_Adoption_Platform
Super User - admin Password - 1234

// For the Error in Set up The error message "Error dropping database (can't rmdir '.\pet_info', errno: 41 "Directory not empty")" suggests that there are still files or directories present in the database directory for pet_info after attempting to drop the database.

1)To solve this issue, you can manually delete the directory for the pet_info database. Here are the steps to do so:

2)Stop the MySQL server to ensure that no new files are being written to the database directory. 3)Open a file explorer window and navigate to the data directory for your MySQL installation. The default location for the data directory depends on your operating system and MySQL installation method, but it is typically located in /var/lib/mysql on Linux or C:\ProgramData\MySQL\MySQL Server x.x\Data on Windows. 4)Locate the directory for the pet_info database. It should be named pet_info and located in the data directory. 5)Delete the pet_info directory. 6)Start the MySQL server again.

Open a command prompt or terminal window and navigate to your Django project directory. 1)Run the following command to create new database migrations: python manage.py makemigrations

This command will generate new migration files for your Django app based on the current state of your models. After the migration files have been generated, run the following command to apply the migrations to the database: 2) python manage.py migrate This command will apply the migrations to the database and create any necessary tables and columns.
