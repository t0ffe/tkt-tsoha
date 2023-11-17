from db import db
from flask import jsonify
from sqlalchemy.sql import text

def add_badge(collection_id, amount, price, name, designer, supplier):
    sql = "INSERT INTO badges (collection_id, amount, price, name, designer, supplier) VALUES (:collection_id, :amount, :price, :name, :designer, :supplier)"
    
    try:
        db.session.execute(text(sql))
        db.session.commit()
        return jsonify({'message': 'Badge added successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()    

def removeBadge(badge_id, user_id):
    sql = "UPDATE badges SET visible=0 WHERE id=:id AND creator_id=:user_id"
    db.session.execute(sql, {"id":badge_id, "user_id":user_id})
    db.session.commit()

