package service

import (
	_ "github.com/ClickHouse/clickhouse-go"
	"github.com/jmoiron/sqlx"
	"log"
)

var ChDB *sqlx.DB

const (
	_dbUrl = "tcp://121.5.252.185:9000?debug=true"
	_clickhouse_tag="clickhouse"
)

//clickhouse 初始化
func InitChDB()  {

	var err error

	ChDB,err=sqlx.Open(_clickhouse_tag,_dbUrl)

	if err!=nil{
		log.Fatal(err)
	}
}

//insert封装
func InsertIntoCHExec(insertSqlStr string){

	if ChDB==nil{
		log.Printf("db no init")
		return
	}

	_,err:=ChDB.Exec(insertSqlStr)

	if err!=nil{
		log.Printf("insert failed,err: %v \n ",err)
		return
	}

}
