# clickhouse fs_report table fotmat

## tracking_report_by_hour_table
creative_id,day,hour_num,imp,clk,cst,win,impU1,impU2,impU3,impU4,impU5,impU6,impU7,impU8,impN1,impN2,impN3,impN4,impN5,impN6,impN7,impN8,impT1,impT2,impT3,impT4,impT5,impT6,impT7,impT8

```
CREATE TABLE fs_report.tracking_report_by_hour
(
    `creative_id` int32 COMMENT '创意id',
    `date` DateTime COMMENT '日期',
    `hour_num` int8 COMMENT '分小时',
    `imp` Int32 COMMENT '曝光次数',
    `clk` Int32 COMMENT '创意id',
    `cst` String COMMENT '设备id',
    `win` String COMMENT ' IP地址',
    `impU1` Int32 COMMENT '频次统计',
    `impU2` Int32,
    `impU3` Int32,
    `impU4` Int32,
    `impU5` Int32,
    `impU6` Int32,
    `impU7` Int32,
    `impU8` Int32,
    `impN1` Int32,
    `impN2` Int32,
    `impN3` Int32,
    `impN4` Int32,
    `impN5` Int32,
    `impN6` Int32,
    `impN7` Int32,
    `impN8` Int32,
    `impT1` Int32,
    `impT2` Int32,
    `impT3` Int32,
    `impT4` Int32,
    `impT5` Int32,
    `impT6` Int32,
    `impT7` Int32,
    `impT8` Int32
)
ENGINE = MergeTree
ORDER BY date
```



## tracking_report_by_date_table
creative_id,day,imp,clk,cst,win,impU1,impU2,impU3,impU4,impU5,impU6,impU7,impU8,impN1,impN2,impN3,impN4,impN5,impN6,impN7,impN8,impT1,impT2,impT3,impT4,impT5,impT6,impT7,impT8

```
CREATE TABLE fs_report.tracking_report_by_day
(
    `creative_id` int32 COMMENT '创意id',
    `date` DateTime COMMENT '日期',
    `imp` Int32 COMMENT '曝光次数',
    `clk` Int32 COMMENT '创意id',
    `cst` String COMMENT '设备id',
    `win` String COMMENT ' IP地址',
    `impU1` Int32 COMMENT '频次统计',
    `impU2` Int32,
    `impU3` Int32,
    `impU4` Int32,
    `impU5` Int32,
    `impU6` Int32,
    `impU7` Int32,
    `impU8` Int32,
    `impN1` Int32,
    `impN2` Int32,
    `impN3` Int32,
    `impN4` Int32,
    `impN5` Int32,
    `impN6` Int32,
    `impN7` Int32,
    `impN8` Int32,
    `impT1` Int32,
    `impT2` Int32,
    `impT3` Int32,
    `impT4` Int32,
    `impT5` Int32,
    `impT6` Int32,
    `impT7` Int32,
    `impT8` Int32
)
ENGINE = MergeTree
ORDER BY date
```