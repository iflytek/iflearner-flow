#  Copyright 2022 iFLYTEK. All Rights Reserved.
#  #
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  #
#      http://www.apache.org/licenses/LICENSE-2.0
#  #
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  ==============================================================================
from urllib.parse import quote

DATABASES: dict = {
    "NAME": "gx_day16",
    "USER": "ifly_dlaas",
    "PASSWORD": "ozEUd$0%6@M4",
    "HOST": "172.31.164.79",
    "PORT": 32306,
    "OPTIONS": {
        "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",  # MySQL Strict Mode设置
    },
}


# 全局通用配置类
class Config(object):
    """项目配置核心类."""

    # Debug Mode
    DEBUG: bool = False

    # 配置日志
    LOG_LEVEL: str = "DEBUG"
    LOG_PATH: str = "log/iflearner-flow-server.log"

    # 数据库连接格式
    SQLALCHEMY_DATABASE_URI: str = "mysql+pymysql://{}:{}@{}:{}/{}".format(
        DATABASES["USER"],
        quote(DATABASES["PASSWORD"]),
        DATABASES["HOST"],
        DATABASES["PORT"],
        DATABASES["NAME"],
    )
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO: bool = False
    # 数据库连接池的大小
    SQLALCHEMY_POOL_SIZE: int = 10
    # 指定数据库连接池的超时时间
    SQLALCHEMY_POOL_TIMEOUT: int = 10
    # 控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃。
    SQLALCHEMY_MAX_OVERFLOW: int = 2

    # iflearner-operator配置
    IFLEARNER_SERVER_IMAGE = "iflearner:0.1.2"
    IFLEARNER_SERVER_ARGS = ["python", "iflearner/business/homo/aggregate_server.py"]


def conf_init(app):
    app.config.from_object(Config)
    return app
