#include <stdlib.h>
#include <stdio.h>
#include <iostream>

#include <mysql_connection.h>
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/statement.h>
#include <cppconn/resultset.h>

using namespace std;
using namespace sql;
int main(void)
{
  try {
    sql::Driver *driver;
    sql::Connection *con;
    sql::Statement *stmt;
    sql::ResultSet *res;

    driver = get_driver_instance();
    con = driver->connect("localhost", "root", "123456");

    con->setSchema("simplify");
    stmt = con->createStatement();
    res = stmt->executeQuery("SELECT * FROM admin;");

    while(res->next()) {

      cout << "id: " << res->getInt(1) << endl;
      cout << "nome: " << res->getString(2) << endl;
      cout << "cargo: " << res->getString(3) << endl;
      cout << "user: " << res->getString(4) << endl;
      cout << "senha: " << res->getString(5) << endl;

    }


    delete res;
    delete stmt;
    delete con;

  } catch (sql::SQLException &e) {
    cout << "# ERR: " << e.what();
    cout << " (MySQL error code: " << e.getErrorCode();
    cout << ", SQLState: " << e.getSQLState() << " )" << endl;
  }


  return EXIT_SUCCESS;
}
