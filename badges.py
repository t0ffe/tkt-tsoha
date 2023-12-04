from db import db
from flask import jsonify
from sqlalchemy.sql import text

def add_badge(student_organization, amount, price, name, designer_id, supplier_id):
    sql = "INSERT INTO badges (student_organization, amount, price, name, designer_id, supplier_id) VALUES (:student_organization, :amount, :price, :name, :designer_id, :supplier_id)"
    
    try:
        db.session.execute(text(sql), {"student_organization":student_organization, "amount":amount, "price":price, "name":name, "designer_id":designer_id, "supplier_id":supplier_id})
        db.session.commit()
        return jsonify({'message': 'Badge added successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()    

def removeBadge(badge_id):
    sql = "DELETE FROM badges WHERE id = :id"
    db.session.execute(sql, {"id":badge_id})
    db.session.commit()
    return True

def updateBadge():
    return

def getAllSuppliers():
    sql = "SELECT id, name FROM badge_supplier"
    result = db.session.execute(text(sql))
    suppliers = result.fetchall()
    return suppliers

def getAllDesigners():
    sql = "SELECT id, name FROM badge_designers"
    result = db.session.execute(text(sql))
    designers = result.fetchall()
    return designers


def getAllBadges():
    sql = "SELECT id, name, amount FROM badges"
    result = db.session.execute(text(sql))
    badges = result.fetchall()
    return badges