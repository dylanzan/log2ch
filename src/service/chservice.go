package service

import (
	"database/sql"
	"fmt"
	"github.com/ClickHouse/clickhouse-go"
	"log"
)

var ChDB *sql.DB

const (
	_dbUrl          = "tcp://121.5.252.185:9000?debug=true"
	_clickhouse_tag = "clickhouse"
)

//clickhouse 初始化
func InitChDB() {

	var err error
	ChDB, err = sql.Open(_clickhouse_tag, _dbUrl)

	if err = ChDB.Ping(); err != nil {
		if exception, ok := err.(*clickhouse.Exception); ok {
			fmt.Printf("[%d] %s \n%s\n", exception.Code, exception.Message, exception.StackTrace)
		} else {
			fmt.Println(err)
		}
		return
	}
}

//insert封装
func InsertIntoCHExec(insertSqlStr string) {

	if ChDB == nil {
		log.Printf("db no init")
		return
	}

	tx, err := ChDB.Begin()
	stmt, err := tx.Prepare(insertSqlStr)

	defer stmt.Close()

	if err = tx.Commit(); err != nil {
		log.Fatal(err)
	}

}
