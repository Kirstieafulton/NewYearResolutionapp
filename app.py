from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = [
    {'id': 1, 'task': 'Learn a new language', 'completed': False, 'comment': ''},
    {'id': 2, 'task': 'Exercise regularly', 'completed': True, 'comment': ''},
    # ... more tasks
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/edit_task/<int:task_id>')
def edit_task(task_id):
    task = next(task for task in tasks if task['id'] == task_id)
    return render_template('edit_task.html', task=task)

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = next(task for task in tasks if task['id'] == task_id)
    task['task'] = request.form['task']
    task['completed'] = request.form.get('completed') == 'on'
    task['comment'] = request.form.get('comment', '')  # Retrieve and handle empty comments
    return redirect('/')

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = request.form['new_task']
    next_id = max(task['id'] for task in tasks) + 1
    tasks.append({'id': next_id, 'task': new_task, 'completed': False})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

