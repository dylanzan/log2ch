package service

import "testing"

func TestBrokerConsumer_GetData(t *testing.T) {

	InitChDB()

	var brokerConsumer = &BrokerConsumer{}

	brokerConsumer.InsertDataToCH()
}
