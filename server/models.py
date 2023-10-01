from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        if name =="":
            raise ValueError("name cannot be blank")
        return name

    @validates('name2')
    def validate_name2(self, key, name):
        author_name = Author.query.filter_by(name=name).first() 
        if author_name:
            raise IntegrityError("a similar name exists")
        return name

    phone_number = db.Column(db.String)

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("phone_number must contain 10 digits")
        return phone_number


    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    @validates('title')
    def validate_title(self, key, title):
        if title =="":
            raise ValueError("title cannot be blank")
        return title

    @validates('title2')
    def validate_custom_title(self, key, title):
        if "Won't Believe" not in title or "Secret" not in title or "Top [number]" not in title or "Guess" not in title :
            raise ValueError("title must contain atleat one of the following phrases")
        return title    

    content = db.Column(db.String)

    @validates('content')
    def validate_content (self, key, content):
        if not len(content) >= 250:
            raise ValueError("content must be atleast 250 characters long")
        return content

    category = db.Column(db.String)

    @validates('category')
    def validate_category(self, key, category):
        if category != "Fiction" or category != "Non-Fiction":
            raise ValueError("Post category must be either Fiction or Non-Fiction")
        return category


    summary = db.Column(db.String)

    @validates('summary')
    def validate_summary(self, key, summary):
        if not len(summary) <= 250:
            raise ValueError("post summary must be a maximum 250 characters long")
        return summary

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'