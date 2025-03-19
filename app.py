from flask import Flask,jsonify,render_template

todo = Flask(__name__)

students= [
    {
        'id':1,
        'name':'Hemanth',
        'age':20
    },
{
        'id':2,
        'name':'Pramod',
        'age':20
    },
{
        'id':3,
        'name':'Harish',
        'age':21
    }
]

@todo.route('/student-list')
def get_student_list():
    return jsonify(students)

@todo.route('/student/get/<int:id>')
def student_get_id(id):
    for student in students:
        if student['id'] == id:
            return jsonify(student)
    return jsonify('not found')

if __name__ == '__main__':
    todo.run(
        debug=True
    )