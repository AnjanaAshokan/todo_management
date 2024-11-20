from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from todo_app.app.models import Project, Todo
from todo_app.app import db
from utils import export_as_gist

bp = Blueprint('routes', __name__)

@bp.route('/')
@login_required
def home():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)

@bp.route('/project/create', methods=['GET', 'POST'])
@login_required
def create_project():
    if request.method == 'POST':
        title = request.form['title']
        project = Project(title=title)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('routes.home'))
    return render_template('create_project.html')

@bp.route('/project/<int:project_id>', methods=['GET', 'POST'])
@login_required
def view_project(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        description = request.form['description']
        todo = Todo(description=description, project_id=project.id)
        db.session.add(todo)
        db.session.commit()
    return render_template('view_project.html', project=project)

@bp.route('/project/<int:project_id>/export')
@login_required
def export_project(project_id):
    project = Project.query.get_or_404(project_id)
    gist_url = export_as_gist(project)
    if gist_url:
        flash(f'Project exported successfully! View it here: {gist_url}', 'success')
    else:
        flash('Failed to export project. Please try again.', 'danger')
    return redirect(url_for('routes.view_project', project_id=project_id))
