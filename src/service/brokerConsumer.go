package service

import (
	"fmt"
	"github.com/Shopify/sarama"
	cluster "github.com/bsm/sarama-cluster"
	"log"
	"sync"
)

var(
	wg sync.WaitGroup

	kafkaConsumer *cluster.Consumer
	kafkaBrokers = []string{_masterKafkaURL,_slaverKafkaURL}

)

const (
	_masterKafkaURL = "121.5.252.185:9092"
	_slaverKafkaURL = "1.116.69.194:9092"

	_topicName="tracking"
)

type BrokerConsumer struct {

}

func (BrokerConsumer)GetData(){

	consumer,err:=sarama.NewConsumer([]string{_masterKafkaURL,_slaverKafkaURL},nil)

	if err!=nil{
		log.Fatal(err)
	}
	defer consumer.Close()

	fmt.Println(consumer.Topics())
	partitionList,err:=consumer.Partitions(_topicName)

	if err!=nil{
		log.Fatal(err)
	}

	for partition:=range partitionList{

		pc,err:=consumer.ConsumePartition(_topicName,int32(partition),sarama.OffsetNewest)

		if err!=nil{
			log.Fatal(err)
		}

		defer pc.AsyncClose()

		wg.Add(1)

		go func(sarama.PartitionConsumer) {
			defer wg.Done()
			for msg:=range pc.Messages(){
				fmt.Printf("Partition:%d, Offset:%d, Key:%s, Value:%s\n", msg.Partition, msg.Offset, string(msg.Key), string(msg.Value))
			}
		}(pc)

		wg.Wait()
	}

}
