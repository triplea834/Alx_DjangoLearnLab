## Permissions and Groups Setup

Custom permissions were added to the Book model:
- can_view
- can_create
- can_edit
- can_delete

User Groups:
- Viewers: can_view
- Editors: can_create, can_edit
- Admins: all permissions

Permissions are enforced using the @permission_required decorator in views.
ss