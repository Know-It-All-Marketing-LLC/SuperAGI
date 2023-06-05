import json
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from superagi.models.base_model import DBBaseModel


class AgentExecution(DBBaseModel):
    __tablename__ = 'agent_executions'

    id = Column(Integer, primary_key=True)
    status = Column(String)  # like ('CREATED', 'RUNNING', 'PAUSED', 'COMPLETED', 'TERMINATED')
    name = Column(String)
    agent_id = Column(Integer)
    name = Column(String)
    last_execution_time = Column(DateTime)
    num_of_calls = Column(Integer, default=0)
    num_of_tokens = Column(Integer, default=0)
    current_step_id = Column(Integer)

    def __repr__(self):
        return f"AgentExecution(id={self.id}, name={self.name},status='{self.status}', " \
               f"last_execution_time='{self.last_execution_time}', current_step_id={self.current_step_id}, " \
               f"agent_id={self.agent_id}, num_of_calls={self.num_of_calls})"

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'agent_id': self.agent_id,
            'current_step_id': self.current_step_id,
            'num_of_calls': self.num_of_calls,
            'last_execution_time': self.last_execution_time.isoformat()
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        last_execution_time = datetime.fromisoformat(data['last_execution_time'])
        return cls(
            id=data['id'],
            name=data['name'],
            status=data['status'],
            agent_id=data['agent_id'],
            calls=data['calls'],
            last_execution_time=last_execution_time
        )
