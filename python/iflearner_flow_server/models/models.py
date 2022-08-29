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

import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from iflearner_flow_server.utils.conf import conf_inst
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql import func

db = SQLAlchemy()


def auto_alter_tables(flask_app):
    """自动修改表结构.

    :param flask_app:
    :return:
    """
    with flask_app.app_context():
        metadata = sqlalchemy.MetaData()
        tables = {
            table_name: {
                column.name: column
                for column in sqlalchemy.Table(
                    table_name, metadata, autoload=True, autoload_with=db.engine
                ).c
            }
            for table_name in db.engine.table_names()
        }
        models = db.Model.__subclasses__()
        for model_class in models:
            table_name = model_class.__table__.name
            if table_name in tables:
                table = tables[table_name]
                for attr_name in dir(model_class):
                    attr = getattr(model_class, attr_name)
                    if (
                        isinstance(attr, InstrumentedAttribute)
                        and hasattr(attr, "type")
                        and hasattr(attr, "compile")
                    ):
                        attr_name = attr.name
                        # 添加新字段
                        if attr_name not in table:
                            column_type = attr.type.compile(dialect=db.engine.dialect)
                            db.engine.execute(
                                "ALTER TABLE %s ADD COLUMN %s %s"
                                % (table_name, attr_name, column_type)
                            )


class Task(db.Model):  # type: ignore
    __tablename__ = "t_task"
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String(32), unique=True, index=True)
    template_id = db.Column(db.String(32))

    name = db.Column(db.String(100), unique=True, nullable=True)
    status = db.Column(db.String(20))
    remark = db.Column(db.Text)
    modify_time = db.Column(
        db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()
    )
    create_time = db.Column(db.TIMESTAMP, server_default=func.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TaskParty(db.Model):  # type: ignore
    __tablename__ = "t_task_party"
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String(32), db.ForeignKey("t_task.task_id"), index=True)
    party_name = db.Column(db.String(100))
    volumes = db.Column(db.Text)

    task = db.relationship("Task", backref=db.backref("parties", lazy=True))

    def as_dict(self):
        return {"federated_id": self.party_name, "federated_data": self.volumes}


class Template(db.Model):  # type: ignore
    __tablename__ = "t_template"
    id = db.Column(db.String(32), primary_key=True, comment="模板id")
    name = db.Column(
        db.String(50), unique=True, index=True, nullable=False, comment="模板名"
    )
    image_url = db.Column(
        db.String(255),
        nullable=False,
        comment="镜像url",
    )
    remark = db.Column(db.Text, nullable=False, default="", comment="模板备注")
    workdir = db.Column(db.String(255), nullable=False, default="", comment="工作目录")
    command = db.Column(db.String(255), nullable=False, default="", comment="启动命令")
    hyper_parameter = db.Column(db.Text, nullable=True, comment="任务启动超参")
    modify_time = db.Column(
        db.TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
        comment="更新时间",
    )
    create_time = db.Column(db.TIMESTAMP, server_default=func.now(), comment="创建时间")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


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
    auto_alter_tables(app)
    with app.app_context():
        db.create_all()
    return app
