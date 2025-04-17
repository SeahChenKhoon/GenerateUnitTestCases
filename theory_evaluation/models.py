from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()


class UserInfo(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    github_username = Column(String(50), nullable=False)
    payment_date = Column(TIMESTAMP(timezone=True))
    current_duration = Column(Integer)
    course_duration = Column(Integer)
    end_date = Column(TIMESTAMP(timezone=True))
    status = Column(Integer)


class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    repo_name = Column(String(255), nullable=False)
    problem_statement = Column(JSONB)
    bloblink = Column(Text)
    mini_project_flag = Column(Integer, nullable=False)
    ctime = Column(TIMESTAMP(timezone=True), server_default=func.now())


class SprintIssues(Base):
    __tablename__ = "sprint_issues"
    id = Column(Integer, primary_key=True)
    psid = Column(Integer, nullable=False)
    sprint_no = Column(Integer, nullable=False)
    issue_no = Column(Integer, nullable=False)
    title = Column(Text)
    description = Column(Text)
    max_evaluations = Column(Integer, nullable=False)
    last_issue_flag = Column(Integer, nullable=False)


class UserRepo(Base):
    __tablename__ = "user_repo"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_info.id"), nullable=False)
    psid = Column(Integer)
    github_username = Column(String(50), nullable=False)
    repo_name = Column(String(255), nullable=False)
    github_url = Column(String(255), nullable=False)
    __table_args__ = (
        UniqueConstraint("github_username", "repo_name", name="unique_user_repo"),
    )


class UserScoreLog(Base):
    __tablename__ = "user_score_log"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_info.id"), nullable=False)
    psid = Column(Integer, nullable=False)
    eval_sprint = Column(Integer, nullable=False)
    eval_issue = Column(Integer, nullable=False)
    stage = Column(Integer, nullable=False)
    score_number = Column(Float)
    score_status = Column(String(10))
    current_sprint = Column(Integer, nullable=False)
    current_issue = Column(Integer, nullable=False)
    num_tries = Column(Integer)
    max_tries = Column(Integer)
    ctime = Column(TIMESTAMP(timezone=True), server_default=func.now())


class CurrentUserTable(Base):
    __tablename__ = "current_user_table"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    psid = Column(Integer)
    current_sprint = Column(Integer)
    current_issue = Column(Integer)
    ctime = Column(TIMESTAMP(timezone=True))
    num_tries = Column(Integer)


class ConsultantChat(Base):
    __tablename__ = "consultant_chat"
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    consultant_history = Column(Text)
    modified_on = Column(TIMESTAMP(timezone=True), server_default=func.now())
    project_id = Column(Integer)


class MentorChat(Base):
    __tablename__ = "mentor_chat"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_info.id"), nullable=False)
    route = Column(String(10), nullable=False)
    sender_type = Column(String(10), nullable=False)
    message_content = Column(Text)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())


class Curriculum(Base):
    __tablename__ = "curriculum"
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    question = Column(Text, unique=True, nullable=False)
    marking_scheme = Column(Text, nullable=False)
    model_answer = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())


class TheoryEvalUserPerformance(Base):
    __tablename__ = "theory_eval_user_performance"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), ForeignKey("user_info.email"))
    question_id = Column(UUID(as_uuid=True), ForeignKey("curriculum.id"))
    user_response = Column(Text)
    llm_evaluation = Column(Text)
    llm_score = Column(Float)
    user_grade = Column(String)
    user_attempts = Column(Integer)
    llm_evaluation_status = Column(Integer)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())