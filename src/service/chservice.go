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

//tracking 日志insert sql
func InsertSqlOfTracking() string {
	return "insert into fs_logdata.tracking_debug values(?,?,?,?,?)"
}

//insert封装
func InsertIntoCHExec(insertdate, trackingtype, strategyId, creativeId, deviceID, ipAddress, timestamp string) {

	if ChDB == nil {
		log.Printf("db no init")
		return
	}

	tx, err := ChDB.Begin()
	stmt, err := tx.Prepare(InsertSqlOfTracking())

	defer stmt.Close()

	if _, err := stmt.Exec(
		insertdate, trackingtype, strategyId, creativeId, deviceID, ipAddress, timestamp,
	); err != nil {
		log.Fatal(err)
	}

	if err = tx.Commit(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("---------------------------------")
}
