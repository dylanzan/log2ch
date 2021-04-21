package trackingmodel

//存入ch's db tracking的日志参数
type TrackingLogModel struct {
	InsertDate   string `json:"insert_date"`
	TrackingType string `json:"tracking_type"`
	StrategyId   string `json:"strategy_id"`
	CreativeId   string `json:"creative_id"`
	DeviceId     string `json:"device_id"`
	IpAddress    string `json:"ip_address"`
	Timestamp    string `json:"timestamp"`
}
