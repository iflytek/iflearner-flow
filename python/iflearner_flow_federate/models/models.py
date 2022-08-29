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

from flask_sqlalchemy import SQLAlchemy
from iflearner_flow_federate.utils.conf import conf_inst

db = SQLAlchemy()


class User(db.Model):  # type: ignore
    # __tablename__ = 't_user'  # 设置表名, 表名默认为类名小写
    id = db.Column(db.Integer, primary_key=True)  # 设置主键, 默认自增
    name = db.Column("username", db.String(20), unique=True)  # 设置字段名 和 唯一约束
    age = db.Column(db.Integer, default=10, index=True)  # 设置默认值约束 和 索引


def models_init(app):
    database: dict = conf_inst.raw_dict["database"]
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}:{}/{}".format(
        database["user"],
        quote(database["password"]),
        database["host"],
        database["port"],
        database["name"],
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = database.get(
        "sqlalchemy_track_modifycations", False
    )
    app.config["SQLALCHEMY_ECHO"] = database.get("sqlalchemy_echo", False)
    app.config["SQLALCHEMY_POOL_SIZE"] = database.get("sqlalchemy_pool_size", 10)
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = database.get("sqlalchemy_pool_timeout", 10)
    app.config["SQLALCHEMY_MAX_OVERFLOW"] = database.get("sqlalchemy_pool_overflow", 10)
    app.config["DEBUG"] = conf_inst.raw_dict["flask"]["debug"]
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
