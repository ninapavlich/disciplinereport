from carbon.compounds.core.dashboard import BaseAdminDashboard

from .models import AdminSidebar, AdminAppGroup

class AdminDashboard(BaseAdminDashboard):
	sidebar_model = AdminSidebar
	main_model = AdminAppGroup
