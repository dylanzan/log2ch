package trackingmodel

import "fmt"

//存入ch's db tracking的日志参数
type TrackingLogModel struct {
	InsertDate string `json:"insert_date"`
	StrategyId string `json:"strategy_id"`
	CreativeId string `json:"creative_id"`
	DeviceId string `json:"device_id"`
	IpAddress string `json:"ip_address"`
	Timestamp string `json:"timestamp"`
}

//tracking 日志insert sql
func insertSqlOfTracking(insertdate,strategyId,creativeId,deviceID,ipAddress,timestamp string) string{
	return fmt.Sprintf("insert into logdata.tracking_test values(%v,%v,%v,%v,%v,%v)",insertdate,strategyId,creativeId,deviceID,ipAddress,timestamp)
}