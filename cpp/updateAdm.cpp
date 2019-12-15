#include <stdlib.h>
#include <stdio.h>
#include <iostream>

#include <mysql_connection.h>
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/prepared_statement.h>

using namespace std;
using namespace sql;
int main(void)
{
  try {
    sql::Driver *driver;
    sql::Connection *con;
    sql::PreparedStatement *prep_stmt;

    driver = get_driver_instance();
    con = driver->connect("localhost", "root", "123456");

    con->setSchema("simplify");
    prep_stmt = con->prepareStatement("UPDATE admin SET nome=?,cargo=?,user=?,senha=? WHERE id=?");

    // updated data
    //int id = 1;
    char name[255];
    char cargo[255];
    char user[255];
    char senha[255];

    cin >> (name);
    cin >> (cargo);
    cin >> (user);
    cin >> (senha);

    prep_stmt->setString(1,name);
    prep_stmt->setString(2,cargo);
    prep_stmt->setString(3,user);
    prep_stmt->setString(4,senha);
    //prep_stmt->setInt(3,id);

    prep_stmt->execute();



    delete prep_stmt;
    delete con;

  } catch (sql::SQLException &e) {
    cout << "# ERR: " << e.what();
    cout << " (MySQL error code: " << e.getErrorCode();
    cout << ", SQLState: " << e.getSQLState() << " )" << endl;
  }


  return EXIT_SUCCESS;
}
