import uuid
from datetime import datetime
from sqlalchemy import (
    Column, String, Boolean, Integer, Float, Text, 
    ForeignKey, DateTime, Date, JSON
)
from sqlalchemy.orm import relationship
from database.db import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)  # Stored hashed
    created_at = Column(DateTime, default=datetime.utcnow)
    
    resumes = relationship("Resume", back_populates="user", cascade="all, delete-orphan")
    
class Resume(Base):
    __tablename__ = "resumes"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    section_settings = Column(JSON, default=list)  # Store section visibility and order
    
    user = relationship("User", back_populates="resumes")
    personal_info = relationship("PersonalInfo", back_populates="resume", uselist=False, cascade="all, delete-orphan")
    education = relationship("Education", back_populates="resume", cascade="all, delete-orphan")
    experience = relationship("Experience", back_populates="resume", cascade="all, delete-orphan")
    skills = relationship("Skill", back_populates="resume", cascade="all, delete-orphan")
    projects = relationship("Project", back_populates="resume", cascade="all, delete-orphan")
    achievements = relationship("Achievement", back_populates="resume", cascade="all, delete-orphan")
    extracurriculars = relationship("Extracurricular", back_populates="resume", cascade="all, delete-orphan")
    courses = relationship("Course", back_populates="resume", cascade="all, delete-orphan")
    certifications = relationship("Certification", back_populates="resume", cascade="all, delete-orphan")
    volunteer_work = relationship("VolunteerWork", back_populates="resume", cascade="all, delete-orphan")
    publications = relationship("Publication", back_populates="resume", cascade="all, delete-orphan")

class PersonalInfo(Base):
    __tablename__ = "personal_info"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    location = Column(String)
    linkedin = Column(String)
    github = Column(String)
    portfolio = Column(String)
    
    resume = relationship("Resume", back_populates="personal_info")

class Education(Base):
    __tablename__ = "education"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    institution = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    field_of_study = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    gpa = Column(Float)
    description = Column(Text)
    
    resume = relationship("Resume", back_populates="education")

class Experience(Base):
    __tablename__ = "experience"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    company = Column(String, nullable=False)
    position = Column(String, nullable=False)
    location = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    current = Column(Boolean, default=False)
    description = Column(Text)
    achievements = Column(JSON)  # List of achievements as strings
    
    resume = relationship("Resume", back_populates="experience")

class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    name = Column(String, nullable=False)
    level = Column(String)  # beginner, intermediate, advanced, expert
    category = Column(String)  # technical, soft, language, etc.
    
    resume = relationship("Resume", back_populates="skills")

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    technologies = Column(JSON)  # List of technologies as strings
    start_date = Column(Date)
    end_date = Column(Date)
    link = Column(String)
    
    resume = relationship("Resume", back_populates="projects")

class Achievement(Base):
    __tablename__ = "achievements"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    date = Column(Date)
    issuer = Column(String)
    
    resume = relationship("Resume", back_populates="achievements")

class Extracurricular(Base):
    __tablename__ = "extracurriculars"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    activity = Column(String, nullable=False)
    organization = Column(String)
    role = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(Text)
    
    resume = relationship("Resume", back_populates="extracurriculars")

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    name = Column(String, nullable=False)
    institution = Column(String)
    date_completed = Column(Date)
    description = Column(Text)
    
    resume = relationship("Resume", back_populates="courses")

class Certification(Base):
    __tablename__ = "certifications"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    name = Column(String, nullable=False)
    issuer = Column(String)
    date = Column(Date)
    credential_id = Column(String)
    url = Column(String)
    
    resume = relationship("Resume", back_populates="certifications")

class VolunteerWork(Base):
    __tablename__ = "volunteer_work"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    organization = Column(String, nullable=False)
    role = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(Text)
    
    resume = relationship("Resume", back_populates="volunteer_work")

class Publication(Base):
    __tablename__ = "publications"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, ForeignKey("resumes.id"))
    title = Column(String, nullable=False)
    authors = Column(JSON)  # List of authors as strings
    publication = Column(String)
    date = Column(Date)
    url = Column(String)
    description = Column(Text)
    
    resume = relationship("Resume", back_populates="publications")

# api/schemas.py
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import date, datetime
import uuid

# User schemas
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True

# Resume section schemas
class PersonalInfoSchema(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None

    class Config:
        orm_mode = True

class EducationSchema(BaseModel):
    institution: str
    degree: str
    field_of_study: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    gpa: Optional[float] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class ExperienceSchema(BaseModel):
    company: str
    position: str
    location: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    current: Optional[bool] = False
    description: Optional[str] = None
    achievements: Optional[List[str]] = []

    class Config:
        orm_mode = True

class SkillSchema(BaseModel):
    name: str
    level: Optional[str] = None
    category: Optional[str] = None

    class Config:
        orm_mode = True

class ProjectSchema(BaseModel):
    title: str
    description: Optional[str] = None
    technologies: Optional[List[str]] = []
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    link: Optional[str] = None

    class Config:
        orm_mode = True

class AchievementSchema(BaseModel):
    title: str
    description: Optional[str] = None
    date: Optional[date] = None
    issuer: Optional[str] = None

    class Config:
        orm_mode = True

class ExtracurricularSchema(BaseModel):
    activity: str
    organization: Optional[str] = None
    role: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class CourseSchema(BaseModel):
    name: str
    institution: Optional[str] = None
    date_completed: Optional[date] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class CertificationSchema(BaseModel):
    name: str
    issuer: Optional[str] = None
    date: Optional[date] = None
    credential_id: Optional[str] = None
    url: Optional[str] = None

    class Config:
        orm_mode = True

class VolunteerWorkSchema(BaseModel):
    organization: str
    role: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class PublicationSchema(BaseModel):
    title: str
    authors: Optional[List[str]] = []
    publication: Optional[str] = None
    date: Optional[date] = None
    url: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class ResumeSectionSchema(BaseModel):
    name: str
    visible: bool = True
    order: int

    class Config:
        orm_mode = True

# Resume schemas
class ResumeCreate(BaseModel):
    title: str
    summary: Optional[str] = None
    section_settings: Optional[List[ResumeSectionSchema]] = []

class ResumeUpdate(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    section_settings: Optional[List[ResumeSectionSchema]] = None

class ResumeResponse(BaseModel):
    id: str
    user_id: str
    title: str
    summary: Optional[str] = None
    section_settings: List[ResumeSectionSchema]
    personal_info: Optional[PersonalInfoSchema] = None
    education: List[EducationSchema] = []
    experience: List[ExperienceSchema] = []
    skills: List[SkillSchema] = []
    projects: List[ProjectSchema] = []
    achievements: List[AchievementSchema] = []
    extracurriculars: List[ExtracurricularSchema] = []
    courses: List[CourseSchema] = []
    certifications: List[CertificationSchema] = []
    volunteer_work: List[VolunteerWorkSchema] = []
    publications: List[PublicationSchema] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Services schemas
class ResumeOptimizeRequest(BaseModel):
    job_description: str

class ResumeOptimizeResponse(BaseModel):
    score: float
    suggestions: List[str]
    optimized_summary: Optional[str] = None
    keyword_matches: dict