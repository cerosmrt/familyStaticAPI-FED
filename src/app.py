from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")

jackson_family.add_member({
    'id': 1,
    'first_name': 'John',
    'age': 33,
    'lucky_numbers': [7, 13, 22]
})

jackson_family.add_member({
    'id': 2,
    'first_name': 'Jane',
    'age': 35,
    'lucky_numbers': [10, 14, 3]
})

jackson_family.add_member({
    'id': 3,
    'first_name': 'Jimmy',
    'age': 5,
    'lucky_numbers': [1]
})

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200

@app.route('/member', methods=['POST'])
def add_member():
    member_info = request.get_json()
    if not member_info:
        return jsonify({"error": "Bad Request"}), 400
    jackson_family.add_member(member_info)
    return jsonify(member_info), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.delete_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify({"done": True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)