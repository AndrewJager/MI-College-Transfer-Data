from flask import render_template, Blueprint
from flask_login import current_user, login_required

admin_blueprint = Blueprint(
    'admin', __name__,
    template_folder='templates'
)

@admin_blueprint.route('/admin')
@login_required
def admin():
    user = current_user
    return render_template('admin.html', user=user)