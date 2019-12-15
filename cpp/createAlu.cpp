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
    prep_stmt = con->prepareStatement("INSERT INTO aluno(nome,curso,serie,matricula) VALUES(?,?,?,?);");

    char nome[255];
    char curso[255];
    char serie[255];
    char matricula[255];

    cin >> (nome);
    cin >> (curso);
    cin >> (serie);
    cin >> (matricula);

    prep_stmt->setString(1,nome);
    prep_stmt->setString(2,curso);
    prep_stmt->setString(3,serie);
    prep_stmt->setString(4,serie);

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
