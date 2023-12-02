from db import db
from flask import jsonify
from sqlalchemy.sql import text

def add_org(student_organization):
    sql = "INSERT INTO student_organization (name) VALUES (:name)"
    try:
        db.session.execute(text(sql), {"name":student_organization})
        db.session.commit()
        return jsonify({'message': 'Student organization added successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()    

