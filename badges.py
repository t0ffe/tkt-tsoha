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

def updateBadge(badge_id, name, amount, price):
    sql = "UPDATE badges SET name=:name, amount=:amount, price=:price WHERE id = :id"
    db.session.execute(sql, {"id":badge_id, "name":name, "amount":amount, "price":price})
    db.session.commit()
    return True

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
    sql = "SELECT id, name, amount, price FROM badges"
    result = db.session.execute(text(sql))
    badges = result.fetchall()
    return badges

def getOneBadge(badge_id):
    sql = "SELECT id, name, amount, price FROM badges WHERE id=:badge_id"
    result = db.session.execute(text(sql), {"badge_id":badge_id})
    badge = result.fetchone()
    return badge

def addDesigner(designer):
    sql = "INSERT INTO badge_designers (name) VALUES (:name)"
    try:
        db.session.execute(text(sql), {"name":designer})
        db.session.commit()
        return jsonify({'message': 'designer added successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()

def addSupplier(supplier):
    sql = "INSERT INTO badge_supplier (name) VALUES (:name)"
    try:
        db.session.execute(text(sql), {"name":supplier})
        db.session.commit()
        return jsonify({'message': 'supplier added successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()